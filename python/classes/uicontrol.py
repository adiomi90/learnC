from abc import ABC, abstractmethod

class UIControl(ABC):
    
    @abstractmethod
    def draw(self):
        pass



class TestBox(UIControl):
    def draw(self):
        print("Drawing a texbox")

class DropDownList(UIControl):
    def draw(self):
        print("Drawing a DropDownlist")


def draw(controls):
    for control in controls:
        control.draw()



ddl = DropDownList()
txtbox = TestBox()

draw([ddl, txtbox])



