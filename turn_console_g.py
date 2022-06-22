def n_cosmetics():
    x=0
    while True:
        x += 1
        yield "C" + str(x)

def n_pharmacy():
    x = 0
    while True:
        x += 1
        yield "P" + str(x)


def n_perfumery():
    x = 0
    while True:
        x += 1
        yield "Ph" + str(x)


def decorator(function):
    def interior():
        print("Your turn is:")
        print(next(function()))
        print("Wait until you are attended")
    return interior
