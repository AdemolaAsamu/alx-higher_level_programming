#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    import calculator_1
    size = len(sys.argv)
    if size != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])
    if operator == '+':
        out = add(a, b)
        print(f"{a} {operator} {b} = {out}")
    elif operator == '-':
        out = sub(a, b)
        print(f"{a} {operator} {b} = {out}")
    elif operator == '*':
        out = mul(a, b)
        print(f"{a} {operator} {b} = {out}")
    elif operator == '/':
        out = div(a, b)
        print(f"{a} {operator} {b} = {out}")
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
