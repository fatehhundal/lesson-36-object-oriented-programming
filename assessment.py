class Robot:
    def __init__(self, model_name, nickname):
        self.model_name = model_name
        self.nickname = nickname
    
    def bootup(self):
        return "{} has now booted up.".format(self.model_name)

    def introduce(self):
        return '"Hello Harsh, my model name is {}, but you can call me {}."'.format(self.model_name, self.nickname)

tom = Robot("T0M-1940", "Tom")
jerry = Robot("J3RRY-1940", "Jerry")

print(tom.bootup())
print(tom.introduce())
print("\n")
print(jerry.bootup())
print(jerry.introduce())