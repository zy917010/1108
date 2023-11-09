import pkg.modu

print("請輸入三角形的 3 個頂點坐標")
print("-" * 80)

a = input("請輸入頂點 a 的坐標：").split(",")
b = input("請輸入頂點 b 的坐標：").split(",")
c = input("請輸入頂點 c 的坐標：").split(",")

x, y = pkg.modu.triangle_zhonxin(a, b, c)

zhonxin = {}
zhonxin = dict()
zhonxin["x"] = x
zhonxin["y"] = y

print("-" * 80 + "\n此三角形的重心為：({},{})".format(zhonxin["x"], zhonxin["y"]))
