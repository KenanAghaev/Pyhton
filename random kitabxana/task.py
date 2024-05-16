import random

def kv():
    ededler = []

   
    for _ in range(5):
        eded = random.randint(20, 50)
        ededler.append(eded)


    kvadrat = [eded ** 2 for eded in ededler if eded % 2 == 0]

    print(ededler)

    return kvadrat


print(kv())
