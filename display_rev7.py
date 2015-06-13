#Trying to do it using canvas and multithreading, but can't get it to update the variable.

import Tkinter as tk
from Tkinter import *
from PIL import Image
import threading
import time

variable = 1
class App(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.start()

    def callback(self):
        self.root.quit()

    def run(self):
        self.root = tk.Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.callback)

	self.canvas = Canvas(self.root, width=600, height=600)
	self.canvas.grid(row=0, column=0)
	self.my_images = []
	self.my_images.append(PhotoImage(file = "1.png"))
	self.my_images.append(PhotoImage(file = "2.png"))
	self.my_images.append(PhotoImage(file = "3.png"))
	self.my_image_number = variable

        self.image_on_canvas = self.canvas.create_image(0, 0, anchor = NW, image = self.my_images[self.my_image_number])
	
#	self.canvas.update()
        self.root.mainloop()

app = App()

for i in range(3):
    time.sleep(1)
    print(i)
    variable+=1
