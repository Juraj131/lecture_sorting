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

def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n-1):
        for j in range(n-i-1):
            if numbers[j] > numbers[j+1]:
                # výmena dvoch susedných prvkov
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers

def insertion_sort(cisla):
    n = len(cisla)
    for i in range(1, n):
        k = i - 1
        while k >= 0 and cisla[k] > cisla[i]:
            cisla[k - 1] = cisla[k]
            k = k - 1
        cisla[k+1] = cisla[i]
    return cisla








def main():
    my_data = read_data('numbers.csv')
    print(my_data['series_1'])
    stlpec = selection_sort(my_data['series_1'])
    print(stlpec)
    bublinky = bubble_sort(my_data['series_1'])
    print(bublinky)
    inserty = insertion_sort(my_data['series_1'])
    print(inserty)
if __name__ == '__main__':
    main()
