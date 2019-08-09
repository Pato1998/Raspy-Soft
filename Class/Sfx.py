import os

class Sfx:
    os=""
    #Constructor verifica el os (win=nt, no-win=posix)
    def __init__(self):
        self.os = os.name
    def start(self):
        if self.os == "nt":
            import winsound
            winsound.Beep(1255, 150)
            winsound.Beep(1055, 150)
            winsound.Beep(1455, 150)
        else:
            import os
            os.system("beep -f 1255 -l 150")
            os.system("beep -f 1055 -l 150")
            os.system("beep -f 1255 -l 150")