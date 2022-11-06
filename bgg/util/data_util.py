import json
from datetime import date
from os import makedirs
from os.path import exists, join, splitext

OUT_PATH = "./out"


def write_results(src: str, result: dict) -> None:
    src_name = splitext(src)[0]

    today = date.today()
    path = f"{OUT_PATH}/{src_name}/{today.strftime('%Y-%m')}"
    filename = f"{today}.json"

    # create out dirs if they do not exist
    if not exists(path):
        makedirs(path)

    with open(join(path, filename), "w") as f:
        json.dump(result, f, indent=4, ensure_ascii=False)

    print(f"{src_name} results successfully written to {path}/{filename}")
