import numpy as np
from cv2 import VideoCapture
from cv2 import bitwise_or

# local python files
import detect
import fn2
import palm
import finger
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
            from map1 import marksX
            self.marksX = marksX

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

                # get "distance" between camera and "Human Hand"
                self.distance = palm.points_distance(self.pixel_xy)

                # Hand ROI
                self.frame_crop = fn2.crop(frame, self.pixel_xy, self.distance)

                self.raio = palm.t_icon(self.pixel_xy)
                self.clock_wise = palm.clock_wise_check(self.pixel_xy)
                self.palm_middle, self.head_vector = palm.pointing(self.pixel_xy)
                self.diffs_2d, self.fingers_middles = finger.finger_layers(self.pixel_xy)
                self.ratios = finger.diffs_ratio_13_23(self.diffs_2d)
            else:
                pass

        else:
            pass

    def get_mask(self):
        if self.number == 1:
            mask_stick = draw_index.stick_mask(self.pixel_xy, self.distance)
            mask_palm = draw_index.palm_mask(self.pixel_xy, self.distance)
            self.mask = bitwise_or(mask_stick, mask_palm)



def test():
    real1 = PointsIndex(0)
    import cv2 as cv
    cv.imshow('Demo', real1.demo_hand)
    cv.waitKey(1500)

    if real1.camera_ready:
        import time
        time1 = time.time(); time2 = time1
        while time2 - time1 < 30:
            real1.scalars()
            real1.get_mask()
            if real1.number == 1:
                cv.imshow('Demo', real1.mask)

            if cv.waitKey(1) == ord('q'):
                break

    real1.camera.release()

test()