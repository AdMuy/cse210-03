import random


# TODO: Implement the Die class as follows...

# 1) Add the class declaration. Use the following class comment.
class Die:
    """A small cube with a different number of spots on each of its six sides.

    The responsibility of Die is to keep track of the side facing up and calculate the points for 
    it.
   
    Attributes:
        value (int): The number of spots on the side facing up.
        points (int): The number of points the die is worth.
    """

# 2) Create the class constructor. Use the following method comment.
    def __init__(die):
        """Constructs a new instance of Die with a value and points attribute.

        Args:
            self (Die): An instance of Die.
        """
        die.value = 0
        die.points = 0

# 3) Create the roll(self) method. Use the following method comment.
    def roll(die):
        """Generates a new random value and calculates the points.
        
        Args:
            self (Die): An instance of Die.
        """
        seed = [1, 2, 3, 4, 5, 6]
        die.value = random.choice(seed)
        if die.value == 5:
            die.points += 50
        elif die.value == 1:
            die.points += 100
        else:
            die.points += 0
