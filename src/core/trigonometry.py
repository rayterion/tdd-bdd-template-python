

class Trigonometry:
    def calculate_hypothenuse(a, b):
        if a < 0 or b < 0:
            raise ValueError("Sides must be non-negative.")
        return (a**2 + b**2) ** 0.5
    
    def calculate_sine(opposite, hypotenuse):
        if opposite < 0 or hypotenuse <= 0:
            raise ValueError("Opposite must be non-negative and hypotenuse must be positive.")
        return opposite / hypotenuse