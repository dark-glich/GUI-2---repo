from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.configure(bg="white")
name = "facebook"
root.title("my image viewer")
root.iconbitmap("icon.ico")

my_image1 = ImageTk.PhotoImage(Image.open("facebook.png"))
my_image2 = ImageTk.PhotoImage(Image.open("instagram.png"))
my_image3 = ImageTk.PhotoImage(Image.open("twitter.png"))
my_image4 = ImageTk.PhotoImage(Image.open("youtube.png"))
my_image5 = ImageTk.PhotoImage(Image.open("whatsapp.png"))
my_image6 = ImageTk.PhotoImage(Image.open("brands-and-logotypes (1).png"))
my_image7 = ImageTk.PhotoImage(Image.open("paypal.png"))

my_list = [my_image1, my_image2, my_image3, my_image4, my_image5, my_image6, my_image7]

label_10 = Label(image=my_image1, text="bilal")
label_10.grid(row=0, column=0, columnspan=3)

label_1 = Label(bd=2, relief=SUNKEN, anchor=E,
                text="image " + str(1) + " of " + str(len(my_list)))

label_1.grid(row=4, column=0, columnspan=3, sticky=EW)


def forard(num):
    global label_10, forward_button, back_button, label_1, name
    label_10.grid_forget()
    label_10 = Label(image=my_list[num + 1])
    forward_button = Button(root, text=">>", command=lambda: forard(num + 1))
    back_button = Button(root, text="<<", command=lambda: forard(num - 1))
    number = num
    label_10.grid(row=0, column=0, columnspan=3)
    forward_button.grid(row=1, column=2)
    back_button.grid(row=1, column=0)
    label_1 = Label(bd=2, relief=SUNKEN, anchor=E,
                    text="image " + str(number + 2) + " of " + str(len(my_list)))

    label_1.grid(row=4, column=0, columnspan=3, sticky=EW)

    if num == 5:
        forward_button = Button(root, text=">>", state=DISABLED)
        forward_button.grid(row=1, column=2)
    if num == -1:
        back_button = Button(root, text="<<", state=DISABLED)
        back_button.grid(row=1, column=0)


exit_button = Button(root, text="EXIT PROGRAM", command=root.quit)
exit_button.grid(row=1, column=1)

forward_button = Button(root, text=">>", command=lambda: forard(0))
forward_button.grid(row=1, column=2)
back_button = Button(root, text="<<")
back_button.grid(row=1, column=0)
root.mainloop()
