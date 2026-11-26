text = input("Enter text: ")
with open("output.txt", "w") as f:
    f.write(text)
print("Written successfully!")
