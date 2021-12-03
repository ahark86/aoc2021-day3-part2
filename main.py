with open('input.txt') as input_file:
    input = [item.strip() for item in input_file.readlines()]


def bin_to_dec(bin_num):
    dec_num = 0
    power = len(str(bin_num)) - 1
    for digit in str(bin_num):
        to_add = int(digit) * 2 ** power
        dec_num += to_add
        power -= 1
    return dec_num


def calc_o2_rating(input_list):
    total_0 = 0
    total_1 = 0
    for n in range(0, len(input_list[0])):
        for reading in input_list:
            if reading[n] == '0':
                total_0 += 1
            else:
                total_1 += 1
        if total_0 > total_1:
            input_list = [reading for reading in input_list if reading[n] == '0']
        else:
            input_list = [reading for reading in input_list if reading[n] == '1']
        total_0 = 0
        total_1 = 0
        if len(input_list) == 1:
            return input_list[0]
    return input_list[0]


def calc_co2_rating(input_list):
    total_0 = 0
    total_1 = 0
    for n in range(0, len(input_list[0])):
        for reading in input_list:
            if reading[n] == '0':
                total_0 += 1
            else:
                total_1 += 1
        if total_1 < total_0:
            input_list = [reading for reading in input_list if reading[n] == '1']
        else:
            input_list = [reading for reading in input_list if reading[n] == '0']
        total_0 = 0
        total_1 = 0
        if len(input_list) == 1:
            return input_list[0]
    return input_list[0]


def calc_ls_rating(o2_rat, co2_rat):
    return bin_to_dec(o2_rat) * bin_to_dec(co2_rat)

o2_rating = calc_o2_rating(input)
print(o2_rating)
co2_rating = calc_co2_rating(input)
print(co2_rating)

ls_rating = calc_ls_rating(o2_rating, co2_rating)
print(ls_rating)
