import os
import csv

def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)

    with open(file_path, 'r') as csv_file:
        data = {}
        reader = csv.DictReader(csv_file)
        for row in reader:
            for header, value in row.items():
                if header not in data:
                    data[header] = [int(value)]
                else:
                    data[header].append(int(value))
    return data

def selection_sort(stlpec):
    for i in range(len(stlpec)):
        min_num = i
        for j in range(i + 1, len(stlpec)):
            if stlpec[j] < stlpec[min_num]:
                min_num = j
        stlpec[i], stlpec[min_num] = stlpec[min_num], stlpec[i]
    return stlpec

    #i = -1
    #min_number = min(stlpec)
   # for cislo in stlpec:
      #  i += 1
       # if cislo





def main():
    my_data = read_data('numbers.csv')
    print(my_data['series_1'])
    stlpec = selection_sort(selection_sort(my_data['series_1']))
    print(stlpec)

if __name__ == '__main__':
    main()
