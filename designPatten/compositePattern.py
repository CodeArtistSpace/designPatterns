from abc import ABC, abstractmethod


# 抽象组件
class FileSystemComponent(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def show(self, indent=''):
        pass


# 叶子组件
class File(FileSystemComponent):
    def show(self, indent=''):
        print(f"{indent}- {self.name}")


# 组合组件
class Folder(FileSystemComponent):
    def __init__(self, name):
        super().__init__(name)
        self.children = []

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)

    def show(self, indent=''):
        print(f"{indent}+ {self.name}")
        for child in self.children:
            child.show(indent + '  ')


# 客户端代码
root = Folder("root")
folder1 = Folder("folder1")
folder2 = Folder("folder2")
file1 = File("file1.txt")
file2 = File("file2.txt")
file3 = File("file3.txt")

folder1.add(file1)
folder1.add(file2)
folder2.add(file3)
root.add(folder1)
root.add(folder2)

root.show()
