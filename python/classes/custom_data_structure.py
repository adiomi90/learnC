class CloudTag:
    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower())

    def __setitem__(self, tag, count):
        self.__tags[tag] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)

    def __str__(self):
        return str(self.__tags)
        pass


cloud = CloudTag()
cloud.add("particles")
cloud.add("particles")
cloud.add("particles")
cloud.add("particles")
cloud.add("particles")

print(cloud["particles"])
print(cloud)
print(len(cloud))
cloud["particles"] = 20
print(cloud)
