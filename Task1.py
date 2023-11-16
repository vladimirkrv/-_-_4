import json


def task() -> float:
    fname = "input.json"
    with open(fname) as f:
        json_data = json.load(f)

    sum_products = sum([item["score"] * item["weight"] for item in json_data])
    return round(sum_products, 3)


print(task())
