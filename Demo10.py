#创建Rectangle和Square类，使它们均有caculatePerimete的方法，计算周长，创建Rectangle和Square对象，并计算周长
class Shape():
    def WhatAmI(self):
        print("I am a shape")
class Rectangle(Shape):
    def __init__(self,s1,s2,s3) -> None:
        self.s1=s1
        self.s2=s2
        self.s3=s3
    def CalculatePerimeter(self):
        return self.s1+self.s2+self.s3
class Square(Shape):
    def __init__(self,s) -> None:
        self.s=s
    def CalculatePerimeter(self):
        return self.s*4
    def ChangeSize(self,s):
        self.s=s
rectangle=Rectangle(3,4,5)
square=Square(3)
print(rectangle.CalculatePerimeter())
print(square.CalculatePerimeter())
#在Square类中，定义一个ChangeSize方法，支持改变边长。
#创建一个Shape类，定义WhatAmI的方法，被调用时打印“I am a shape”
square.WhatAmI()
#创建Horse类，Rider类，使用组合，表示有骑手的马
class Horse():
    def __init__(self,master) -> None:
        self.owner = master
class Rider():
    def __init__(self,name) -> None:
        self.name =name 
goodHorse=Horse(Rider("LiLi"))
print(goodHorse.owner.name)