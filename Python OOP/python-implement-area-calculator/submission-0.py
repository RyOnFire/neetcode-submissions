import math

class AreaCalc:
    # TODO: Implement calculate method
    def calculate(self, *args):
        if len(args) == 1:
            area1 = math.pi * pow(args[0], 2)
            return round(area1, 2)
        elif len(args) == 2:
            area2 = args[0] * args[1]
            return area2
    

    
# Don't modify the following code
calc = AreaCalc()
print(calc.calculate(5))    
print(calc.calculate(4, 6))
