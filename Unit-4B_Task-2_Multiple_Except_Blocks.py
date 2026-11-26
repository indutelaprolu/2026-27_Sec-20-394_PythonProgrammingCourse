lst = [10, 20, 30, 40, 50]
try:
    index = int(input("Enter index: "))
    print("Value:", lst[index])
except ValueError:
    print("Error: Please enter a valid integer!")
except IndexError:
    print("Error: Index out of range!")
