import json


def triangle_zhonxin(a: tuple, b: tuple, c: tuple):
    """求三角形的重心"""
    return ((int(a[0]) + int(b[0]) + int(c[0])) / 3), (
        (int(a[1]) + int(b[1]) + int(c[1])) / 3
    )


def read_json(MENU_FILE: str) -> dict:
    with open(MENU_FILE, "r", encoding="UTF-8") as f:
        return json.load(f)


def print_json(menu_dict: dict) -> None:
    newjson = json.dumps(menu_dict, ensure_ascii=False, indent=4)
    print(newjson)


def process_data(menu_dict: dict, discount: float) -> None:
    for category in menu_dict["categories"]:
        for item in category["items"]:
            item["price"] = int(round(float(item["price"]) * float(discount)))
    newjson = json.dumps(menu_dict, ensure_ascii=False, indent=4)
    print(newjson)
    return menu_dict


def write_json(menu_dict: dict, OUTPUT_FILE: str) -> None:
    with open(OUTPUT_FILE, "w", encoding="UTF-8") as f:
        OUTPUT_FILE = json.dump(menu_dict, f, ensure_ascii=False, indent=4)
    return OUTPUT_FILE
