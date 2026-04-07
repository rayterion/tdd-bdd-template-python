
def triangleArea(base, height):
    if base < 0 or height < 0:
        raise ValueError("Base and height must be non-negative.")
    return 0.5 * base * height