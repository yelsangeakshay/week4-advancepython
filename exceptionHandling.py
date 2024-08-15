try:
    with open("Sample.txt",'r') as f:
        print(f.read())
        #print(m)
        print(5/0)
except FileNotFoundError:
    print("FIle not found")
except NameError:
    print("Variable not found")
except ZeroDivisionError:
    print("Cannot divide by zero")
except Exception as e:
    print(e.with_traceback)