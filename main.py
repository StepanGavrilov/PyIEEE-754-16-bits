def ie754_encode(float_num: float) -> bytearray:
    """"""

    sign = 1
    exp = 15
    b_array = bytearray()

    if float_num == 0:
        b_array.append(0)
        b_array.append(0)

        return b_array

    if float_num > 0:
        sign = 0

    float_num = abs(float_num)

    integer_part = int(float_num)

    while integer_part != 1:
        integer_part = integer_part >> 1
        exp += 1

    high = (pow(2, exp - 14))
    low = high >> 1

    mantissa = round(((float_num - low) / (high - low)) * 1024)

    exp = mantissa | (exp << 10) | (sign << 15)

    b_array.append((exp & 65280) >> 8)
    b_array.append(exp & 255)

    return b_array


def ie754_decode(b_array: bytearray) -> float:
    """"""

    sign = (b_array[0] >> 7) & 1
    exp = (b_array[0] >> 2) & 31
    mantissa = (((b_array[0]) & 3) << 8) | b_array[1]

    result = round(pow(-1, sign) * pow(2, exp - 15) * (1.0 + (float(mantissa) / 1024)), 1)

    return result


if __name__ == '__main__':
    pass
