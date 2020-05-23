from functools import lru_cache
import sys
import os

# Clear the terminal window
os.system("clear" if os.name == "posix" else "cls")

try:
    desert_length = int(sys.argv[1])
except IndexError:  # Use default value
    desert_length = 100

try:
    fuel_size = int(sys.argv[2])
except IndexError:  # Use default value
    fuel_size = 50


@lru_cache()
def jeep(f):
    if f == 0:
        return 0
    elif f == 1:
        return 1
    else:
        return jeep(f-1) + (1/(2*f-1))


f = 0
while True:
    d = jeep(f) * fuel_size
    if d >= desert_length:
        print(f"Distance: {d}")
        print(f"Fuel used: {f * fuel_size}")
        break
    f += 1
