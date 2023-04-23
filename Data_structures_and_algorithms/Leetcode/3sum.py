nums = [-1, 0, 1, 2, -1, -4]
# i != j, i != k, and j != k
# [[-1,-1,2],[-1,0,1]]

with open("file.txt") as file:
    for line in file:
        print(line)


class Car:

    def __init__(self, weight, power):
        self.weight = weight
        self.power = power

    def type(self):
        print(self.weight,self.power)

class Truck(Car):
    super()

    def __init__(self, weight, power, load_capacity):
        super().__init__(weight,power)
        self.load_capacity=load_capacity

    def type(self):
        super().type()
        print(self.load_capacity)
