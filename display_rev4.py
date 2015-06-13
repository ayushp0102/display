#This thing works perfectly using the buttons I created. I just need to find a way to call the
#button functions outside the class MainWindows(). Then I could multithread it and call it whenever required.

from Tkinter import *
from PIL import Image
import time
#----------------------------------------------------------------------

first=Image.open("1.png")
second=Image.open("2.png")
new_image=Image.open("1.png")
class MainWindow():

    #----------------
	def __init__(self, main):
        # canvas for image
		self.canvas = Canvas(main, width=600, height=600)
		self.canvas.grid(row=0, column=0)

        # images
	        self.my_images = []
	        self.my_images.append(PhotoImage(file = "1.png"))
	        self.my_images.append(PhotoImage(file = "2.png"))
	        self.my_images.append(PhotoImage(file = "3.png"))
	        self.my_image_number = 0

        # set first image on canvas
	        self.image_on_canvas = self.canvas.create_image(0, 0, anchor = NW, image = self.my_images[self.my_image_number])

        # button to change image
	        self.button = Button(main, text="Change", command=self.onButton)
	        self.button.grid(row=1, column=0)

	        self.button2 = Button(main, text="Change", command=self.onButton2)
	        self.button2.grid(row=2, column=0)

	        self.button3 = Button(main, text="Change", command=self.onButton3)
	        self.button3.grid(row=3, column=0)

    #----------------

	def onButton(self):

        # next image
	        self.my_image_number = 0
        # change image
	        self.canvas.itemconfig(self.image_on_canvas, image = self.my_images[self.my_image_number])

    #----------------

	def onButton2(self):

        # next image
	        self.my_image_number = 1
        # change image
	        self.canvas.itemconfig(self.image_on_canvas, image = self.my_images[self.my_image_number])

    #----------------

	def onButton3(self):

        # next image
	        self.my_image_number = 2
        # change image
	        self.canvas.itemconfig(self.image_on_canvas, image = 	self.my_images[self.my_image_number])
	#-----------------

#----------------------------------------------------------------------
#def task():
	#time.sleep(1)
	#window.onButton3
	#root.update()
	#time.sleep(1)
	#window.onButton2
#	root.update()

root = Tk()
window=MainWindow(root)
root.mainloop()
#while True:
#	task()
