from map1 import marksX
from map1 import fingersX_a
from fn1 import d
from draw_index import local


layer_index1 = [marksX['thumb_head'], marksX['index_Finger_head'], marksX['middle_Finger_head'], marksX['ring_Finger_head'], marksX['little_Finger_head'],]
layer_index2 = [marksX['thumb_head_middle'], marksX['index_Finger_head_middle'], marksX['middle_Finger_head_middle'], marksX['ring_Finger_head_middle'], marksX['little_Finger_head_middle'],]
layer_index3 = [marksX['thumb_end_middle'], marksX['index_Finger_end_middle'], marksX['middle_Finger_end_middle'], marksX['ring_Finger_end_middle'], marksX['little_Finger_end_middle'],]
layer_index4 = [marksX['thumb_end'], marksX['index_Finger_end'], marksX['middle_Finger_end'], marksX['ring_Finger_end'], marksX['little_Finger_end'],]

two_neighbor_layers_index = list(zip(layer_index1, layer_index2)) + list(zip(layer_index2, layer_index3)) + list(zip(layer_index3, layer_index4))


def layers(measure_detect):
    layer1 = []
    layer2 = []
    layer3 = []
    layer4 = []
    for i in range(5):
        layer1.append(measure_detect[ layer_index1[i] ])
        layer2.append(measure_detect[ layer_index2[i] ])
        layer3.append(measure_detect[ layer_index3[i] ])
        layer4.append(measure_detect[ layer_index4[i] ]) 
    return layer1, layer2, layer3, layer4       

def fingers_a(measure_detect):
    thumb =          []
    index_finger  =  []
    middle_finger =  []
    ring_finger   =  []
    little_finger =  []

    for i in range(4):
        thumb.append(          measure_detect[ fingersX_a['thumb'][i] ])
        index_finger.append(   measure_detect[ fingersX_a['index'][i] ])
        middle_finger.append(  measure_detect[ fingersX_a['middle'][i] ])
        ring_finger.append(    measure_detect[ fingersX_a['ring'][i] ])
        little_finger.append(  measure_detect[ fingersX_a['little'][i] ])
    
    return thumb, index_finger, middle_finger, ring_finger, little_finger
