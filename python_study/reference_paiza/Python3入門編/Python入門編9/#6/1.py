# coding: utf-8
# クラスの中のメソッドを呼び出す

class Greeting:
    def __init__(self):
        self.msg = "hello"
        self.target = "paiza"

    def say_hello(self):
        print(self.msg + " " + self.target)
        self.__say_yeah()

    def __say_yeah(self):
        print("YEAH YEAH YEAH!")


player = Greeting()
player.say_hello()
