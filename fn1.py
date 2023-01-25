import numpy as np

def normV(vector):
    v = np.array(vector) / np.linalg.norm(vector)
    return v.tolist()
def add(point1, point2):
    len1 = len(point1); len2 = len(point2)

    if len1 == 2 and len2 == 2:
        x1, y1 = point1
        x2, y2 = point2
        return [x1 + x2, y1 + y2]

    elif len1 == 3 and len2 == 3:
        x1, y1, z1 = point1
        x2, y2, z2 = point2
        return [x1 + x2, y1 + y2, z1 + z2]

    else:
        print("Error Data Structure.")
# Distance
def d(point1, point2 = None):
    len1 = len(point1)
    if point2 is not None:
        len2 = len(point2)
        assert len2 == len1,"Two point list not matching"
    else:
        point2 = [0] * len1 
    if len1 == 2:
        x1, y1 = point1
        x2, y2 = point2
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1/2)

    elif len1 == 3:
        x1, y1, z1 = point1
        x2, y2, z2 = point2
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2) ** (1/2)

    else:
        print("Error Data Structure.")

# Perimeter of polygon or multi-points line
def points_perimeter(points, clOse = True):
    numP = len(points)
    assert numP
    length = 0
    for i in range(numP):
        ii = i+1
        if ii < numP:
            length += d(points[i], points[ii])
        elif clOse:
            length += d(points[i], points[0])
    return length

def layer_diff(layer1, layer2):
    diff = []
    for point1, point2 in zip(layer1, layer2):
        diff.append(d(point1, point2))
    return diff

def layers_diff(layers1, layers2):
    diffs = []
    for layer1, layer2 in zip(layers1, layers2):
        diffs.append(layer_diff(layer1, layer2))
    return diffs

def mean(points):
    num = len(points)
    assert num
    x, y = 0, 0
    for x_, y_ in points:
        x += x_; y += y_
    return [x / num, y / num]

def layer_mean(layer1, layer2):
    means = []
    for point1, point2 in zip(layer1, layer2):
        means.append(mean([point1, point2]))
    return means

def layers_mean(layers1, layers2):
    fingers_mean = []
    for layer1, layer2 in zip(layers1, layers2):
        fingers_mean.append(layer_mean(layer1, layer2))
    return fingers_mean




# Process of correcting MediaPipe landmarks XY
# 640/480 = 4*160 / 3*160  =>  X = x*4; Y = y*3
def pro43(point):
    x = point[0]; y = point[1]
    return [x*4, y*3]
def pro_k(point, kx = 4, ky = 3):
    x = point[0]; y = point[1]
    return [kx*x, ky*y]
def pro_int(point, kx = 640, ky = 480):
    
    x = point[0]; y = point[1]
    return [int(kx*x), int(ky*y)]
def layer_pro43(layer):
    return [pro43(point) for point in layer]
def layer_pro(layer, kx, ky):
    return [pro_k(point, kx, ky) for point in layer]
def layer_pixel(landmarks, kx, ky):
    return [pro_int(point, kx, ky) for point in landmarks]


# Used frequently
def angle_180(vector1, vector2 = None):
    if not vector2:
        vector1, vector2 = vector1
    v1 = np.array(vector1) / np.linalg.norm(vector1)
    v2 = np.array(vector2) / np.linalg.norm(vector2)
    return np.arccos(np.clip(np.dot(v1, v2), -1.0, 1.0)) / np.pi * 180

def ratio(vector1, vector2):
    return d(vector1) / d(vector2)



def AfromB(pointA, pointB):
    deltaX = pointA[0] - pointB[0]
    deltaY = pointA[1] - pointB[1]
    
    pointer = [deltaX, deltaY]
    return pointer

def ABCfromD(layerABC, pointD):
    result = []
    for point in layerABC:
        result.append(AfromB(point, pointD))
    return result

def layer2layerV(layerB, layerA):
    return [AfromB(a, b) for a, b in zip(layerA, layerB)]

def layers2layersV(layersB, layersA):
    return [layer2layerV(layerB, layerA) for layerB, layerA in zip(layersB, layersA)]


def extension_CBA(pointB, pointA, change_rate = 0.1):
    xB, yB = pointB; xA, yA = pointA

    deltaX = xB - xA; deltaY = yB - yA

    return [xB + deltaX * change_rate, yB + deltaY * change_rate]




# (x2 − x1)(y2 + y1) clockwise if sum greater than zero
def clock_wise(points):
    sortPolygon = [
        [points[map.marksX['wrist']][0], -points[map.marksX['wrist']][1]],
        [points[map.marksX['index_Finger_end']][0], -points[map.marksX['index_Finger_end']][1]],
        [points[map.marksX['little_Finger_end']][0], -points[map.marksX['little_Finger_end']][1]],]
    sum = 0; num = len(sortPolygon)
    for i in range(num):
        x2, y2 = sortPolygon[(i+1) % num]; x1, y1 = sortPolygon[i]
        sum += (x2 - x1) * (y2 + y1)
    clock_wise_or_not = sum > 0
    return clock_wise_or_not


def t_icon(self):
    wrist = self.xy[map.marksX['wrist']]
    headsMPxy = [self.xy[i] for i in map.PALM_POINTS_IDX]
    self.palm_pointers = ABCfromD(headsMPxy, wrist)
    
    virtical = d(wrist, mean(headsMPxy))
    horizontals = [d(headsMPxy[0],headsMPxy[1]), d(headsMPxy[1], headsMPxy[2]), d(headsMPxy[2], headsMPxy[3])]

    return virtical / sum(horizontals)

# A vector [x,y,None] perpendicular to another vector [x,y,z]
def perpendicular(normalV, vector):
    x1, y1, z1 = normV(normalV); x2, y2 = normV(vector)
    if abs(z1) > 1e-6:
        return [x2, y2, -( x2 * x1 + y1 * y2 ) / z1]


import map1

def points_to_sticks(measure_detect):
    thumb_head= measure_detect[map1.marksX['thumb_head']]
    thumb_head_middle = measure_detect[map1.marksX['thumb_head_middle']]
    thumb_end_middle = measure_detect[map1.marksX['thumb_end_middle']] 
    thumb_end = measure_detect[map1.marksX['thumb_end']] 

    index_Finger_head= measure_detect[map1.marksX['index_Finger_head']]
    index_Finger_head_middle = measure_detect[map1.marksX['index_Finger_head_middle']]
    index_Finger_end_middle = measure_detect[map1.marksX['index_Finger_end_middle']] 
    index_Finger_end = measure_detect[map1.marksX['index_Finger_end']] 
    
    middle_Finger_head= measure_detect[map1.marksX['middle_Finger_head']]
    middle_Finger_head_middle = measure_detect[map1.marksX['middle_Finger_head_middle']]
    middle_Finger_end_middle = measure_detect[map1.marksX['middle_Finger_end_middle']] 
    middle_Finger_end = measure_detect[map1.marksX['middle_Finger_end']] 
    
    ring_Finger_head= measure_detect[map1.marksX['ring_Finger_head']]
    ring_Finger_head_middle = measure_detect[map1.marksX['ring_Finger_head_middle']]
    ring_Finger_end_middle = measure_detect[map1.marksX['ring_Finger_end_middle']] 
    ring_Finger_end = measure_detect[map1.marksX['ring_Finger_end']] 
    
    little_Finger_head= measure_detect[map1.marksX['little_Finger_head']]
    little_Finger_head_middle = measure_detect[map1.marksX['little_Finger_head_middle']]
    little_Finger_end_middle = measure_detect[map1.marksX['little_Finger_end_middle']] 
    little_Finger_end = measure_detect[map1.marksX['little_Finger_end']] 
    
    return (
        ((thumb_head, thumb_head_middle), (thumb_head_middle, thumb_end_middle), (thumb_end_middle, thumb_end)),
        ((index_Finger_head, index_Finger_head_middle), (index_Finger_head_middle, index_Finger_end_middle), (index_Finger_end_middle, index_Finger_end)),
        ((middle_Finger_head, middle_Finger_head_middle), (middle_Finger_head_middle, middle_Finger_end_middle), (middle_Finger_end_middle, middle_Finger_end)),
        ((ring_Finger_head, ring_Finger_head_middle), (ring_Finger_head_middle, ring_Finger_end_middle), (ring_Finger_end_middle, ring_Finger_end)),
        ((little_Finger_head, little_Finger_head_middle), (little_Finger_head_middle, little_Finger_end_middle), (little_Finger_end_middle, little_Finger_end)),
    ) 
