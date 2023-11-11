from pkg.modu import print_json, process_data, read_json, write_json


MENU_FILE = "menu.json"
OUTPUT_FILE = "output.json"

new_item = {
    "name": "海鮮燉飯",
    "price": 239,
    "description": "西班牙的代表美食，海鮮配料豐富、色彩繽紛"
}

menu_dict = read_json(MENU_FILE)

print_json(menu_dict)

menu_dict["categories"][1]["items"].append(new_item)

discount = float(input("請輸入折扣率(0.0 ~ 1.0):"))

process_data(menu_dict, discount)

write_json(menu_dict, OUTPUT_FILE)
