class ConfigurationManager:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.init_configurations()
        return cls._instance

    def init_configurations(self):
        # 假设这里我们读取一个配置文件来初始化设置。
        # 为简化起见，这里只初始化一个简单的字典。
        self._configurations = {"setting1": "value1", "setting2": "value2"}

    def get_configuration(self, key):
        return self._configurations.get(key)

# 测试单例模式
config1 = ConfigurationManager()
config2 = ConfigurationManager()

print(config1 == config2)  # 输出：True, 表明它们是相同的实例

print(config1.get_configuration("setting1"))  # 输出：value1
print(config2.get_configuration("setting2"))  # 输出：value2
