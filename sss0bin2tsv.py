input = "data/Sss0.bin"

f = open(input,mode="rb")

import os
file_size = os.path.getsize(input)


column_names = ["消失时间","事件X坐标","事件Y坐标","图层","触发脚本","自动脚本","触发状态",
                "触发方式","事件标志物","动态图像参数","静态图像参数","特殊图像参数","不明",
                "时间参数","每方向动作帧数","自动脚本"]

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

f2 = open("data/sss0.tsv",encoding="utf-8",mode="w")

for col in column_names:
    f2.write(col)
    f2.write("\t")
f2.write("\n")
for i,row in enumerate(matrix):
    for cell in row:
       f2.write(str(cell))
       f2.write("\t")
    f2.write("\n")


