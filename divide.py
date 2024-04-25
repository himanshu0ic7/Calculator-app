def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print("division by zero!")