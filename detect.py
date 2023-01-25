# Using MediaPipe Hand Detection
from mediapipe import solutions

mp_hands = solutions.hands
mp_solution = mp_hands.Hands(
        model_complexity = 0, 
        min_detection_confidence = 0.5, 
        min_tracking_confidence = 0.5
        )

# 1
def it(frame): 
    result = mp_solution.process(frame)
    subjects = result.multi_handedness
    # if "human hand" detected
    if subjects is not None:
        number = len(subjects)
        id = []
        for i in range(number):
            id.append(subjects[i].classification[0].label)
        return number, id, result.multi_hand_landmarks
    else:
        return 0, None, None

# 2
def label_xy(label):
    measure_detect = []
    # keypoints number amount is 21
    for i in range(21):
        measure_detect.append([label.landmark[i].x, label.landmark[i].y])
    return measure_detect
# 3
def points(number, labels):

    if number == 1:
        return label_xy(labels[0])

    if number > 1:
        measure_detect = []
        for i in range(number):
            measure_detect.append(label_xy(labels[i]))
    
        return measure_detect
