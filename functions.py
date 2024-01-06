import os

def latest_file(files):
    recent_file = None
    time_recent = None

    for file in files:
        try:
            time = os.stat(file).st_mtime
        except FileNotFoundError:
            continue

        if time_recent is None or time > time_recent:
            time_recent = time
            recent_file = file

    return recent_file

print(latest_file(['assets/file-01.txt', 'assets/file-02.txt', 'assets/file.txt']))
