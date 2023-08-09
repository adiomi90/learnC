class Test(str):
    def duplicate(self):
        return self +  self


text = Test("Python")
print(text.duplicate())

class TrackableList(list):
    def append(self, object):
        print("Append called")
        super().append(object)


list = TrackableList()
list.append("l")
