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
fingersX = dict()
# oder A
fingersX['finger1_a'] = [4, 3, 2, 1]
fingersX['finger2_a'] = [8, 7, 6, 5]
fingersX['finger3_a'] = [12, 11, 10, 9]
fingersX['finger4_a'] = [16, 15, 14, 13]
fingersX['finger5_a'] = [20, 19, 18, 17]
# order B
fingersX['finger1_b'] = [1, 2, 3, 4]
fingersX['finger2_b'] = [5, 6, 7, 8]
fingersX['finger3_b'] = [9, 10, 11, 12]
fingersX['finger4_b'] = [13, 14, 15, 16]
fingersX['finger5_b'] = [17, 18, 19, 20]
# order C
fingersX['finger1_c'] = [4, 3, 2]
fingersX['finger2_c'] = [8, 7, 6]
fingersX['finger3_c'] = [12, 11, 10]
fingersX['finger4_c'] = [16, 15, 14]
fingersX['finger5_c'] = [20, 19, 18]
# order D
fingersX['finger1_d'] = [2, 3, 4]
fingersX['finger2_d'] = [6, 7, 8]
fingersX['finger3_d'] = [10, 11, 12]
fingersX['finger4_d'] = [14, 15, 16]
fingersX['finger5_d'] = [18, 19, 20]
# order E
fingersX['finger1_e'] = [3, 2, 1]
fingersX['finger2_e'] = [7, 6, 5]
fingersX['finger3_e'] = [11, 10, 9]
fingersX['finger4_e'] = [15, 14, 13]
fingersX['finger5_e'] = [19, 18, 17]

fingers_order1 = [fingersX['finger1_b'], fingersX['finger2_b'], fingersX['finger3_b'], fingersX['finger4_b'], fingersX['finger5_b']]
fingers_order2 = [fingersX['finger5_b'], fingersX['finger4_b'], fingersX['finger3_b'], fingersX['finger2_b'], fingersX['finger1_b']]

fingers = ['index_Finger', 'middle_Finger', 'ring_Finger', 'little_Finger', 'Thumb']


# palm points index
palmX_list = [0, 1, 5, 9, 13, 17]
