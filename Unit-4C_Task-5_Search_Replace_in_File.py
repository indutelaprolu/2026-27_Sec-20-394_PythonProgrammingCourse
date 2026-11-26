with open("sample.txt", "r") as f:
    data = f.read()
data = data.replace("Python", "Java")
with open("sample.txt", "w") as f:
    f.write(data)
print("Replaced successfully!")
print(data)
