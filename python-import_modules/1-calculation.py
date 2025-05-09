#!/usr/bin/python3

if __name__ == "__main__":
    import calculator_1 as calculation_module

    a = 10
    b = 5

    print("{} + {} = {}".format(a, b, calculation_module.add(a, b)))
    print("{} - {} = {}".format(a, b, calculation_module.sub(a ,b)))
    print("{} * {} = {}".format(a, b, calculation_module.mul(a ,b)))
    print("{} / {} = {}".format(a, b, calculation_module.div(a ,b)))
