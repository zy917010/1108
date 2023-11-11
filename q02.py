students = []
student = {}
student = dict()
t = 0
ex = "員工薪資輸入\n若姓名處未輸入則代表結束\n"
print("{:^30}".format(ex))

while True:
    name = input("請輸入姓名:")
    student["eName"] = name
    students.append(student["eName"])
    if name == "":
        break
    money = input("請輸入薪資:")
    student["eSalary"] = money
    students.append(student["eSalary"])


print("-" * 80)
length = int(len(students) - 1)
for i in range(0, length, 2):
    print("員工", students[i], " 的薪資為{}".format(students[i + 1]))
for j in range(1, length, 2):
    a = int(students[j])
    t += a

print("-" * 80)
if len(students) != 1:
    sum = float(t / ((len(students) - 1) / 2))
    T = round(sum, 2)
    print("合計薪資：{:>10,}".format(t))
    print("平均薪資：{:>13}".format(T))
else:
    print("合計薪資：0")
    print("平均薪資：0.00")
