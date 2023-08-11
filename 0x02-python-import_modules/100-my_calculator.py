#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    from calculator_1 import add, sub, mul, div
    size = len(sys.argv)
    if size != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])
    if operator == '+':
        out = add(a, b)
    elif operator == '-':
        out = sub(a, b)
    elif operator == '*':
        out = mul(a, b)
    elif operator == '/':
        out = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    print(f"{a} {operator} {b} = {out})
