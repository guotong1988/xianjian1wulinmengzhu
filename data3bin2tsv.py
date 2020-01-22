input = "data/Data3.bin"

f = open(input,mode="rb")

import os
file_size = os.path.getsize(input)

row_names = ["属性名","头像","战像","形象","名字","全攻",
             "未知","级别","HPmax","MPmax","HP","MP","头戴",
             "披挂","身穿","手持","脚穿","配戴","武术","灵力",
             "防御","身法","吉运","毒抗","风抗","雷抗","水抗",
             "火抗","土抗","未知","未知","未知","受援"]

row_names += ["法术"]*32

row_names += ["行桢","合体","未知","未知","死亡音效",
              "普攻音效","武器音效","倍攻音效","施法音效",
              "格挡音效","被击音效"]


column_names = ["lixiaoyao","zhaolinger","linyueru","wuhou","anu","gailuojiao"]

line_num = int(file_size / len(column_names) / 2)

matrix = []
for l in range(line_num):
    row = []
    for i in range(0,len(column_names)):

        tmp = f.read(1)
        tmp2 = f.read(1)

        row.append(int((tmp2+tmp).hex(),16))
    matrix.append(row)

f2 = open("data/data3.tsv",encoding="utf-8",mode="w")

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


