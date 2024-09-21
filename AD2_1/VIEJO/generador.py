import random
import pyperclip


def generate(n):
    #print(n)
    todo = f"{n}\n"
    for i in range(n):
        #print(f"{random.randint(-100, 100)}, {random.uniform(0, 1)}")
        todo += f"{random.randint(-100, 100)}, {random.uniform(0, 1)}\n"

    #print(n*random.randint(3, 30))
    todo += str(n*random.randint(3, 25))

    pyperclip.copy(todo)
    print("ya")

generate(2_000_000)
