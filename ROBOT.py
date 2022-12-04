# 1 (i). Write the following classes with class variables, instance variable and illustration
# the self variable
#    Robot (to greet the world).
class Robot:
    def __init__(self,name):
        self.name=name
a=Robot(input())
print("Robot says hello to ",a.name)