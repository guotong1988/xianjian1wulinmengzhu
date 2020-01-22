input = "data/Sss1.bin"

f = open(input,mode="rb")

import os
file_size = os.path.getsize(input)


column_names = ["场景地图编号","场景进入脚本","场景脱离脚本","场景事件定义"]

line_num = int(file_size / len(column_names) / 2)
print(line_num)
matrix = []
for l in range(line_num):
    row = []

    for i in range(0, len(column_names)):
        tmp = f.read(1)
        tmp2 = f.read(1)

        row.append(int((tmp2 + tmp).hex(), 16))

    matrix.append(row)

f2 = open("data/sss1.tsv",encoding="utf-8",mode="w")

for col in column_names:
    f2.write(col)
    f2.write("\t")
f2.write("\n")
for i,row in enumerate(matrix):
    for cell in row:
       f2.write(str(cell))
       f2.write("\t")
    f2.write("\n")


