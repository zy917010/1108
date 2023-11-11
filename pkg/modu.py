import json


def triangle_zhonxin(a: tuple, b: tuple, c: tuple):
    """求三角形的重心"""
    x = int(round(((int(a[0]) + int(b[0]) + int(c[0])) / 3), 0))
    y = int(round(((int(a[1]) + int(b[1]) + int(c[1])) / 3), 0))
    return x, y


def read_json(MENU_FILE: str) -> dict:
    """將 json 檔案轉為字典後回傳"""
    with open(MENU_FILE, "r", encoding="UTF-8") as f:
        return json.load(f)


def print_json(menu_dict: dict) -> None:
    """將字典轉爲 json 字串後輸出到螢幕"""
    newjson = json.dumps(menu_dict, ensure_ascii=False, indent=4)
    print(newjson)


def process_data(menu_dict: dict, discount: float) -> None:
    """將字典中每個菜品的價格打discount 折數"""
    for category in menu_dict["categories"]:
        for item in category["items"]:
            item["price"] = int(round(float(item["price"]) * float(discount)))
    newjson = json.dumps(menu_dict, ensure_ascii=False, indent=4)
    print(newjson)
    return menu_dict


def write_json(menu_dict: dict, OUTPUT_FILE: str) -> None:
    """將字典轉為檔案"""
    with open(OUTPUT_FILE, "w", encoding="UTF-8") as f:
        OUTPUT_FILE = json.dump(menu_dict, f, ensure_ascii=False, indent=4)
    return OUTPUT_FILE
