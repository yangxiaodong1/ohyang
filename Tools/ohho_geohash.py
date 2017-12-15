import pygeohash

#  http://blog.csdn.net/u014520745/article/details/52619796

ODD_LIST = [list("bcfguvyz"), list("89destwx"), list("2367kmqr"), list("0145hjnp")]
EVEN_LIST = [list("prxz"), list("nqwy"), list("jmtv"), list("hksu"),
             list("57eg"), list("46df"), list("139c"), list("028b")]

CENTER = 0
TOP = 1  # 0001
RIGHT = 2  # 0010
BOTTOM = 4  # 0100
LEFT = 8  # 1000
LEFT_TOP = 9  # 1001
RIGHT_TOP = 3  # 0011
RIGHT_BOTTOM = 6  # 0110
LEFT_BOTTOM = 12  # 1100
EXCEPTION = 15  # 1111


class OHHOGeohash(object):
    @staticmethod
    def get(latitude, longitude, precision=12):
        return pygeohash.encode(latitude, longitude, precision)

    @staticmethod
    def get_max(is_odd):
        if is_odd:
            row_max = 4
            column_max = 8
        else:
            row_max = 8
            column_max = 4
        return row_max, column_max

    @staticmethod
    def get_the_list(is_odd):
        if is_odd:
            return ODD_LIST
        else:
            return EVEN_LIST

    @staticmethod
    def get_list_and_max(is_odd):
        the_list = OHHOGeohash.get_the_list(is_odd)
        row_max, column_max = OHHOGeohash.get_max(is_odd)
        return the_list, row_max, column_max

    @staticmethod
    def get_index(letter, is_odd):
        result_row = -1
        result_column = -1
        the_list, row_max, column_max = OHHOGeohash.get_list_and_max(is_odd)

        for row in range(row_max):
            if letter in the_list[row]:
                result_row = row
                for column in range(column_max):
                    if letter == the_list[row][column]:
                        result_column = column
                        break
                if result_column >= 0:
                    break
        return result_row, result_column

    @staticmethod
    def get_letter(row, column, is_odd):
        the_list = OHHOGeohash.get_the_list(is_odd)
        return the_list[row][column]

    @staticmethod
    def get_border_overflow(row, column, is_odd):
        row_max, column_max = OHHOGeohash.get_max(is_odd)
        top = (row == 0)
        bottom = (row == row_max - 1)
        left = (column == 0)
        right = (column == column_max - 1)
        data = top + bottom + left + right
        if data == 1:
            if top:
                return TOP
            if bottom:
                return BOTTOM
            if left:
                return LEFT
            if right:
                return RIGHT
        elif data == 2:
            if left and top:
                return LEFT_TOP
            elif left and bottom:
                return LEFT_BOTTOM
            elif right and top:
                return RIGHT_TOP
            elif right and bottom:
                return RIGHT_BOTTOM
            else:
                return EXCEPTION
        return CENTER

    @staticmethod
    def sum_dict(border_dict):
        total = 0
        for key, value in border_dict.items():
            total += value
        return total

    @staticmethod
    def is_top_overflow(the_overflow):
        return the_overflow in (TOP, LEFT_TOP, RIGHT_TOP)

    @staticmethod
    def is_bottom_overflow(the_overflow):
        return the_overflow == (LEFT_BOTTOM, BOTTOM, RIGHT_BOTTOM)

    @staticmethod
    def is_left_overflow(the_overflow):
        return the_overflow == (LEFT_BOTTOM, LEFT, LEFT_TOP)

    @staticmethod
    def is_right_overflow(the_overflow):
        return the_overflow in (RIGHT_BOTTOM, RIGHT, RIGHT_TOP)

    @staticmethod
    def is_left_top_overflow(the_overflow):
        return the_overflow == LEFT_TOP

    @staticmethod
    def is_right_top_overflow(the_overflow):
        return the_overflow == RIGHT_TOP

    @staticmethod
    def is_left_bottom_overflow(the_overflow):
        return the_overflow == LEFT_BOTTOM

    @staticmethod
    def is_right_bottom_overflow(the_overflow):
        return the_overflow == RIGHT_BOTTOM

    @staticmethod
    def is_overflow(the_overflow):
        return the_overflow > 0

    @staticmethod
    def is_the_overflow(the_previous_overflow, current_overflow):
        return the_previous_overflow == current_overflow

    @staticmethod
    def get_top(row, column, is_odd):
        row_max, column_max = OHHOGeohash.get_max(is_odd)
        return (row - 1 + row_max) % row_max, column

    @staticmethod
    def get_top_letter(letter, is_odd):
        row, column = OHHOGeohash.get_index(letter, is_odd)
        the_row, the_column = OHHOGeohash.get_top(row, column, is_odd)
        return OHHOGeohash.get_letter(the_row, the_column, is_odd)

    @staticmethod
    def get_bottom(row, column, is_odd):
        row_max, column_max = OHHOGeohash.get_max(is_odd)
        return (row + 1) % row_max, column

    @staticmethod
    def get_bottom_letter(letter, is_odd):
        row, column = OHHOGeohash.get_index(letter, is_odd)
        the_row, the_column = OHHOGeohash.get_bottom(row, column, is_odd)
        return OHHOGeohash.get_letter(the_row, the_column, is_odd)

    @staticmethod
    def get_left(row, column, is_odd):
        row_max, column_max = OHHOGeohash.get_max(is_odd)
        return row, (column - 1 + column_max) % column_max

    @staticmethod
    def get_left_letter(letter, is_odd):
        row, column = OHHOGeohash.get_index(letter, is_odd)
        the_row, the_column = OHHOGeohash.get_left(row, column, is_odd)
        return OHHOGeohash.get_letter(the_row, the_column, is_odd)

    @staticmethod
    def get_right(row, column, is_odd):
        row_max, column_max = OHHOGeohash.get_max(is_odd)
        return row, (column + 1) % column_max

    @staticmethod
    def get_right_letter(letter, is_odd):
        row, column = OHHOGeohash.get_index(letter, is_odd)
        the_row, the_column = OHHOGeohash.get_right(row, column, is_odd)
        return OHHOGeohash.get_letter(the_row, the_column, is_odd)

    @staticmethod
    def get_left_top(row, column, is_odd):
        row_max, column_max = OHHOGeohash.get_max(is_odd)
        return (row - 1 + row_max) % row_max, (column - 1 + column_max) % column_max

    @staticmethod
    def get_left_top_letter(letter, is_odd):
        row, column = OHHOGeohash.get_index(letter, is_odd)
        the_row, the_column = OHHOGeohash.get_left_top(row, column, is_odd)
        return OHHOGeohash.get_letter(the_row, the_column, is_odd)

    @staticmethod
    def get_right_top(row, column, is_odd):
        row_max, column_max = OHHOGeohash.get_max(is_odd)
        return (row - 1 + row_max) % row_max, (column + 1) % column_max

    @staticmethod
    def get_right_top_letter(letter, is_odd):
        row, column = OHHOGeohash.get_index(letter, is_odd)
        the_row, the_column = OHHOGeohash.get_right_top(row, column, is_odd)
        return OHHOGeohash.get_letter(the_row, the_column, is_odd)

    @staticmethod
    def get_left_bottom(row, column, is_odd):
        row_max, column_max = OHHOGeohash.get_max(is_odd)
        return (row + 1) % row_max, (column - 1 + column_max) % column_max

    @staticmethod
    def get_left_bottom_letter(letter, is_odd):
        row, column = OHHOGeohash.get_index(letter, is_odd)
        the_row, the_column = OHHOGeohash.get_left_bottom(row, column, is_odd)
        return OHHOGeohash.get_letter(the_row, the_column, is_odd)

    @staticmethod
    def get_right_bottom(row, column, is_odd):
        row_max, column_max = OHHOGeohash.get_max(is_odd)
        return (row + 1) % row_max, (column + 1) % column_max

    @staticmethod
    def get_right_bottom_letter(letter, is_odd):
        row, column = OHHOGeohash.get_index(letter, is_odd)
        the_row, the_column = OHHOGeohash.get_right_bottom(row, column, is_odd)
        return OHHOGeohash.get_letter(the_row, the_column, is_odd)

    @staticmethod
    def is_odd(length):
        return length % 2

    @staticmethod
    def get_top_data(data):
        result = list()
        letter, other = OHHOGeohash.get_some_letter(data, OHHOGeohash.get_top_letter)
        last_overflow = TOP
        last_second_overflow = OHHOGeohash.get_last_letter_overflow(data)
        if last_second_overflow == CENTER or not (last_second_overflow & last_overflow):
            return other + letter
        else:
            result.append(letter)
        while last_overflow & last_second_overflow:
            overflow = last_overflow & last_second_overflow
            last_overflow = overflow
            last_second_overflow = OHHOGeohash.get_last_letter_overflow(other)
            if overflow == TOP:
                letter, other = OHHOGeohash.get_some_letter(other, OHHOGeohash.get_top_letter)
            # elif overflow == RIGHT:
            #     letter, other = OHHOGeohash.get_some_letter(other, OHHOGeohash.get_right_letter)
            # else:
            #     letter, other = OHHOGeohash.get_some_letter(other, OHHOGeohash.get_right_top_letter)
            result.append(letter)
        return other + "".join(reversed(result))

    @staticmethod
    def get_right_data(data):
        result = list()
        letter, other = OHHOGeohash.get_some_letter(data, OHHOGeohash.get_right_letter)
        last_overflow = RIGHT
        last_second_overflow = OHHOGeohash.get_last_letter_overflow(data)
        if last_second_overflow == CENTER or not (last_second_overflow & last_overflow):
            return other + letter
        else:
            result.append(letter)
        while last_overflow & last_second_overflow:
            overflow = last_overflow & last_second_overflow
            last_overflow = overflow
            last_second_overflow = OHHOGeohash.get_last_letter_overflow(other)
            if overflow == RIGHT:
                letter, other = OHHOGeohash.get_some_letter(other, OHHOGeohash.get_right_letter)
            # elif overflow == RIGHT:
            #     letter, other = OHHOGeohash.get_some_letter(other, OHHOGeohash.get_right_letter)
            # else:
            #     letter, other = OHHOGeohash.get_some_letter(other, OHHOGeohash.get_right_top_letter)
            result.append(letter)
        return other + "".join(reversed(result))

    @staticmethod
    def get_left_data(data):
        result = list()
        letter, other = OHHOGeohash.get_some_letter(data, OHHOGeohash.get_left_letter)
        last_overflow = LEFT
        last_second_overflow = OHHOGeohash.get_last_letter_overflow(data)
        if last_second_overflow == CENTER or not (last_second_overflow & last_overflow):
            return other + letter
        else:
            result.append(letter)
        while last_overflow & last_second_overflow:
            overflow = last_overflow & last_second_overflow
            last_overflow = overflow
            last_second_overflow = OHHOGeohash.get_last_letter_overflow(other)
            if overflow == LEFT:
                letter, other = OHHOGeohash.get_some_letter(other, OHHOGeohash.get_left_letter)
            # elif overflow == RIGHT:
            #     letter, other = OHHOGeohash.get_some_letter(other, OHHOGeohash.get_right_letter)
            # else:
            #     letter, other = OHHOGeohash.get_some_letter(other, OHHOGeohash.get_right_top_letter)
            result.append(letter)
        return other + "".join(reversed(result))

    @staticmethod
    def get_bottom_data(data):
        result = list()
        letter, other = OHHOGeohash.get_some_letter(data, OHHOGeohash.get_bottom_letter)
        last_overflow = BOTTOM
        last_second_overflow = OHHOGeohash.get_last_letter_overflow(data)
        if last_second_overflow == CENTER or not (last_second_overflow & last_overflow):
            return other + letter
        else:
            result.append(letter)
        while last_overflow & last_second_overflow:
            overflow = last_overflow & last_second_overflow
            last_overflow = overflow
            last_second_overflow = OHHOGeohash.get_last_letter_overflow(other)
            if overflow == BOTTOM:
                letter, other = OHHOGeohash.get_some_letter(other, OHHOGeohash.get_bottom_letter)
            # elif overflow == RIGHT:
            #     letter, other = OHHOGeohash.get_some_letter(other, OHHOGeohash.get_right_letter)
            # else:
            #     letter, other = OHHOGeohash.get_some_letter(other, OHHOGeohash.get_right_top_letter)
            result.append(letter)
        return other + "".join(reversed(result))

    @staticmethod
    def get_some_letter(data, get_letter_function):
        length = len(data)
        is_odd = OHHOGeohash.is_odd(length)
        letter = data[-1]
        other = data[:-1]
        the_letter = get_letter_function(letter, is_odd)
        return the_letter, other

    @staticmethod
    def get_last_letter_overflow(data):
        length = len(data)
        is_odd = OHHOGeohash.is_odd(length)
        letter = data[-1]
        row, column = OHHOGeohash.get_index(letter, is_odd)

        the_overflow = OHHOGeohash.get_border_overflow(row, column, is_odd)
        return the_overflow

    @staticmethod
    def get_last_second_letter_overflow(data):
        data = data[:-1]
        return OHHOGeohash.get_last_letter_overflow(data)

    @staticmethod
    def get_right_top_data(data):
        result = list()
        letter, other = OHHOGeohash.get_some_letter(data, OHHOGeohash.get_right_top_letter)
        last_overflow = RIGHT_TOP
        last_second_overflow = OHHOGeohash.get_last_letter_overflow(data)
        if last_second_overflow == CENTER or not (last_second_overflow & last_overflow):
            return other + letter
        else:
            result.append(letter)
        while last_overflow & last_second_overflow:
            overflow = last_overflow & last_second_overflow
            last_overflow = overflow
            last_second_overflow = OHHOGeohash.get_last_letter_overflow(other)
            if overflow == TOP:
                letter, other = OHHOGeohash.get_some_letter(other, OHHOGeohash.get_top_letter)
            elif overflow == RIGHT:
                letter, other = OHHOGeohash.get_some_letter(other, OHHOGeohash.get_right_letter)
            else:
                letter, other = OHHOGeohash.get_some_letter(other, OHHOGeohash.get_right_top_letter)
            result.append(letter)
        return other + "".join(reversed(result))

    @staticmethod
    def get_right_bottom_data(data):
        result = list()
        letter, other = OHHOGeohash.get_some_letter(data, OHHOGeohash.get_right_bottom_letter)
        last_overflow = RIGHT_BOTTOM
        last_second_overflow = OHHOGeohash.get_last_letter_overflow(data)
        if last_second_overflow == CENTER or not (last_second_overflow & last_overflow):
            return other + letter
        else:
            result.append(letter)
        while last_overflow & last_second_overflow:
            overflow = last_overflow & last_second_overflow
            last_overflow = overflow
            last_second_overflow = OHHOGeohash.get_last_letter_overflow(other)
            if overflow == BOTTOM:
                letter, other = OHHOGeohash.get_some_letter(other, OHHOGeohash.get_bottom_letter)
            elif overflow == RIGHT:
                letter, other = OHHOGeohash.get_some_letter(other, OHHOGeohash.get_right_letter)
            else:
                letter, other = OHHOGeohash.get_some_letter(other, OHHOGeohash.get_right_bottom_letter)
            result.append(letter)
        return other + "".join(reversed(result))

    @staticmethod
    def get_left_bottom_data(data):
        result = list()
        letter, other = OHHOGeohash.get_some_letter(data, OHHOGeohash.get_left_bottom_letter)
        last_overflow = LEFT_BOTTOM
        last_second_overflow = OHHOGeohash.get_last_letter_overflow(data)
        if last_second_overflow == CENTER or not (last_second_overflow & last_overflow):
            return other + letter
        else:
            result.append(letter)
        while last_overflow & last_second_overflow:
            overflow = last_overflow & last_second_overflow
            last_overflow = overflow
            last_second_overflow = OHHOGeohash.get_last_letter_overflow(other)
            if overflow == BOTTOM:
                letter, other = OHHOGeohash.get_some_letter(other, OHHOGeohash.get_bottom_letter)
            elif overflow == LEFT:
                letter, other = OHHOGeohash.get_some_letter(other, OHHOGeohash.get_left_letter)
            else:
                letter, other = OHHOGeohash.get_some_letter(other, OHHOGeohash.get_left_bottom_letter)
            result.append(letter)
        return other + "".join(reversed(result))

    @staticmethod
    def get_left_top_data(data):
        result = list()
        letter, other = OHHOGeohash.get_some_letter(data, OHHOGeohash.get_left_top_letter)
        last_overflow = LEFT_TOP
        last_second_overflow = OHHOGeohash.get_last_letter_overflow(data)
        # print("left top")
        # print(LEFT_TOP)
        # print(data)
        # print(last_second_overflow)
        # print(last_second_overflow & last_overflow)
        if last_second_overflow == CENTER or not (last_second_overflow & last_overflow):

            return other + letter
        else:
            result.append(letter)
        while last_overflow & last_second_overflow:
            overflow = last_overflow & last_second_overflow
            last_overflow = overflow
            last_second_overflow = OHHOGeohash.get_last_letter_overflow(other)
            if overflow == TOP:
                letter, other = OHHOGeohash.get_some_letter(other, OHHOGeohash.get_top_letter)
            elif overflow == LEFT:
                letter, other = OHHOGeohash.get_some_letter(other, OHHOGeohash.get_left_letter)
            else:
                letter, other = OHHOGeohash.get_some_letter(other, OHHOGeohash.get_left_top_letter)
            result.append(letter)
        return other + "".join(reversed(result))

    @staticmethod
    def get_neighbours(data):
        result = dict()
        result["top"] = OHHOGeohash.get_top_data(data)
        result["right"] = OHHOGeohash.get_right_data(data)
        result["bottom"] = OHHOGeohash.get_bottom_data(data)
        result["left"] = OHHOGeohash.get_left_data(data)
        result["left_top"] = OHHOGeohash.get_left_top_data(data)
        result["right_top"] = OHHOGeohash.get_right_top_data(data)
        result["right_bottom"] = OHHOGeohash.get_right_bottom_data(data)
        result["left_bottom"] = OHHOGeohash.get_left_bottom_data(data)
        return result

    @staticmethod
    def get_neighbours_list(data):
        result = list()
        result.append(OHHOGeohash.get_top_data(data))
        result.append(OHHOGeohash.get_right_data(data))
        result.append(OHHOGeohash.get_bottom_data(data))
        result.append(OHHOGeohash.get_left_data(data))
        result.append(OHHOGeohash.get_left_top_data(data))
        result.append(OHHOGeohash.get_right_top_data(data))
        result.append(OHHOGeohash.get_right_bottom_data(data))
        result.append(OHHOGeohash.get_left_bottom_data(data))
        return result


if __name__ == "__main__":
    latitude = 40.0585138025
    longitude = 117.445044487
    data = OHHOGeohash.get(latitude, longitude)
    print(data)
    data = "wx5ebs2vgbhp"
    # 'wx4cp','wx4bx','wx50b','wx4by','wx4cn','wx510','wx508','wx4bw','wx4bz'
    # 'wx4bx', 'wx4by', 'wx4bw', 'wx50b'
    # z --> y,w,x,i,b,n,p,0
    data = "wx4epc"
    print(OHHOGeohash.get_neighbours(data))
    # print("wx4bz top data wx4cp")
    # top_data = OHHOGeohash.get_top_data(data)
    # print(top_data)
    # print("wx4bz right data wx50b")
    # right_data = OHHOGeohash.get_right_data(data)
    # print(right_data)
    # print("wx4bz left data wx4by")
    # left_data = OHHOGeohash.get_left_data(data)
    # print(left_data)
    # print("wx4bz bottom data wx4bx")
    # bottom_data = OHHOGeohash.get_bottom_data(data)
    # print(bottom_data)

    # print("wx4bz right top data wx510")
    # right_top_data = OHHOGeohash.get_right_top_data(data)
    # print(right_top_data)

    # print("wx4bz right bottom data wx508")
    # right_bottom_data = OHHOGeohash.get_right_bottom_data(data)
    # print(right_bottom_data)

    # print("wx4bz left bottom data wx4cn")
    # left_top_data = OHHOGeohash.get_left_top_data(data)
    # print(left_top_data)

    # print("wx4bz left bottom data wx4bw")
    # left_bottom_data = OHHOGeohash.get_left_bottom_data(data)
    # print(left_bottom_data)

    # letter = 'c'
    # is_odd = 1
    # row, column = OHHOGeohash.get_index(letter, is_odd)
    # top_row, top_column = OHHOGeohash.get_top(row, column, is_odd)
    # border = OHHOGeohash.get_border(row, column, is_odd)
    # top_letter = OHHOGeohash.get_letter(top_row, top_column, is_odd)
    # print(border)
    # print(top_letter)
    # print(OHHOGeohash.is_odd(2))
