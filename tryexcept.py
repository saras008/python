try:
    print(5)
except NameError:
    print("Variable x not define yet")
except:
    print("There is another error")