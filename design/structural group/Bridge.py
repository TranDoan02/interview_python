class RemoteControl:
    def __init__(self, device):
        self.device = device

    def toggle_power(self):
        if self.device.is_enabled():
            self.device.disable()
        else:
            self.device.enable()

class TV:
    def __init__(self):
        self.on = False
    def is_enabled(self):
        return self.on
    def enable(self):
        self.on = True
    def disable(self):
        self.on = False

tv = TV()
remote = RemoteControl(tv)
remote.toggle_power()
print(tv.is_enabled())  # True
# Tách riêng phần trừu tượng và phần hiện thực, giúp hai phần có thể thay đổi độc lập mà không ảnh hưởng lẫn nhau.

# Thường dùng khi có nhiều biến thể của đối tượng ở cả hai phía (giao diện và cài đặt).