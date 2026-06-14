class Camera:
    def take_photo(self):
        print("Kichik Kichik📸")

class MusicPlayer:
    def play_music(self):
        print("Dhoom machale⚡!!Dhoom machale!!⚡")

class SmartPhone(Camera,MusicPlayer):
    pass

phone=SmartPhone()
phone.take_photo()
phone.play_music()






