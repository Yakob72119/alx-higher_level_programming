#!/usr/bin/python3

def magic_calculation(a, b):
    """Match the bytecode"""
    from magic_calculation_102 import add, sub

    if a < b:
        total = add(a, b)
        for i in range(4, 6):
            total = add(total, i)
        return (total)
    else:
        return(sub(a, b))
