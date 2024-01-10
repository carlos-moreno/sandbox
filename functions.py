import os

files_with_zone = [
    "assets/file_01_20240110_Z01.txt",
    "assets/file_02_20240110_Z01.txt",
    "assets/file_03_20240110_Z01.txt",
    "assets/file_01_20240110_Z02.txt",
    "assets/file_01_20240110_Z03.txt",
]

files_without_zone = [
    "assets/file-01.txt",
    "assets/file-02.txt",
    "assets/file.txt",
    "assets/file-05.txt",
]

d = {"teste": 3}


def generate_list_for_column(idx_column, files):
    sublistas = {}

    for file_ in files:
        zona = file_.split("_")[-1].split(".")[0]
        sublistas.setdefault(zona, []).append(file_)

    return sublistas

def sorting_key(file_):
    return os.stat(file_).st_mtime

def order_list(files):
    if d.get(idx_zone):
        ...
    else:
        return sorted(files, key=sorting_key, reverse=True)


def latest_file(files):
    recent_file = None
    time_recent = None

    for file in files:
        time = os.stat(file).st_mtime

        if time_recent is None or time > time_recent:
            time_recent = time
            recent_file = file

    return recent_file


print(
    latest_file(
        ["assets/file-01.txt", "assets/file-02.txt", "assets/file.txt"]
    )
)
