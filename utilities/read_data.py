# a function will return data from a csv file
import csv
#just practiced the file reading and parcing data
# def get_csv_data_1(file_name):
#     rows = []
#
#     file_handle = open(file_name, 'r')
#     lines = file_handle.readlines()
#     print(lines)
#     for i in range(1, len(lines)):
#         if i > 0:
#             line = lines[i].rstrip().split(',')
#             if len(line) == 4:
#                 rows.append(line)
#     file_handle.close()
#     return rows

def get_csv_data(file_name):
    rows = []
    with open(file_name, 'r', newline='') as f:
        reader = csv.reader(f)
        # to skip a line with the headers
        next(reader)
        for row in reader:
            rows.append(row)
    return rows

# print(get_csv_data_1('/home/anna/PycharmProjects/letscodit/test_data.csv'))
# print(get_csv_data('/home/anna/PycharmProjects/letscodit/test_data.csv'))
