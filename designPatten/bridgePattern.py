from abc import ABC,abstractmethod

# 实现（Platform）
class Platform(ABC):
    @abstractmethod
    def draw(self, shape):
        pass

class WindowsPlatform(Platform):
    def draw(self, shape):
        print(f"Drawing {shape} on Windows")

class LinuxPlatform(Platform):
    def draw(self, shape):
        print(f"Drawing {shape} on Linux")

# 抽象（Shape）
class Shape:
    def __init__(self, platform):
        self.platform = platform

    def draw(self):
        self.platform.draw(self.__class__.__name__)

class Circle(Shape):
    pass

class Rectangle(Shape):
    pass

# 客户端代码
windows = WindowsPlatform()
linux = LinuxPlatform()

circle_on_windows = Circle(windows)
circle_on_windows.draw()

rectangle_on_linux = Rectangle(linux)
rectangle_on_linux.draw()
