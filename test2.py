#usage of python property decorator

class shape:
    def __init__(self, value = 0):
        self.attr = value

    @property
    def score(self):
        #print("%d" % self.attr)
        return self.attr

    @score.setter
    def score(self, value):
        if  not isinstance(value, int):
            raise ValueError("Not a integer")

        if value < 0 or value >= 10:
            raise ValueError("You guys confusing")

        else:
            self.attr += value

circle = shape(2)

print(circle.score)


