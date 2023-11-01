# 老旧的接口
class OldSpeaker:
    def connect_via_3_5mm_jack(self, device):
        device.play_sound_through_3_5mm_jack()

# 新设备接口
class ModernPhone:
    def play_sound_through_type_c(self):
        print("Playing sound through Type-C port")

# 适配器
class TypeCTo3_5mmAdapter:
    def __init__(self, modern_device):
        self.modern_device = modern_device

    def play_sound_through_3_5mm_jack(self):
        # 调用新设备的Type-C方法
        self.modern_device.play_sound_through_type_c()

# 客户端代码
phone = ModernPhone()
adapter = TypeCTo3_5mmAdapter(phone)
speaker = OldSpeaker()
speaker.connect_via_3_5mm_jack(adapter)
