import json


def triangle_zhonxin(a: tuple, b: tuple, c: tuple):
    """求三角形的重心"""
    return ((int(a[0]) + int(b[0]) + int(c[0])) / 3), (
        (int(a[1]) + int(b[1]) + int(c[1])) / 3
    )


def print_json(data: dict) -> None:
    # json.dump() 將 dict 轉成 JSON 格式，寫入 JSON 檔案
    print = json.dumps(data, ensure_ascii=False, indent=4)
    print(print)


def process_data(data1: dict, discount: float) -> None:
    data1["price"] = int(round(float["price"] * float(discount)))
    return data1


def read_json(file_name: str) -> dict:
    with open(file_name, "r", encoding="UTF-8") as f:
        # json.load() 讀取 JSON 檔案，轉換為 Python 的 dict
        menu_dict = json.load(f)
    return menu_dict


def write_json(data2: dict) -> None:
    with open(data2, "w", encoding="UTF-8") as f:
        json.dump(data2, f, ensure_ascii=False, indent=4)
    return
