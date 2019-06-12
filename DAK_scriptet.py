import tkinter as tk
import json
import os
import time

class DAKScreen:
    def __init__(self):
        self.settingsJSONPath = "./settings.json"
        self.settings = self.getSettings()

        self.timeBetweenFrames = 1 / self.settings["FPS"]
        self.timeNextFrame = time.time()
        self.currentColor = 0   # This is needed to loop though colors if random colors is not used.

        self.tk = tk.Tk()
        self.tk.title("DAK_scriptet")
        self.tk.attributes("-fullscreen", True)
        self.tk.config(cursor="none")
        self.canvas = tk.Canvas(self.tk, highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=1)
        self.tk.bind("<Escape>", self.quit)

        self.canvas.config(bg="#FF0000")

    def changeColor(self):
        self.canvas.config(bg="#0000FF")

    def setStandardSettings(self):
        # Standard settings.
        settings = {
            "FPS": 5,
            "randomColors": False,
            "colors": [
                "#ff0000",
                "#00ff00",
                "#0000ff"
            ]
        }
        # Write to file.
        with open(self.settingsJSONPath, "w") as f:
            f.write(json.dumps(settings, indent=2))

    def getSettings(self, asString=False):
        settings = None

        if os.path.isfile(self.settingsJSONPath) is False:
            self.setStandardSettings()

        # Read file.
        with open(self.settingsJSONPath, "r") as f:
            settings = json.loads(f.read())

        return settings

    def quit(self, event=None):
        self.tk.destroy()

if __name__ == '__main__':
    window = DAKScreen()
    while True:
        window.tk.update_idletasks()
        window.tk.update()
        if (time.time() > window.timeNextFrame):
            window.changeColor()
            window.timeNextFrame = time.time() + window.timeBetweenFrames
