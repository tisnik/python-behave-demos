import ctypes

libname = "libadder.so"

adder = ctypes.CDLL(libname)

for x in range(0, 6):
    for y in range(0, 6):
        result = adder.add(x,y)
        print("{x} + {y} = {z}".format(x=x, y=y, z=result))
