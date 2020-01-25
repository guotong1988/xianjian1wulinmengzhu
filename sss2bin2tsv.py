input = "data/Sss2.bin"

f = open(input,mode="rb")

import os
file_size = os.path.getsize(input)


column_names = ["关联参数","属性参数","脚本1","脚本2","脚本3","作用参数","一个脚本入口"]

row_names = ["系统"] * 53
row_names += ["人物"] * 6
row_names += ["物品"] * 234
row_names += ["仙术"] * 104
row_names += ["怪物"] * 153
row_names += ["中毒"] * 14
row_names += ["空"]
print(len(row_names))

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

f2 = open("data/sss2.tsv",encoding="utf-8",mode="w")

for col in column_names:
    f2.write(col)
    f2.write("\t")
f2.write("\n")
for i,row in enumerate(matrix):
    f2.write(row_names[i])
    f2.write("\t")
    for cell in row:
       f2.write(str(cell))
       f2.write("\t")
    f2.write("\n")


