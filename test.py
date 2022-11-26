def f():
    print("f1")

def f2():
    print("f2")
    return None

def f3():
    print("f3")
    return

print(f())
print(f2())
print(f3())
