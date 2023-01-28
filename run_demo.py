import numpy as np
from cv2 import VideoCapture
from cv2 import bitwise_or

# local python files
import detect
import fn2
import palm
import finger_layer_iter
import draw_index

class PointsIndex:
    def __init__(self, camera_index, framework_name = 'mediapipe'):
        self.camX = camera_index
        camera = VideoCapture(self.camX)

        self.camera_ready = False
        if camera.isOpened():
            setup_result, frame = camera.read()
            if setup_result:
                self.height, self.width = frame.shape[:2]
                self.square_size = min(self.height, self.width)

                self.camera_ready = True
                camera.release()
        
        assert self.camera_ready,'Webcam ' + str(self.camX) + 'activation failed.'
        self.camera = VideoCapture(self.camX)

        # A DashBoard that showing a 2d Demo Hand color image
        self.demo_hand, self.demo_points = fn2.demo_hand(self.square_size)

        if framework_name == 'mediapipe':
            self.using_framework = framework_name
            # from map1 import marksX
            # self.marksX = marksX

            self.finger = dict()
            self.finger_layer = dict()
            self.two_points = dict()

    # get 2d infomation
    def scalars(self):
        ret, frame = self.camera.read()

        if self.using_framework == 'mediapipe':
            # get rectangle shaped frame into square shape
            frame = fn2.slip(frame) # 640*480 -> 480*480
            # mediapipe hand detection uses size of 256*256 as default

            self.number, self.left_or_right, labels = detect.it(frame)
            # number of hands; left or right; mediapipe labels -> landmarks xy

            if self.number == 1:
                self.origin_xy = detect.points(self.number, labels)

                numpy_xy = np.array(self.origin_xy)
                self.pixel_xy = numpy_xy * self.square_size

                # Palm
                self.clock_wise, self.deepth_distance, self.horizontals_lengths, self.virtical_length, self.middle_point, self.vector, self.palm_trangle_area = palm.update_palm(self.pixel_xy)
                self.t_ratio = self.virtical_length / self.horizontals_lengths
                # Hand ROI
                self.frame_crop = fn2.crop(frame, self.pixel_xy, self.deepth_distance)


                # Finger
                thumb, index_finger, middle_finger, ring_finger, little_finger = finger_layer_iter.fingers_a(self.pixel_xy)

                self.finger['thumb'] = thumb
                self.finger['index'] = index_finger
                self.finger['middle'] = middle_finger
                self.finger['ring'] = ring_finger
                self.finger['little'] = little_finger

                # Finger Layers
                layer1, layer2, layer3, layer4 = finger_layer_iter.layers(self.pixel_xy)

                self.finger_layer['head'] = layer1
                self.finger_layer['head_middle'] = layer2
                self.finger_layer['end_middle'] = layer3
                self.finger_layer['end_middle'] = layer4

                self.diffs_2d, self.fingers_middles = finger_layer_iter.finger_layers(self.pixel_xy)
                self.ratios = finger_layer_iter.diffs_ratio_13_23(self.diffs_2d)
            else:
                pass

        else:
            pass

    def get_mask(self):
        if self.number == 1:
            mask_stick = draw_index.stick_mask(self.pixel_xy, self.deepth_distance)
            mask_palm = draw_index.palm_mask(self.pixel_xy, self.deepth_distance)
            self.mask = bitwise_or(mask_stick, mask_palm)

    def neighbor_line(self):
        if self.number == 1:
            self.two_points['thumb'] = zip( self.finger['thumb'][:-1], self.finger['thumb'][1:] )
            self.two_points['index'] = zip( self.finger['index'][:-1], self.finger['index'][1:] )
            self.two_points['middle'] = zip( self.finger['middle'][:-1], self.finger['middle'][1:] )
            self.two_points['ring'] = zip( self.finger['ring'][:-1], self.finger['ring'][1:] )
            self.two_points['little'] = zip( self.finger['little'][:-1], self.finger['little'][1:] )



def test():
    real1 = PointsIndex(0)
    import cv2 as cv
    cv.imshow('Demo', real1.demo_hand)
    cv.waitKey(1500)

    if real1.camera_ready:
        import time
        time1 = time.time(); time2 = time1
        t_ratios = []
        while time2 - time1 < 30:
            real1.scalars()
            real1.get_mask()
            real1.neighbor_line()
            if real1.number == 1:
                t_ratios.append(real1.t_ratio)
                cv.imshow('Demo', real1.mask)

            if cv.waitKey(1) == ord('q'):
                break
            time2 = time.time()

    real1.camera.release()

test()
