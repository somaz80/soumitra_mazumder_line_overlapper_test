# get the maximum of (x1 and x2) and get min of (x3 and x4)
# compare which one is grater or equal and if condition
# satisfies then return true else return false.


def are_line_segments_overlapping(line1, line2):
    # using >= to compare considering that lines might start from same point.
    # If this condition is not needed please remove it before running
    x1 = line1[0]
    x2 = line1[1]
    x3 = line2[0]
    x4 = line2[1]

    # if the line 2 exists on the left of line 1
    if max(x3, x4) > max(x1, x2):
        if max(x1, x2) >= min(x3, x4):
            return True
        return False
    else:
        # if the line 1 exists on the left of line 2
        if max(x3, x4) >= min(x1, x2):
            return True
        return False

# main method for standalone run
def main():
    print(are_line_segments_overlapping([2, 6], [5, 8]))


if __name__ == '__main__':
    main()
