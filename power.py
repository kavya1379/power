import sys

def power(base, exp):
    return base**exp

if __name__ == "__main__":
    if len(sys.argv) > 2:
        base = float(sys.argv[1])
        exp = int(sys.argv[2])
    else:
        base = float(input("Enter base: "))
        exp = int(input("Enter exponent: "))
    print(power(base, exp))