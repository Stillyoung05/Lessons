def my_func(*args):
    try:
        a = int(input("Enter num: "))
        b = int(input("Enter num2: "))
        print(a + b)
    except ValueError:
        print("Enter available data")
