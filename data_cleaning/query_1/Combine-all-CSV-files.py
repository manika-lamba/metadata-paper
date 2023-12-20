import csv
import os

inputFolderPath = "\\16_march_2021\\data"
outFilePath = "\\16_march_2021\output.csv"

order = {}
order_order = []
last_num = 0
all_files = os.listdir(inputFolderPath)
all_new_rows = []
for file in all_files:
    with open(inputFolderPath + "//" + file, "r") as dataFile:
        dataFileReader = csv.reader(dataFile, delimiter=',')
        curMap = {}
        isFirst = 0
        for row in dataFileReader:
            new_row = [''] * 15
            for idx, field in enumerate(row):
                if field == None or str(field) == '' or (str(field)).isspace():
                    continue
                if (isFirst == 0):
                    field = str(field).strip()
                    if (field == 'University/institution' or field == 'University/insitution' or field == 'University'):
                        field = 'University/institution'
                    if (field == 'Dissertation/thesis number' or field == 'Dissertion/thesis number'):
                        field = 'Dissertation/thesis number'
                    if (field == 'Identifier / keyword' or field == 'Identifier/keyword'):
                        field = 'Identifier/keyword'
                    if (field == 'Number of pages' or field == 'Pages'):
                        field = 'Number of pages'
                    if (field == 'Degree date' or field == 'Year'):
                        field = 'Degree date'
                    if (field == 'University location' or field == 'Location'):
                        field = 'University location'
                    if((str(field)).lower() not in order):
                        order[(str(field)).lower()] = last_num
                        order_order.append(str(field))
                        last_num += 1

                    curMap[idx] = (str(field)).lower()
                else:
                    new_row[order[curMap[idx]]] = field
            isFirst += 1
            all_new_rows.append(new_row)

with open(outFilePath, mode='wb') as out_file:
    all_writer = csv.writer(out_file, delimiter=',')
    all_writer.writerow(order_order)
    for new_row in all_new_rows:
        if all('' == s or s.isspace() for s in new_row):
            continue
        all_writer.writerow(new_row)
