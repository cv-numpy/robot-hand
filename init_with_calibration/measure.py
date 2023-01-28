
# To check if the point from indexing is at "U turn" position
def monotonic(t_ratios, index, number = 10):
    length = len(t_ratios)
    if index + number > length or index - number < 0:
        return False

    monotonical = []
    for i in range(number):
        if t_ratios[index+i] > t_ratios[index+i+1] == t_ratios[index+i+1] > t_ratios[index+i+2] \
            and t_ratios[index-i] > t_ratios[index-i-1] == t_ratios[index-i-1] > t_ratios[index-i-2]:
            monotonical.append(True)
        else:
            monotonical.append(False)
    return monotonical

def swing(t_ratios, direction):
    # slice part from t_ratios with length of 20
    part_length = 20
    if len(t_ratios) <= part_length:
        return False
    else:
        num = len(t_ratios) - part_length

        if direction == 'left_and_right':
            mins_result = []
            for i in range(num):
                t_ratios_part = t_ratios[i:i+part_length]

                # get partial minimal value
                t_ratios_part_min = min(t_ratios_part)

                min_index = t_ratios_part.index(t_ratios_part_min) + i

                # make sure it will not out of boundary in fn monotonic
                if min_index > (10+4) and len(t_ratios) - min_index > (10+4):
                    monotonicals = [monotonic(t_ratios, min_index)]
                    for i in range(4):
                        monotonicals.append(monotonic(t_ratios, min_index+i))
                        monotonicals.append(monotonic(t_ratios, min_index-i))
                    
                    # if it is extreme value
                    mins_counts = [sum(bool(x) for x in lst) for lst in monotonicals if type(lst) == list]

                    if mins_counts != []:
                        if mins_counts[0] == max(mins_counts):
                            mins_result.append(t_ratios[min_index])
            return mins_result


        elif direction == 'upside_down':
            maxs_result = []
            for i in range(num):
                t_ratios_part = t_ratios[i:i+part_length]

                # get partial maximal value
                t_ratios_part_max = max(t_ratios_part)

                max_index = t_ratios_part.index(t_ratios_part_max) + i

                # make sure it will not out of boundary in fn monotonic
                if max_index > (10+4) and len(t_ratios) - max_index > (10+4):
                    monotonicals = [monotonic(t_ratios, max_index)]
                    for i in range(4):
                        monotonicals.append(monotonic(t_ratios, max_index+i))
                        monotonicals.append(monotonic(t_ratios, max_index-i))

                    # if it is extreme value
                    maxs_counts = [sum(bool(x) for x in lst) for lst in monotonicals if type(lst) == list]

                    if maxs_counts != []:
                        if maxs_counts[0] == max(maxs_counts):
                            maxs_result.append(t_ratios[max_index])
            return maxs_result

        else:
            print('direction should be "left_and_right" or "upside_down".')
            return False
