class Robot:
    population = 0

    def __init__(self, name):
        self.name = name
        print("Initilaizing {}".format(self.name))

        Robot.population += 1


    def die(self):
        print("{} is being destroyed".format(self.name))
        Robot.population -= 1

        if Robot.population == 0:
             print("{} was the last one.".format(self.name))
        else:
             print("There are still {:d} robots working.".format(Robot.population))


    def say_hi(self):
        print("Greetings, my masters call me {}".format(self.name))

    @classmethod
    def how_many(cls):
        print("We have {:d}".format(cls.population))

    


driod = Robot("ri")
driod.say_hi()
driod.how_many()

driod2 = Robot("r2")
driod2.say_hi()
driod2.how_many()

driod.die()
driod2.die()

Robot.how_many()