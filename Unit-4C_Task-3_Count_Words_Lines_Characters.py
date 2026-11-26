with open("sample.txt", "r") as f:
    data = f.read()
    lines = data.splitlines()
    words = data.split()
    print("Lines:", len(lines))
    print("Words:", len(words))
    print("Characters:", len(data))
