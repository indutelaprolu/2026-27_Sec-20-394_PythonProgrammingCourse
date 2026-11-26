try:
    num = int(input("Enter numerator: "))
    den = int(input("Enter denominator: "))
    print("Result:", num / den)
except ZeroDivisionError:
    print("Error: Denominator cannot be zero!")
except ValueError:
    print("Error: Please enter integers only!")
