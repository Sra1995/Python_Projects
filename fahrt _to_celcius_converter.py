import math

def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier
    
def convert(s):
    f = float(s)
    c = (f - 32) * 5/9
    return c
    
print(f' This morning it was', round_up(convert(35) , 2))

print(f' This afternoon it was', round_up(convert(48) , 2))

print(f' This evening it was', round_up(convert(43) , 2))