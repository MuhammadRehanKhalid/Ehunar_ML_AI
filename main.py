# Module


# what is module


# why we need it


# How does it works
# body
# from West.america import body
# # chasis
# from East.china import chasis
# # engines
# from West.germany import engines
# # tyres
# from West.italy import tyres

from West import america, italy, germany
from East import china
def car_ass():
    """
    This function generates a string describing the components of a car.
    It takes no parameters and returns no value, instead printing the result directly.
    """
    print(f'{america.body()}, {china.chasis()}, {germany.engines()}, and {italy.tyres()} makes a car')

car_ass()