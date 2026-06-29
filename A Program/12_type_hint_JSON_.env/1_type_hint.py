# normally
def add(a, m):
    return a + m


# using type hints
def add(a: int, m: int) -> int:
    return a + m


def info(name: str, age: int) -> str:
    return f"My name is {name} and I am {age} year old."
print(info("Atharva",19))


def sub(a: int, m: int) -> int:
    return a - m
print(sub(19,7))


def mul(x: int, y: int) -> int:
    return x*y
print(mul(19,7))


def add_return(a,m):
    return a+m

def add_print(a,m):
    print(a+m)


# return version
result = add_return(2,3)
print(result * 2)


# print version
result = add_print(2,3)

