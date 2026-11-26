try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Error: Invalid input!")
else:
    print("Square:", num * num)
finally:
    print("Program finished")
