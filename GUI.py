# using library
from tkinter import *
from email.message import EmailMessage
import smtplib
import imghdr
from tkinter import ttk
from tkinter import messagebox
from functools import partial
from PIL import Image, ImageTk
from tkinter import filedialog
import os
import csv
import time
import AssignmentGenerator
import cv2
import FaceRecognizer

# key for permanent login
key_of_login = None  # Define key_of_login as a global variable outside any function
private_key_pem = None
public_key_pem = None

# Open the file in read mode and retrieve the user name
if os.path.exists('username.txt') and os.path.exists('userPrivate_key.txt') and os.path.exists('userPublic_key.txt'):
    with open("username.txt", "r") as file:
        key_of_login = file.read()
    with open("userPrivate_key.txt", "r") as file:
        private_key_pem = file.read()
    with open("userPublic_key.txt", "r") as file:
        public_key_pem = file.read()


# create a class
class en_Dec_rypt:

    def __init__(self, root):

        # Setting the Tkinter main window
        self.window = root
        self.window.geometry("900x600+200+100")
        self.window.title('Attendance and Assignment Manager')
        self.window.resizable(False, False)
        self.window.configure(bg="#2f4155")
        # icon
        self.image_icon = PhotoImage(file="images\images\logo_200x200.png")
        self.window.iconphoto(False, self.image_icon)
        # Calling the Home_Page() function
        self.home_page()

    # home page (First open page)
    def home_page(self):
        # call the clear screen Function
        self.ClearScreen()
        col11 = "#70DFED"
        self.window.configure(bg=col11)
        # global key of login
        global key_of_login


        # Encrupt Button
        title_lable = Label(self.window, bg="white", height=3, relief=SUNKEN)
        title_lable.pack(side=TOP, fill=X)
        # logo

        image0= Image.open("images/images/uok-logo.png")
        resized_image0 = image0.resize((50, 50))
        photo0 = ImageTk.PhotoImage(resized_image0)
        # photo=ImageTk.PhotoImage(image)
        label0 = Label(title_lable, image=photo0, bg="#ffffff")
        label0.image = photo0
        label0.place(x=30, y=0)

        Label(title_lable, text="Attendance and Assignment Manager",
              font="arial 20 bold",bg="#ffffff", fg="black").place(x=200, y=2)

        image4 = Image.open("images/images/bg101.png")
        resized_image4 = image4.resize((300, 300))
        photo4 = ImageTk.PhotoImage(resized_image4)

        frame1 = Frame(self.window, width=300, height=300, relief=GROOVE, bg=col11)
        frame1.place(x=100, y=130)

        # photo=ImageTk.PhotoImage(image)
        label4 = Label(frame1, image=photo4, bg=col11)
        label4.image = photo4
        label4.place(x=0, y=0)

        image7 = Image.open("images/images/assignment.png")
        resized_image7 = image7.resize((200, 200))
        photo7 = ImageTk.PhotoImage(resized_image7)
        # photo=ImageTk.PhotoImage(image)
        label7 = Label(frame1, image=photo7, bg="#ffffff")
        label7.image = photo7
        label7.place(x=50, y=5)
        Label(frame1, text="Attendence",
              font="arial 20 bold", fg="black").place(x=70, y=210)

        b5 = Button(frame1, fg="white", bg="#454545", font="Helvetica 13 bold", text="Take",
                    command=self.attendance_system, width=15, height=2)
        b5.place(x=70, y=245)

        frame3 = Frame(self.window, width=300, height=300, relief=GROOVE, bg=col11)
        frame3.place(x=500, y=130)

        label4 = Label(frame3, image=photo4, bg=col11)
        label4.image = photo4
        label4.place(x=0, y=0)

        image8 = Image.open("images/images/immigration.png")
        resized_image8 = image8.resize((200, 200))
        photo8 = ImageTk.PhotoImage(resized_image8)
        # photo=ImageTk.PhotoImage(image)
        label8 = Label(frame3, image=photo8, bg="#ffffff")
        label8.image = photo8
        label8.place(x=50, y=5)
        Label(frame3, text="Assignment",
              font="arial 20 bold", fg="black").place(x=70, y=200)

        b2 = Button(frame3, fg="white", bg="#454545", font="Helvetica 13 bold", text="Genrate",
                    command=self.assignment_generate, width=15, height=2)
        b2.place(x=70, y=245)

        # image1 = Image.open("images/Averda_new.png")
        # resized_image1 = image1.resize((500, 400))
        # photo1 = ImageTk.PhotoImage(resized_image1)
        # # photo=ImageTk.PhotoImage(image1)
        # label = Label(self.window, image=photo1)
        # label.image = photo1
        # label.place(x=50, y=100)

        # about the app
        frame2 = Frame(self.window, bd=6, bg="#454545", width=900, height=100, relief=GROOVE)
        frame2.place(x=0, y=500)

        Label(frame2,
              text="""An attendance system automates tracking student or employee attendance using technologies like face \nrecognition. Assignment generation streamlines creating and distributing tasks, ensuring efficient \nworkload management.""",
              font="arial 12 bold", bg="#454545", fg="white").place(x=10, y=5)


    # Remove all widgets from the Home Page(self.frame)
    def ClearScreen(self):
        for widget in self.window.winfo_children():
            widget.destroy()

    def attendance_system(self):
        self.ClearScreen()
        color = "#70DFED"
        self.window.configure(bg=color)

        # add home button
        ba4 = Button(self.window, text="<-Back", bg="#2f4155", fg="white", font=("Helvetica", 8, 'bold'),
                     command=self.home_page)
        ba4.place(x=10, y=10)

        frame2 = Frame(self.window, bd=6, bg="#454545", width=550, height=400, relief=GROOVE)
        frame2.place(x=50, y=50)

        # image8 = Image.open("images/images/Averda_new.png")
        # resized_image8 = image8.resize((550, 400))
        # photo8 = ImageTk.PhotoImage(resized_image8)
        # label8 = Label(frame2, image=photo8, bg=color)
        # label8.image = photo8
        # label8.place(x=50, y=50)

        frame3 = Frame(self.window, bd=6, bg="#ffffff", width=200, height=200, relief=GROOVE)
        frame3.place(x=650, y=50)
        Label(frame3, text="Detail", font="arial 18 bold", bg="#ffffff", fg="black").place(x=50, y=5)
        Label(frame3, text="ID: 230148", font="arial 12 bold", bg="#ffffff", fg="black").place(x=1, y=50)
        Label(frame3, text="Name: Pratap Singh", font="arial 12 bold", bg="#ffffff", fg="black").place(x=1, y=80)
        Label(frame3, text="Class: MCA 4 Sem.", font="arial 12 bold", bg="#ffffff", fg="black").place(x=1, y=110)

        frame4 = Frame(self.window, bd=6, bg="#454545", width=900, height=100, relief=GROOVE)
        frame4.place(x=0, y=500)

        Label(frame4,
              text="""An attendance system automates tracking student or employee attendance using technologies like face \nrecognition. Assignment generation streamlines creating and distributing tasks, ensuring efficient \nworkload management.""",
              font="arial 12 bold", bg="#454545", fg="white").place(x=10, y=5)

        model_path = 'face_trained.yml'
        labels = ['100', '101']  # Replace with your actual labels
        self.attendance_system = FaceRecognizer.FaceRecognitionAttendance(model_path, labels)
        self.attendance_system.recognize_and_update(frame2)
        #Create a label within frame2 to display the video

    def assignment_generate(self):
        self.ClearScreen()
        color = "#70DFED"  # lite blue
        color2 = "#70DFED"  # dark blue
        self.window.configure(bg=color)

        # Encrypt Button
        title_label = Label(self.window, bg="white", height=3, relief=SUNKEN)
        title_label.pack(side=TOP, fill=X)

        # add home button
        ba4 = Button(title_label, text="<-Back", bg="#2f4155", fg="white", font=("Helvetica", 8, 'bold'),
                     command=self.home_page)
        ba4.place(x=10, y=2)

        # logo
        image1 = Image.open("images/images/assignmentG.png")
        photo1 = ImageTk.PhotoImage(image1)
        label1 = Label(title_label, image=photo1, bg="white")
        label1.image = photo1
        label1.place(x=300, y=0)



        # Inputs
        Label(self.window, text="Enter All Details", bg=color2, fg="black", font=("Game Of Squids", 18, "bold")).place(
            x=350, y=60)
        Label(self.window, text="Class", bg=color2, fg="black", font=("Game Of Squids", 14)).place(
            x=250, y=120)
        # Define a list of options for the combo box
        options1 = ["MCA1", "MCA2", "MCA3"]

        # Create a Tkinter variable to hold the selected option
        self.selected_option1 = StringVar()
        # Create a combo box and assign options to it
        self.combo_box = ttk.Combobox(self.window, textvariable=self.selected_option1, values=options1, width=15)
        self.combo_box.place(x=380, y=120)  # Place the combo box on the window
        self.combo_box.set("Select Class")  # Set default value for the combo box
        Label(self.window, text="Subject", bg=color2, fg="black", font=("Game Of Squids", 14)).place(
            x=250, y=160)

        # Define a list of options for the combo box
        options2 = ["Cloud Computing", "Design and Analysis of Algorithms", "Information and Network Security System",
                    "Programming with JAVA", "Theory of Computation"]

        # Create a Tkinter variable to hold the selected option
        self.selected_option2 = StringVar()
        # Create a combo box and assign options to it
        self.combo_box2 = ttk.Combobox(self.window, textvariable=self.selected_option2, values=options2, width=40)
        self.combo_box2.place(x=380, y=160)  # Place the combo box on the window
        self.combo_box2.set("Select Subject")  # Set default value for the combo box

        Label(self.window, text="Unit", bg=color2, fg="black", font=("Game Of Squids", 14)).place(
            x=250, y=200)

        self.string_input1 = Entry(self.window, width=10)
        self.string_input1.place(x=380, y=200)

        Label(self.window, text="(1,2,3,4,5..)", bg=color2, fg="black", font=("Game Of Squids", 11)).place(
            x=440, y=200)

        Label(self.window, text="Topic", bg=color2, fg="black", font=("Game Of Squids", 14)).place(
            x=250, y=240)

        self.string_input2 = Entry(self.window, width=30)
        self.string_input2.place(x=380, y=240)

        def generate_assignment():
            class_name = self.selected_option1.get()
            subject_name = self.selected_option2.get()
            unit_name = self.string_input1.get()
            topic_name = self.string_input2.get()
            result = AssignmentGenerator.main(class_name, subject_name, unit_name, topic_name)
            print(result)
            return result
            # You can do something with the result here, such as displaying it on a label or printing it

        def twoWay():
            self.result_page(generate_assignment())

        Button(text="Generate Assignment", height=1, width=40, bg="green", fg="black", font="arial 13 bold", bd=3,
               command=twoWay).place(x=230, y=390)

        frame1 = Frame(self.window, bd=6, bg="#454545", width=900, height=100, relief=GROOVE)
        frame1.place(x=0, y=500)

        Label(frame1,
              text="""An attendance system automates tracking student or employee attendance using technologies like face \nrecognition. Assignment generation streamlines creating and distributing tasks, ensuring efficient \nworkload management.""",
              font="arial 12 bold", bg="#454545", fg="white").place(x=5, y=5)

    def result_page(self, result):
        self.ClearScreen()
        color = "#C5D4EC"  # lite blue
        color2 = "#2f4155"  # dark blue
        self.window.configure(bg=color)
        # add home button

        ba10 = Button(self.window, text="<-Back", bg="#2f4155", fg="white", font=("Helvetica", 8, 'bold'),
                      command=self.home_page)
        ba10.place(x=10, y=10)

        Label(self.window, text="Assignment Generated", bg=color, fg="red", font=("Game Of Squids", 20, "bold")).place(
            x=150, y=10)
        Label(self.window, text="--", bg=color, fg="blue", font=("Game Of Squids", 20, "bold")).place(x=10, y=40)
        Label(self.window, text="--", bg=color, fg="orange", font=("Game Of Squids", 20, "bold")).place(x=60, y=40)
        Label(self.window, text="--", bg=color, fg="green", font=("Game Of Squids", 20, "bold")).place(x=110, y=40)
        Label(self.window, text="--", bg=color, fg="red", font=("Game Of Squids", 20, "bold")).place(x=160, y=40)

        frame = Frame(self.window, bg=color2, bd=0, width=700, height=420)
        frame.place(x=0, y=80)

        Label(frame, text="1. Questionq", bg=color2, fg="white", font=("Game Of Squids", 16, "bold")).place(
            x=200, y=5)

        def divide():
            length = len(result)
            midpoint = length // 2
            if length > 70:
                if length % 2 == 0:
                    return result[:midpoint], result[midpoint:]
                else:
                    return result[:midpoint + 1], result[midpoint + 1:]
            else:
                return result, ""

        s1, s2 = divide()
        Label(frame, text=s1 + "\n" + s2, width=65, height=10, font=("times new roman", 14), bd=2,
              bg=color).place(x=20, y=50)

    def audio_file(self):
        self.ClearScreen()
        color = "#C5D4EC"  # lite blue
        color2 = "#2f4155"  # dark blue
        self.window.configure(bg=color)

    def video_file(self):
        self.ClearScreen()
        color = "#C5D4EC"  # lite blue
        color2 = "#2f4155"  # dark blue
        self.window.configure(bg=color)


# The main function
if __name__== "__main__":

    loding_root = Tk()

    # Using piece of code from old splash screen
    width_of_window = 427
    height_of_window = 250
    screen_width = loding_root.winfo_screenwidth()
    screen_height = loding_root.winfo_screenheight()
    x_coordinate = (screen_width / 2) - (width_of_window / 2)
    y_coordinate = (screen_height / 2) - (height_of_window / 2)
    loding_root.geometry("%dx%d+%d+%d" % (width_of_window, height_of_window, x_coordinate, y_coordinate))
    # loding_root.configure(bg='#ED1B76')
    loding_root.overrideredirect(1)  # for hiding titlebar

    Frame(loding_root, width=427, height=250, bg='#272727').place(x=0, y=0)

    if key_of_login == "" or key_of_login == None:  # for without login user
        label1 = Label(loding_root, text='Welcome   To', fg='white', bg='#272727',
                       font=("Game Of Squids", 20, "bold"))  # decorate it
        label1.place(x=80, y=50)
        label2 = Label(loding_root, text='Attendance and Assignment Manager', fg='yellow', bg='#272727',
                       font=("Game Of Squids", 14, "bold"))  # decorate it
        label2.place(x=50, y=100)
        label2 = Label(loding_root, text='You Should Login..', fg='white', bg='#272727',
                       font=("Calibri", 11))  # decorate it
        label2.place(x=300, y=215)

    else:
        label1 = Label(loding_root, text='Welcome To', fg='white', bg='#272727',
                       font=("Game Of Squids", 17, "bold"))  # decorate it
        label1.place(x=50, y=40)
        label2 = Label(loding_root, text='Attendance and Assignment Manager', fg='red', bg='#272727',
                       font=("Game Of Squids", 17, "bold"))  # decorate it
        label2.place(x=217, y=40)
        label3 = Label(loding_root, text='User name - ', fg='white', bg='#272727',
                       font=("Game Of Squids", 12, "bold"))  # decorate it
        label3.place(x=55, y=100)
        label4 = Label(loding_root, text=key_of_login, fg='yellow', bg='#272727',
                       font=("Game Of Squids", 12, "bold"))  # decorate it
        label4.place(x=235, y=100)
        label2 = Label(loding_root, text='You Already Login.', fg='white', bg='#272727',
                       font=("Calibri", 11))  # decorate it
        label2.place(x=300, y=215)

    label2 = Label(loding_root, text='Loading...', fg='white', bg='#272727', font=("Calibri", 11))  # decorate it
    label2.place(x=10, y=215)

    # making animation

    image_a = ImageTk.PhotoImage(Image.open('images/images/c2.png'))
    image_b = ImageTk.PhotoImage(Image.open('images/images/c1.png'))

    for i in range(8):  # 5loops
        dote_a = Label(loding_root, image=image_a, border=0, relief=SUNKEN)
        dote_a.image = image_a
        dote_a.place(x=180, y=160)

        dote_b = Label(loding_root, image=image_b, border=0, relief=SUNKEN)
        dote_b.image = image_b
        dote_b.place(x=200, y=160)
        dote_c = Label(loding_root, image=image_b, border=0, relief=SUNKEN)
        dote_c.image = image_b
        dote_c.place(x=220, y=160)
        dote_d = Label(loding_root, image=image_b, border=0, relief=SUNKEN)
        dote_d.image = image_b
        dote_d.place(x=240, y=160)
        loding_root.update_idletasks()
        time.sleep(0.1)

        dote_a = Label(loding_root, image=image_b, border=0, relief=SUNKEN)
        dote_a.image = image_b
        dote_a.place(x=180, y=160)

        dote_b = Label(loding_root, image=image_a, border=0, relief=SUNKEN)
        dote_b.image = image_a
        dote_b.place(x=200, y=160)
        dote_c = Label(loding_root, image=image_b, border=0, relief=SUNKEN)
        dote_c.image = image_b
        dote_c.place(x=220, y=160)
        dote_d = Label(loding_root, image=image_b, border=0, relief=SUNKEN)
        dote_d.image = image_b
        dote_d.place(x=240, y=160)
        loding_root.update_idletasks()
        time.sleep(0.1)

        dote_a = Label(loding_root, image=image_b, border=0, relief=SUNKEN)
        dote_a.image = image_b
        dote_a.place(x=180, y=160)

        dote_b = Label(loding_root, image=image_b, border=0, relief=SUNKEN)
        dote_b.image = image_b
        dote_b.place(x=200, y=160)
        dote_c = Label(loding_root, image=image_a, border=0, relief=SUNKEN)
        dote_c.image = image_a
        dote_c.place(x=220, y=160)
        dote_d = Label(loding_root, image=image_b, border=0, relief=SUNKEN)
        dote_d.image = image_b
        dote_d.place(x=240, y=160)
        loding_root.update_idletasks()
        time.sleep(0.1)

        dote_a = Label(loding_root, image=image_b, border=0, relief=SUNKEN)
        dote_a.image = image_b
        dote_a.place(x=180, y=160)

        dote_b = Label(loding_root, image=image_b, border=0, relief=SUNKEN)
        dote_b.image = image_b
        dote_b.place(x=200, y=160)
        dote_c = Label(loding_root, image=image_b, border=0, relief=SUNKEN)
        dote_c.image = image_b
        dote_c.place(x=220, y=160)
        dote_d = Label(loding_root, image=image_a, border=0, relief=SUNKEN)
        dote_d.image = image_a
        dote_d.place(x=240, y=160)
        loding_root.update_idletasks()
        time.sleep(0.1)

    loding_root.destroy()
    loding_root.mainloop()

    root = Tk()
    # Creating a 'En_Dec_rypt' class object
    obj = en_Dec_rypt(root)
    root.mainloop()