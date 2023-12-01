#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    a = 1
    b = 2

    add_result = add(a, b)
    sub_result = sub(a, b)
    mul_result = mul(a, b)
    div_result = div(a, b)

    print("{:d} + {:d} = {:d}".format(a, b, add_result))
    print("{:d} - {:d} = {:d}".format(a, b, sub_result))
    print("{:d} * {:d} = {:d}".format(a, b, mul_result))
    print("{:d} / {:d} = {:d}".format(a, b, div_result))

