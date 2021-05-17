#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        divide_result = a/b
    except (ZeroDivisionError, TypeError):
        divide_result = None
    finally:
        print("{:s} {}".format("Inside result:", divide_result))
    return(divide_result)
