def foo():
    print("this is foo")

def bar():
    print("this is bar")

def sum(a, b):
    print(f"suma {a} + {b} = {a+b}")
    assert a != b

if __name__ == "__main__":
    print("Running script")
    sum(4, 5)
