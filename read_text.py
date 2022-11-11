data = open('Data.txt', 'r', encoding='utf-8').readlines()


def d_d(file):
    dict_data = {}
    for i in range(len(file)):
        file[i] = file[i].split()
        dict_data[file[i][1]] = dict_data.get(file[i][1], 0) + int(file[i][2])
    return dict_data


print(type(d_d(data)))