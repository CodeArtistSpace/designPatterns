from abc import ABC, abstractmethod


# 抽象工厂
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass


# 具体工厂：Windows
class WindowsFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()

    def create_checkbox(self):
        return WindowsCheckbox()


# 具体工厂：MacOS
class MacOSFactory(GUIFactory):
    def create_button(self):
        return MacOSButton()

    def create_checkbox(self):
        return MacOSCheckbox()


# 产品：按钮
class Button(ABC):
    @abstractmethod
    def click(self):
        pass


class WindowsButton(Button):
    def click(self):
        print("Windows button clicked!")


class MacOSButton(Button):
    def click(self):
        print("MacOS button clicked!")


# 产品：复选框
class Checkbox(ABC):
    @abstractmethod
    def toggle(self):
        pass


class WindowsCheckbox(Checkbox):
    def toggle(self):
        print("Windows checkbox toggled!")


class MacOSCheckbox(Checkbox):
    def toggle(self):
        print("MacOS checkbox toggled!")


# 客户端代码
def create_ui(factory: GUIFactory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    button.click()
    checkbox.toggle()


# 使用Windows的UI元素
create_ui(WindowsFactory())

# 使用MacOS的UI元素
create_ui(MacOSFactory())
