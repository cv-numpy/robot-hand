'''
Index of Landmarks
'''

# Landmarks Orders #
marksX = dict()
marks = []

marksX['wrist'] = 0
marksX['index_Finger_head'] = 8
marksX['index_Finger_head_middle'] = 7
marksX['index_Finger_end_middle'] = 6
marksX['index_Finger_end'] = 5
marksX['middle_Finger_head'] = 12
marksX['middle_Finger_head_middle'] = 11
marksX['middle_Finger_end_middle'] = 10
marksX['middle_Finger_end'] = 9
marksX['ring_Finger_head'] = 16
marksX['ring_Finger_head_middle'] = 15
marksX['ring_Finger_end_middle'] = 14
marksX['ring_Finger_end'] = 13
marksX['little_Finger_head'] = 20
marksX['little_Finger_head_middle'] = 19
marksX['little_Finger_end_middle'] = 18
marksX['little_Finger_end'] = 17
marksX['thumb_head'] = 4
marksX['thumb_head_middle'] = 3
marksX['thumb_end_middle'] = 2
marksX['thumb_end'] = 1

marksX['0'] = 'wrist'
marksX['8'] = 'index_Finger_head'
marksX['7'] = 'index_Finger_head_middle'
marksX['6'] = 'index_Finger_end_middle'
marksX['5'] = 'index_Finger_end'
marksX['12'] = 'middle_Finger_head'
marksX['11'] = 'middle_Finger_head_middle'
marksX['10'] = 'middle_Finger_end_middle'
marksX['9'] = 'middle_Finger_end'
marksX['16'] = 'ring_Finger_head'
marksX['15'] = 'ring_Finger_head_middle'
marksX['14'] = 'ring_Finger_end_middle'
marksX['13'] = 'ring_Finger_end'
marksX['20'] = 'little_Finger_head'
marksX['19'] = 'little_Finger_head_middle'
marksX['18'] = 'little_Finger_end_middle'
marksX['17'] = 'little_Finger_end'
marksX['4'] = 'Thumb_head'
marksX['3'] = 'Thumb_head_middle'
marksX['2'] = 'Thumb_end_middle'
marksX['1'] = 'Thumb_end'

# Fingers #
# default direction: use the direction that 
# from tip of finger point to the center of palm
default_direction = True

if default_direction:
    fingersX_a = dict()
    # oder A
    fingersX_a['thumb'] = [4, 3, 2, 1]
    fingersX_a['index'] = [8, 7, 6, 5]
    fingersX_a['middle'] = [12, 11, 10, 9]
    fingersX_a['ring'] = [16, 15, 14, 13]
    fingersX_a['little'] = [20, 19, 18, 17]

    fingersX_b = dict()
    # order B
    fingersX_b['thumb'] = [4, 3, 2]
    fingersX_b['index'] = [8, 7, 6]
    fingersX_b['middle'] = [12, 11, 10]
    fingersX_b['ring'] = [16, 15, 14]
    fingersX_b['little'] = [20, 19, 18]

    fingersX_c = dict()
    # order C
    fingersX_c['thumb'] = [3, 2, 1]
    fingersX_c['index'] = [7, 6, 5]
    fingersX_c['middle'] = [11, 10, 9]
    fingersX_c['ring'] = [15, 14, 13]
    fingersX_c['little'] = [19, 18, 17]

else:
    fingersX_g = dict()
    # order G
    fingersX_g['thumb'] = [1, 2, 3, 4]
    fingersX_g['index'] = [5, 6, 7, 8]
    fingersX_g['middle'] = [9, 10, 11, 12]
    fingersX_g['ring'] = [13, 14, 15, 16]
    fingersX_g['little'] = [17, 18, 19, 20]
    
    fingersX_h = dict()
    # order H
    fingersX_h['thumb'] = [1, 2, 3]
    fingersX_h['index'] = [5, 6, 7]
    fingersX_h['middle'] = [9, 10, 11]
    fingersX_h['ring'] = [13, 14, 15]
    fingersX_h['little'] = [17, 18, 19]
    
    fingersX_i = dict()
    # order i
    fingersX_i['thumb'] = [2, 3, 4]
    fingersX_i['index'] = [6, 7, 8]
    fingersX_i['middle'] = [10, 11, 12]
    fingersX_i['ring'] = [14, 15, 16]
    fingersX_i['little'] = [18, 19, 20]


# palm points index
palmX_list = [0, 1, 5, 9, 13, 17]
