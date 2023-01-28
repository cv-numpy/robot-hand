import fn1
from map1 import marksX

# three points that could made the biggest trangle inside the palm pionts
def three_points(measure_detect):
    wrist = measure_detect[marksX['wrist']]                         # 0
    index_Finger_end = measure_detect[marksX['index_Finger_end']]   #5
    little_Finger_end = measure_detect[marksX['little_Finger_end']] #17
    return wrist, index_Finger_end, little_Finger_end

# all palm points
def five_points(measure_detect):
    wrist   = measure_detect[marksX['wrist']] # 0
    palm_p2 = measure_detect[marksX['index_Finger_end']]    # 5
    palm_p3 = measure_detect[marksX['middle_Finger_end']]   # 9
    palm_p4 = measure_detect[marksX['ring_Finger_end']]     # 13
    palm_p5 = measure_detect[marksX['little_Finger_end']]   # 17
    return wrist, palm_p2, palm_p3, palm_p4, palm_p5    


def points_distance(measure_detect):
    middle_Finger_head = measure_detect[marksX['middle_Finger_head']]
    middle_Finger_head_middle = measure_detect[marksX['middle_Finger_head_middle']]
    middle_Finger_end_middle = measure_detect[marksX['middle_Finger_end_middle']]
    middle_Finger_end = measure_detect[marksX['middle_Finger_end']]

    wrist, index_Finger_end, little_Finger_end = three_points(measure_detect)

    distance = max(
        fn1.d(middle_Finger_head, middle_Finger_head_middle), 
        fn1.d(middle_Finger_head_middle, middle_Finger_end_middle), 
        fn1.d(middle_Finger_end_middle, middle_Finger_end), 
        
        fn1.d(wrist, index_Finger_end), 
        fn1.d(index_Finger_end, little_Finger_end), 
        fn1.d(little_Finger_end, wrist))
    
    return int(distance/10)

def t_icon(measure_detect):
    wrist, palm_p2, palm_p3, palm_p4, palm_p5 = five_points(measure_detect)

    horizontals_lengths = sum([fn1.d(palm_p2, palm_p3), fn1.d(palm_p3, palm_p4), fn1.d(palm_p4, palm_p5)])
    
    virtical_length = fn1.d(wrist, fn1.mean([palm_p2, palm_p3, palm_p4, palm_p5]))

    return horizontals_lengths, virtical_length

def get_area(measure_detect):
    wrist, index_Finger_end, little_Finger_end = three_points(measure_detect)

    x = [wrist[0], index_Finger_end[0], little_Finger_end[0]]
    y = [wrist[1], index_Finger_end[1], little_Finger_end[1]]

    area=0.5*( (x[0]*(y[1]-y[2])) + (x[1]*(y[2]-y[0])) + (x[2]*(y[0]-y[1])) )
    area=0.5*( (x[0]*(y[1]-y[2])) + (x[1]*(y[2]-y[0])) + (x[2]*(y[0]-y[1])) )

    return int(area)

# (x2 − x1)(y2 + y1) clockwise if sum greater than zero
def clock_wise_check(measure_detect):
    palm_p2 = measure_detect[marksX['index_Finger_end']]    # 5
    palm_p5 = measure_detect[marksX['little_Finger_end']]   # 17
    wrist   = measure_detect[marksX['wrist']] # 0

    sortPolygon = [
        [  wrist[0],   -wrist[1]],
        [palm_p2[0], -palm_p2[1]],
        [palm_p5[0], -palm_p5[1]],
    ]

    sum = 0; num = len(sortPolygon)
    for i in range(num):
        x2, y2 = sortPolygon[(i+1) % num]; x1, y1 = sortPolygon[i]
        sum += (x2 - x1) * (y2 + y1)

    return sum > 0

def pointing(measure_detect):
    wrist, palm_p2, palm_p3, palm_p4, palm_p5 = five_points(measure_detect)

    middle_point = fn1.mean([palm_p2, palm_p5, wrist])

    vector = fn1.AfromB(palm_p4, wrist)

    return middle_point, vector

def update_palm(measure_detect):
    clock_wise = clock_wise_check(measure_detect)
    deepth_distance = points_distance(measure_detect)
    horizontals_lengths, virtical_length = t_icon(measure_detect)
    middle_point, vector = pointing(measure_detect)
    palm_trangle_area = get_area(measure_detect)

    return clock_wise, deepth_distance, horizontals_lengths, virtical_length, middle_point, vector, palm_trangle_area
