# colors

black  =         (0, 0, 0)
dark  =          (0, 0, 0)
gray  =          (125, 125, 125)
white  =         (255, 255, 255)
bright  =        (255, 255, 255)

blue  =          (255, 0, 0)
green  =         (0, 255, 0)
red  =           (0, 0, 255)
cyan  =          (255, 255, 0)
yellow  =        (0, 255, 255)
purple  =        (255, 0, 255)

purple_ubuntu = (111, 33, 119)
gold =          (0, 215, 255)
brown =         (42 ,42, 165)
colors = [(0, 125, 255), (0, 255, 125), (125, 0, 255), (125, 255, 0), (255, 0, 125), (255, 125, 0)]


# for example: input color = "b255g125r5" 
# then: blue = 255; green = 125; red = 5
def bgr_string(color): # from string to a tuple of color
    b = 0; g = 0; r = 0

    index_of_b = color.find('b')
    index_of_g = color.find('g')
    index_of_r = color.find('r')

    index_of_bgr = [index_of_b, index_of_g, index_of_r]
    index_of_bgr.sort()
    index_of_bgr = [i for i in index_of_bgr if i >= 0]

    num = len(index_of_bgr)
    assert num > 0,"bgr not found."
    # we slice number substring between two indexes.
    index_of_bgr.append(len(color) + 1) 
    # so we add a index for the last one which didnt between two other indexes.

    for i in range(num): # num : 1 2 or 3

        # get sub_string between two 'b''g' or 'r' string
        value = int(color[(index_of_bgr[i]+1): (index_of_bgr[i+1])])

        if value >= 0 and value <= 255:
            channel = color[index_of_bgr[i]]
            if channel == 'b':
                b = value
            elif channel == 'g':
                g = value
            elif channel == 'r':
                r = value
        
    if b != 0 or g != 0 or r!= 0:
        return (b, g, r)
    else:
        # gray = (125, 125, 125)
        # if not matched to any color
        return (125, 125, 125)
