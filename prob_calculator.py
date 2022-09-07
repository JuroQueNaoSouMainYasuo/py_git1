class Hat():
    def __init__(self, **kwargs):
        self.contents = []
        if len(kwargs) > 0:
            raise ValueError("The hat is empty!")
        for key, value in kwargs.items():
            for i in range(value):
                self.contents.append(key)
    # This method should remove balls at random from contents and return those balls as a list of strings
    # The balls should not go back into the hat during the draw, similar to an urn experiment without replacement.
    # If the number of balls to draw exceeds the available quantity, return all the balls.
    # If the hat is empty, return an empty list.
    def draw(self, number_of_balls):
        if number_of_balls > len(self.contents):
            return self.contents
        if len(self.contents) == 0:
            return []
        

hat1 = Hat(yellow=3, blue=2, green=6)
print(hat1.contents)