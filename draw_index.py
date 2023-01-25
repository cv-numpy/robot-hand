# Type of drawing

#1 Distance
#2 Angle
#3 XY
#4 Vector
#5 3d Vector
#6 Connecting the Dots
#7 Ratio
#8 LeftRight
#9 Text

# Where to draw

#1 on the point_xy
#2 Between two points
#3 Center of points
#5 draw on the DashBoard


import numpy as np
import cv2 as cv


import fn1
import map1
import u8
colors = [u8.red, u8.green, u8.blue, u8.yellow, u8.purple]


# Drawing
def draw_text(src, text, org, fontScale=0.5, color=u8.black, thickness=1):
    return cv.putText(src, text, [int(xy) for xy in org], cv.FONT_HERSHEY_SIMPLEX, fontScale, color, thickness, cv.LINE_AA)

# Show infomation at the coordinates
def local(image, location, bias_x = 0, bias_y = 0, info = None):
    print(info)
    if all(isinstance(ele, float) for ele in location):
        location = u8.point_to_pixel(location)
    if info is None:
        draw_text(image, str(location), (location[0]+int(bias_x), location[1]+int(bias_y)))
    else:
        draw_text(image, str(info), (location[0]+int(bias_x), location[1]+int(bias_y)))



# Draw heads in Init_Hand() detect_what()
def draw_heads(self, real, image):
    wrist_pixel = u8.point_to_pixel(real.wrist)
    heads_pixel = u8.points_to_pixels(real.headsMPxy)
    end_points_pixel = [u8.point_to_pixel(fn1.add(point, vector)) for point, vector in zip(real.headsMPxy, real.heads_vector)]
    for p1, p2 in zip(heads_pixel, end_points_pixel):
        cv.line(image, p1, p2, color = u8.white)
        cv.line(image, p1, wrist_pixel, color = u8.white)

# Draw palm normal vector
def draw_palm_normalV(self, real, image):
    for i, root in enumerate(real.planeV):
        end_point = u8.point_to_pixel(fn1.add(real.centr, root[:2]))
        if i == 0:
            cv.line(image, real.centr_p, end_point, color = u8.red1, thickness = 4)
        if i == 1:
            cv.line(image, real.centr_p, end_point, color = u8.red, thickness = 2)
        if i == 2:
            cv.line(image, real.centr_p, end_point, color = u8.blue1, thickness = 4)
        if i == 3:
            cv.line(image, real.centr_p, end_point, color = u8.blue, thickness = 2)


def draw_point_3d(self, image, Z2positive, Z2negtive):
    p1 = u8.point_to_pixel(Z2positive[0])
    p2 = u8.point_to_pixel(Z2positive[1])
    p3 = u8.point_to_pixel(Z2negtive[0])
    p4 = u8.point_to_pixel(Z2negtive[1])

    if p1 and p2 and p3 and p4:
        local(image, self.pixel_origin, 0, 0, (0,0,0))
        local(image, self.pixel_a, 0, -10, p1)
        local(image, self.pixel_a, 0, 0,   p3)
        local(image, self.pixel_b, 0, -10, p2)
        local(image, self.pixel_b, 0, 0,   p4)

        d1 = int(fn1.d(p1)); d2 = int(fn1.d(p2)); d3 = int(fn1.d(p1, p2))
        inside = str(d1) + ' + ' + str(d2) + ' + ' + str(d3) + ' = ' + str(d1 + d2 + d3)

        local(image, self.centr_P, -40, -10, inside)
    
        d4 = int(fn1.d(p3)); d5 = int(fn1.d(p4)); d6 = int(fn1.d(p3, p4))
        inside = str(d4) + ' + ' + str(d5) + ' + ' + str(d6) + ' = ' + str(d4 + d5 + d6)

        local(image, self.centr_P, -40, 10, inside)









from mediapipe import solutions
mp_drawing = solutions.drawing_utils
styles = solutions.drawing_styles
mp_hands = solutions.hands


def official(image, labels):
    mp_drawing.draw_landmarks(image, labels, mp_hands.HAND_CONNECTIONS, \
    styles.get_default_hand_landmarks_style(), \
        styles.get_default_hand_connections_style())

def draw_pov_fingers(image, pixel_xy, fingersX):
    for fingerX in fingersX:
        for pointX in fingerX:

            cv.circle(image, pixel_xy[pointX], 5, (100,100,200), -1)
def draw_pov_bones(image, pixel_xy, bonesX):
    colors = [color for color in map.finger_color]
    for boneX in bonesX:
        color = colors.pop()
        for small_boneX in boneX:
            cv.line(image, pixel_xy[small_boneX[0]], pixel_xy[small_boneX[1]], color, 20)


def stick_mask(measure_detect, distance, length = 480):
    color_image = np.zeros((length, length), dtype = np.uint8)
    for pixel in measure_detect:
        cv.circle(color_image, (int(pixel[0]), int(pixel[1])), distance, 255, -1)
    sticks = fn1.points_to_sticks(measure_detect)
    for finger in sticks:
        for stick in finger:
            x1, y1 = stick[0]; x2, y2 = stick[1]
            cv.line(color_image, (int(x1), int(y1)), (int(x2), int(y2)), 255, distance*2, -1)
    return color_image

def palm_mask(measure_detect, distance, length = 480):
    color_image = np.zeros((length, length), dtype = np.uint8)
    palmX = map1.palmX_list
    points_np = []
    for index in palmX:
        points_np.append(measure_detect[index])
    points_np = np.asarray(points_np).astype(np.int32)

    cv.fillPoly(color_image, [points_np], color = 255)

    length = len(palmX)
    for index in range(length):
        index1 = palmX[index % length]
        index2 = palmX[(index + 1) % length]

        x1, y1 = measure_detect[index1]
        x2, y2 = measure_detect[index2]
        cv.line(color_image, (int(x1), int(y1)), (int(x2), int(y2)), 255, distance*2, -1)

    return color_image