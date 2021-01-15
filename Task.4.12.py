def divide():
    return 5/0

try:
    divide()
except ZeroDivisionError as zero:
    print("Why dividing a number by ZERO!!")
except:
    print("other exception")