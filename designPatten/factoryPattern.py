from abc import ABC, abstractmethod

# 日志记录器接口
class Logger(ABC):
    @abstractmethod
    def log(self, message: str):
        pass

# 记录到控制台的日志记录器
class ConsoleLogger(Logger):
    def log(self, message: str):
        print(f"Console: {message}")

# 记录到文件的日志记录器
class FileLogger(Logger):
    def log(self, message: str):
        with open("log.txt", "a") as file:
            file.write(f"File: {message}\n")

# 日志记录器工厂
class LoggerFactory:
    @staticmethod
    def get_logger(type: str) -> Logger:
        if type == "console":
            return ConsoleLogger()
        elif type == "file":
            return FileLogger()
        else:
            raise ValueError(f"Logger type {type} not supported")

# 客户端代码
logger = LoggerFactory.get_logger("console")
logger.log("This is a message")

logger = LoggerFactory.get_logger("file")
logger.log("This is another message")