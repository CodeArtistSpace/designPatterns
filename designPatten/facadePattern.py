class Light:
    def turn_on(self):
        print("Light is on")

    def turn_off(self):
        print("Light is off")


class SoundSystem:
    def turn_on(self):
        print("Sound system is on")

    def turn_off(self):
        print("Sound system is off")

    def set_volume(self, volume):
        print(f"Volume set to {volume}")


class Curtain:
    def close(self):
        print("Curtain is closed")

    def open(self):
        print("Curtain is opened")


# 外观
class HomeTheaterFacade:
    def __init__(self):
        self.light = Light()
        self.sound = SoundSystem()
        self.curtain = Curtain()

    def activate_movie_mode(self):
        print("Activating movie mode...")
        self.light.turn_off()
        self.sound.turn_on()
        self.sound.set_volume(5)
        self.curtain.close()


# 客户端代码
facade = HomeTheaterFacade()
facade.activate_movie_mode()
