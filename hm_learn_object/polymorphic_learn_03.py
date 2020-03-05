class Dog(object):

    def __init__(self, name):
        self.name = name

    def play(self):
        print("%s 玩耍" % self.name)


class XiaoTianDog(Dog):
    def play(self):
        print("%s 飞到天上去玩耍" % self.name)


class Person(object):

    def __init__(self, name):
        self.name = name

    def play_dog(self, dog):
        print("%s和%s快乐的玩耍..." % (self.name, dog.name))
        dog.play()


wangcai = XiaoTianDog("feitianwangcai")
xiaomin = Person("xiaomin")
xiaomin.play_dog(wangcai)
