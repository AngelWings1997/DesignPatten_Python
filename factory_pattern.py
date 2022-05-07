# Python原生默认不支持接口，默认多继承，所有的方法都必须不能实现
from abc import abstractmethod, ABCMeta


# 声明一个抽象接口
class Shape(metaclass=ABCMeta):
    @abstractmethod
    def draw(self):
        pass


# 三个形状继承实现 Shape 接口
class Rectangle(Shape):
    def draw(self):
        print("Inside Rectangle.draw method")


class Square(Shape):
    def draw(self):
        print("Inside Square.draw method")


class Circle(Shape):
    def draw(self):
        print("Inside Circle.draw method")


# 创建一个工厂
class ShapeFactory():
    def getShape(self, shapeType):
        if shapeType is None:
            return None
        elif shapeType.upper() == "CIRCLE":
            return Circle()
        elif shapeType.upper() == "RECTANGLE":
            return Rectangle()
        elif shapeType.upper() == "SQUARE":
            return Square()
        return None


# 输出
if __name__ == '__main__':
    shapeFactory = ShapeFactory()
    shape1 = shapeFactory.getShape("CIRCLE")
    shape1.draw()
    shape2 = shapeFactory.getShape("RECTANGLE")
    shape2.draw()
    shape3 = shapeFactory.getShape("SQUARE")
    shape3.draw()