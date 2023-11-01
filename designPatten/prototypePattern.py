import copy

class SystemSettings:
    def __init__(self):
        # 假设从配置文件或数据库中加载以下设置
        self.volume = 10
        self.brightness = 50
        # ... 可能还有其他设置 ...

    def clone(self):
        # 使用深拷贝来确保新的对象是原始对象的完整拷贝，而不仅仅是引用
        return copy.deepcopy(self)

    def __str__(self):
        return f"Volume: {self.volume}, Brightness: {self.brightness}"

# 模拟首次从数据库或文件加载
original_settings = SystemSettings()

# 基于原始设置进行克隆，而不是重新加载
user1_settings = original_settings.clone()
user1_settings.volume = 5

user2_settings = original_settings.clone()
user2_settings.brightness = 70

print(original_settings)
print(user1_settings)
print(user2_settings)
