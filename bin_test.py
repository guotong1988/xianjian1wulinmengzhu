f = open("data/Data3.bin",mode="rb")
tmp = f.read(1)

print(int(tmp.hex(),16))

tmp = f.read(1)
print(int(tmp.hex(),16))

tmp = f.read(1)
print(int(tmp.hex(),16))