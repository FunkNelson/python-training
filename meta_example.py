f = open("file.txt")


def convert_to_list(line):
    num_list = [int(x.strip()) for x in line.split(",")]
    return num_list


def get_sum(list):
    sum = 0
    for num in list:
        sum += num
    return sum


def balance_partitions(list):

    list_sum = (get_sum(list))

    half_sum = list_sum / 2
    tmp_sum = 0
    current_index = 0

    for num in list:
        current_index += 1
        tmp_sum += num
        if tmp_sum == half_sum:
            return list[:current_index], list[current_index:]


for line in f:
    num_list = convert_to_list(line)
    balanced_partitions = balance_partitions(num_list)
    if balanced_partitions != None:
        print(balanced_partitions)


f.close()
