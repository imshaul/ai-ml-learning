try:
    a = int(input("Enter a num :"))
    print(1/a)
except ZeroDivisionError:
    print("you cant divide by zero")
except ValueError:
    print("Invalid input")
except Exception:
    print("something went wrong")
finally:
    print("do some clean up here")