# Fn2: Create Fittable Windows to Show Images

import numpy as np
import cv2 as cv

import u8

# make a square shaped image
def slip(frame, heightvswidth = 1):
    h, w = frame.shape[:2]
    ratio = h / w
    if ratio > heightvswidth:
        center_h = int(h // 2)
        delta_h = int((w * heightvswidth) // 2)
        frame = frame[center_h-delta_h:center_h+delta_h]
    if ratio < heightvswidth:
        center_w = int(w // 2)
        delta_w = int((h / heightvswidth) // 2)
        frame = frame[:, center_w-delta_w:center_w+delta_w]
    return frame





def webcam_testing(arg_index):
    camera = cv.VideoCapture(arg_index)
    setup = False
    if camera.isOpened():
        setup_result, frame = camera.read()
        camera.release()
        if setup_result:
            setup = True
    
    if setup:
        return True
    else:
        print('Webcam activation failed.\n', str(arg_index))
        return False





# Size of screen & camera
from screeninfo import get_monitors
m = get_monitors()
m = m[0]

max_width, max_height = m.width, m.height
max_width1  = max_width - 10; max_height2 = max_height - 10

# How Many Windows You Want
def max_square_windows(height, width):
    # How setup windows size
    w = max_width / width
    h = max_height / height

    w = int(w // 10)
    h = int(h // 10)

    max_XY = min( w *10 , h *10)

    print('Max size of each window: ', max_XY)
    return max_XY


def fit(image, height, width):
    out_shape = image.shape
    if out_shape[0] > height or out_shape[1] > width:
        h_ratio = height / out_shape[0]
        w_ratio = width / out_shape[1]
        hw_ratio = min(h_ratio, w_ratio)
        shape_out = (int(out_shape[1] * hw_ratio), int(out_shape[0] * hw_ratio))
        image = cv.resize(image, shape_out)

    h_diff = height - image.shape[0]
    w_diff = width - image.shape[1]

    padded = None
    if len(out_shape) == 3:
        padded = np.pad(image, [(int(h_diff / 2), int(h_diff / 2)), (int(w_diff / 2), int(w_diff / 2)), (0, 0)], mode='constant', constant_values=0)
    elif len(out_shape) == 2:
        padded = np.pad(image, [(int(h_diff / 2), int(h_diff / 2)), (int(w_diff / 2), int(w_diff / 2))], mode='constant', constant_values=0)
    return padded


# return a camera with resolution of 960 * 720
def cam720(index):
    ret = webcam_testing(index)
    if ret:
        cap = cv.VideoCapture(index)

        cap.set(cv.CAP_PROP_FRAME_WIDTH, 960)
        cap.set(cv.CAP_PROP_FRAME_HEIGHT, 720)
        return cap


def crop(frame, pixel_xy, distance):
    distance = distance * 3
    shapes = frame.shape
    height, width = shapes[0], shapes[1]
    pixel_x = []; pixel_y = []
    for pixel in pixel_xy:
        pixel_x.append(pixel[0])
        pixel_y.append(pixel[1])
    min_x = min(pixel_x); min_y = min(pixel_y)
    max_x = max(pixel_x); max_y = max(pixel_y)

    min_x = max(min_x-distance, 0); min_y = max(min_y-distance, 0)
    max_x = min(max_x+distance, width); max_y = min(max_y+distance, height)

    min_x = int(min_x); min_y = int(min_y); max_x = int(max_x); max_y = int(max_y)

    frame_crop = frame[min_x:max_x, min_y:max_y]
    return frame_crop


# Create a 2d "Hand DashBoard"
# Mask Is The Best Way !
def a_3d2d_Finger_arrayMask_Generator(index, image_height_width):
    # 1 Mask of finger
    l = image_height_width[0] // 2

    if index != 0:
        # If not thumb
        # y : 1/8 of image -> 7/8 of image
        d = l // 2
        y0 = d // 2
        y1 = y0 + d
        y2 = y0 + d + d
        y3 = y0 + d + d + d
    else:
        # If is thumb
        # y : 1/2 of image -> 7/8 of image
        d = l // 4
        y0 = l
        y1 = y0 + d
        y2 = y0 + d + d
        y3 = y0 + d + d + d        

    # x
    w1 = int(image_height_width[1] / 8 / 2)
    w2 = int(image_height_width[1] / 7 / 2)
    w3 = int(image_height_width[1] / 6 / 2)
    x = int(image_height_width[1]*(index*2+2) / 12)
    mask = np.zeros(image_height_width, dtype=np.uint8)
    mask[y0:y1, x-w1:x+w1] = 255
    mask[y1:y2, x-w2:x+w2] = 255
    mask[y2:y3, x-w3:x+w3] = 255

    # 1.1 drawing location
    points = [[x, y0], [x, y1], [x, y2], [x, y3]]
    return points, mask
def apply_mask(index, image_height_width, color_image, mask):
    # 2 logical not
    mask_inv = cv.bitwise_not(mask)
    color_image = cv.bitwise_and(color_image, color_image, mask_inv)

    # 3 full a background with single color
    colors = [u8.red, u8.green, u8.blue, u8.yellow, u8.purple]
    finger_color = colors[index]
    background = np.full(
        (image_height_width[0], 
        image_height_width[1], 
        3), 
        
        finger_color, 
        dtype = np.uint8)
    # 4 mask background with mask
    image1 = cv.bitwise_and(background, background, mask = mask)
    # 5 add "original image" with "color finger image"
    color_image = cv.add(color_image, image1)

    return color_image


# Generate Demo Hand
def demo_hand(length = 480):
    color_image = np.zeros((length, length, 3), dtype = np.uint8)
    demo_pointsS = []
    for i in range(5):
        demo_points, demo_mask = a_3d2d_Finger_arrayMask_Generator(i, (length, length))
        color_image = apply_mask(i, (length, length), color_image, demo_mask)
        demo_pointsS.append(demo_points)
    for demo_points in demo_pointsS:
        for demo_point in demo_points:
            demo_point[0] -= length // 24
    return color_image, demo_pointsS
