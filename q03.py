from pkg.modu import print_json, process_data, read_json, write_json

read_json("menu.json")
print_json("menu_dict")
write_json("menu_dict")
process_data("menu_dict")
discount = float(input("請輸入折扣率(0.0 ~ 1.0):"))
