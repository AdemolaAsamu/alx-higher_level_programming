#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    from calculator_1 import add, sub, mul, div
    size = len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <sym> <b>")
        sys.exit(1)
    a = int(sys.argv[1])
    sym = sys.argv[2]
    b = int(sys.argv[3])
    if sym == '+':
        out = add(a, b)
    elif sym == '-':
        out = sub(a, b)
    elif sym == '*':
        out = mul(a, b)
    elif sym == '/':
        out = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    print(f"{a} {sym} {b} = {out})
