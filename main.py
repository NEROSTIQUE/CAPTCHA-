

from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox


def close():
    root.destroy()


# creating tkinter window
root = Tk()
root.title("Recaptcha Solve Gui")
root.geometry("410x500")
# Adding widgets to the root window
image = Image.open("cake5-small.png")
photo = ImageTk.PhotoImage(image)

label = Label(root, image=photo)
label.image = photo
label.grid(row=0, rowspan=2, column=0, columnspan=2)

label2 = Label(root, text="Select all images with", font=('Helvetica 13'))
label3 = Label(root, text="birthday cake", font=('Helvetica 13 bold'))
label2.grid(row=0, column=2, columnspan=2, pady=0)
label3.grid(row=1, column=2, columnspan=2, pady=0)

image2 = Image.open("recaptcha.png")
photo2 = ImageTk.PhotoImage(image2)

label4 = Label(root, image=photo2)
label4.image = photo2
label4.grid(row=0, rowspan=2, column=4, columnspan=2)

# Creating a photoimage object to use image
photo1 = PhotoImage(file=r"cake1.png")
photo2 = PhotoImage(file=r"cake2.png")
photo3 = PhotoImage(file=r"stone1.png")
photo4 = PhotoImage(file=r"stone2.png")
photo5 = PhotoImage(file=r"cake5.png")
photo6 = PhotoImage(file=r"cake6.png")
photo7 = PhotoImage(file=r"cake7.png")
photo8 = PhotoImage(file=r"stone3.png")
photo9 = PhotoImage(file=r"cake9.png")

# here, image option is used to
# set image on button
bvar1 = BooleanVar()
bvar2 = BooleanVar()
bvar3 = BooleanVar()
bvar4 = BooleanVar()
bvar5 = BooleanVar()
bvar6 = BooleanVar()
bvar7 = BooleanVar()
bvar8 = BooleanVar()
bvar9 = BooleanVar()
btn1 = Checkbutton(root, variable=bvar1, text='Click Me!', image=photo1,
                   onvalue=True, offvalue=False)
btn2 = Checkbutton(root, variable=bvar2, text='Click Me!', image=photo2,
                   onvalue=True, offvalue=False)
btn3 = Checkbutton(root, variable=bvar3, text='Click Me!', image=photo3,
                   onvalue=True, offvalue=False)


btn1.grid(row=2, column=0, columnspan=2)
btn2.grid(row=2, column=2, columnspan=2)
btn3.grid(row=2, column=4, columnspan=2)


btn4 = Checkbutton(root, variable=bvar4, text='Click Me!', image=photo4,
                   onvalue=True, offvalue=False)
btn5 = Checkbutton(root, variable=bvar5, text='Click Me!', image=photo5,
                   onvalue=True, offvalue=False)
btn6 = Checkbutton(root, variable=bvar6, text='Click Me!', image=photo6,
                   onvalue=True, offvalue=False)

btn4.grid(row=3, column=0, columnspan=2)
btn5.grid(row=3, column=2, columnspan=2)
btn6.grid(row=3, column=4, columnspan=2)


btn7 = Checkbutton(root, variable=bvar7, text='Click Me!', image=photo7,
                   onvalue=True, offvalue=False)
btn8 = Checkbutton(root, variable=bvar8, text='Click Me!', image=photo8,
                   onvalue=True, offvalue=False)
btn9 = Checkbutton(root, variable=bvar9, text='Click Me!', image=photo9,
                   onvalue=True, offvalue=False)

btn7.grid(row=4, column=0, columnspan=2)
btn8.grid(row=4, column=2, columnspan=2)
btn9.grid(row=4, column=4, columnspan=2)


def verify():
    v = [bvar1.get(), bvar2.get(), bvar3.get(), bvar4.get(), bvar5.get(),
         bvar6.get(), bvar7.get(), bvar8.get(), bvar9.get()]
    if (v[2] == False and v[3] == False and v[7] == False):
        if v[0] == True and v[1] == True and v[4] == True and v[5] == True and v[6] == True and v[8] == True:
            messagebox.showinfo(title="Successful!! Captcha Solved",
                                message="You have passed the Captcha Succesfully!")
            close()
        else:
            messagebox.showerror(
                "Error Occured", "Select all the images with Birthday Cake")

    else:
        messagebox.showerror(
            "Error Occured", "Select all the images with Birthday Cake Only")


btnverify = Button(root, text="VERIFY",
                   background='#3765b0', width=20, height=2, command=verify)
btnverify.grid(row=5, column=3, columnspan=3, pady=10)


mainloop()
