import random
def lotto(ticket):
    print('Use from current folder')
    return[random.randint(0,99) for x in range(0,ticket)]