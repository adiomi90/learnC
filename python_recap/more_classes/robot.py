class Robot:
    """show a robot with a name"""
    population = 0

    def __init__(self, name):
        """initilases the name"""
        self._name = name
        print(f"Initializing {self._name}")

        #update the population on creation of a robot
        Robot.population += 1

    def die(self):
        """Dead robot"""
        print(f"{self._name} is being destroyed!")

        Robot.population -= 1

        if Robot.population == 0:
            print(f"{self._name} was the last one")
        else:
            print(f"There are still {Robot.population} robots working")

    def say_hi(self):
        """Greetins by the robots"""
        print(f"Greetings, my master call me {self._name}")

    @classmethod
    def how_many(cls):
        """print the current population"""
        print(f"We have {cls.population} robots")


driod1 = Robot("R2-D2")
driod1.say_hi
Robot.how_many()

driod2 = Robot("C-3P0")
driod2.say_hi
Robot.how_many()


driod1.die()
driod2.die()

Robot.how_many()


driod1.die()
driod2.die()

Robot.how_many()
