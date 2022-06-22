def n_cosmetics():
    x=0
    while True:
        x += 1
        yield "C" + str(x)

def n_pharmacy():
    y = 0
    while True:
        y += 1
        yield "Ph" + str(y)


def n_perfumery():
    z = 0
    while True:
        z += 1
        yield "P" + str(z)


perfumery = n_perfumery()
pharmacy = n_pharmacy()
cosmetics = n_cosmetics()

def decorator(function):
    def interior():
        print("Your turn is:")
        print(next(function))
        print("Wait until you are attended")
    return interior
