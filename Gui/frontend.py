#ManageCal FrontEnd 
"""
A small poorly implemented GUI for task management and calendar scheduling of daily tasks.
Working Alpha
"""



__version__ = '0.0.1'
__author__ = 'Aditya Kulkarni'

#Using Tkinter
from tkinter import *
#to import image files in normal formats
from PIL import ImageTk, Image
#importing databases stuff
import sqlite3
#fonts
import tkinter.font as tkFont


# Here, we are creating our class, Window, and inheriting from the Frame
# class. Frame is a class from the tkinter module. (see Lib/tkinter/__init__)
class Window(Frame):

    # Define settings upon initialization. Here you can specify
    def __init__(self, master=None):
        
        # parameters that you want to send through the Frame class. 
        Frame.__init__(self, master)   

        #reference to the master widget, which is the tk window                 
        self.master = master

        #with that, we want to then run init_window, which doesn't yet exist
        self.init_window()

    #Creation of init_window
    def init_window(self):

        # changing the title of our master widget      
        self.master.title("ManageCal")

        # changing the Logo icon
        self.master.iconbitmap('D:\Programming\Projects\ManageCal\Scheduler\Gui\managecal_image_bly_icon.ico')

        #HAVE TO IMPLEMENT: Scrollbar
        #scrollbar
        #scrollbar = Scrollbar(root)
        #scrollbar.grid(row = 10, column = 0,sticky = E)

        # allowing the widget to take the full space of the root window
#        self.grid(row = 0 , column = 0)

        # creating a menu instance
        menu = Menu(self.master)
        self.master.config(menu=menu)

        # create the file object)
        file = Menu(menu)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        file.add_command(label="Exit", command=self.client_exit)

        #added "file" to our menu
        menu.add_cascade(label="File", menu=file)

        # create the file object)
        edit = Menu(menu)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        edit.add_command(label="Undo")

        #added "file" to our menu
        menu.add_cascade(label="Edit", menu=edit)

        #Creating mainWindow
        mainWindow = LabelFrame(self.master, text ="List of tasks with deadlines", padx = 10, pady= 10, borderwidth = 2, bg= "white", labelanchor = N)
        mainWindow.grid(row = 2, column = 1, columnspan = 99)



    #Main Tabs
        #Courses
        def openCourses():
            c = Button(mainWindow, text="list of courses will open here", command= lambda: c.grid_remove())
            c.grid(row = 0, column = 0)

        tabButton = Button(self.master, text="Courses",pady = 10, bg= "red", fg= "white",command = openCourses, font = tkFont.Font(family="Verdana", size= 10))
        tabButton.grid(row=1,column=1)

        #Events
        def openEvents():
            c = Button(mainWindow, text="list of events will open here", padx = 13, command= lambda: c.grid_remove() )
            c.grid(row = 1, column = 0)

        tabButton = Button(self.master, text="Events",pady = 10, bg= "red", fg= "white",command = openEvents, font = tkFont.Font(family="Verdana", size= 10))
        tabButton.grid(row=1,column=2)
        #Others
        def openOthers():
            c = Button(mainWindow, text="list of other things will open here", padx = 13, command= lambda: c.grid_remove() )
            c.grid(row = 2, column = 0)
            

        tabButton = Button(self.master, text="Others",pady = 10, bg= "red", fg= "white",command = openOthers, font = tkFont.Font(family="Verdana", size= 10))
        tabButton.grid(row=1,column=3)
        #Add

        
        def openAdd():
            c = Button(mainWindow, text="you can add other title tab names here", padx = 13, command= lambda: c.grid_remove() )
            c.grid(row= 3, column = 0)
        photo = PhotoImage(file='add-icon.png')
        smaller_image = photo.subsample(8, 10)
        label = Label(image=smaller_image)
        label.image = smaller_image

        tabButton = Button(self.master, image = smaller_image,pady = 10,command = openAdd)
        tabButton.grid(row=1,column=4)
        #Calender View Button on the last
        def print_hello():
            top2 = Toplevel()
            labelCal = Label(top2, text="insert calender API here")
            labelCal.grid(row=0, column= 0)
            print('hello this is cal view stuff')
        myButton = Button(self.master, text="Cal View",pady = 10,command = print_hello, bg= "pink", fg= "blue")
        myButton.grid(row=0,column=100)

        
        #New button
        def new():
            top2 = Toplevel()
            labelNew = Label(top2, text= "New tasks are added through here. \n Don't know if we want to make it a new window or something else")
            labelNew.grid(row= 0, column = 0)
        myButton = Button(self.master, text="New",pady = 10,command = new, bg= "pink", fg= "blue")
        myButton.grid(row=0,column=0)

        #Exit Button
        buttonExit = Button(self.master, text="Exit Program", command = root.quit)
        buttonExit.grid(row = 400,column = 400)

        ##toolbar
        toolbar = Frame(self.master, bg= "blue")
        insertButt = Button(toolbar, text= "Insert Image")
        insertButt.grid(sticky = W, padx = 2, pady = 2)
        printButt = Button(toolbar , text= "Print")
        printButt.grid(sticky = W, padx = 2, pady = 2 )


    
    def client_exit(self):
        exit()

        
# root window created. Here, that would be the only window, but
# you can later have windows within windows.
root = Tk()

#size of root
width_value = root.winfo_screenwidth()
height_value = root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (width_value, height_value))

#creation of an instance
app = Window(root)

#mainloop 
root.mainloop()  




'EVERYTHING AFTER THIS IS THINGS THAT WILL BE INTEGRATED LATER'


#creating function for radio buttons
def clicked(r_value):
    Label_r = Label(root, text = r_value)
    Label_r.grid(row = 1, column = 0)


#Creating a slider
h = Scale(root, from_ = 0, to = 25, orient = HORIZONTAL)
#h.grid(row = 6, column = 1)

my_label = Label(root, text = h.get())
#my_label.grid(row = 2, column = 2)

def slide():
    my_label = Label(root, text = h.get())
    my_label.grid(row = 2, column = 2)

my_btn = Button(root, text = "Slider click ", command = slide)
#my_btn.grid(row = 2, column = 5)



#Checkboxes
#var = StringVar()
#c = Checkbutton(root, text = "Check to select course", variable = var, onvalue = "on", offvalue = "off")
#c.deselect() #to curb the glitch of starting with tick chekced
#c.grid(row = 9, column = 1)


def click():
    label3 = Label(root, text = var.get())
    label3.grid(row = 5, column = 2)
b = Button(root, text = "Checkbox button", command = click)
#b.grid(row = 3, column =3 )

#DropDown Boxes 
#def show():
#    LabelDrop = Label(root,text= clicked.get())
#    LabelDrop.grid(row = 3, column = 6)

options = [
    "Classes", "Events", "Meetings", "Other"
]

#clicked = StringVar()
#clicked.set(options[0])
#drop = OptionMenu(root, clicked, *options)
#drop.grid(row = 2, column = 6)

#ButtonDrop = Button(root, text="SHow selection", command = show)
#ButtonDrop.grid(row = 4, column = 6)


#Databases using JSON

'''
c.execute("""CREATE TABLE address (
    first_name text, 
    last_name text,
    address text,
    city text,
    state text,
    zipcode integer)
""")
'''


#creating submit function for db
def submit():
    #creating or connecting to a database
    conn = sqlite3.connect('address_book.db')


    c = conn.cursor()   #creating cursor

    #insert into table
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
        { 
            'f_name': f_name.get(), 
            'city': city.get(),
            'l_name': l_name.get(),
            'address': address.get(),
            'state': state.get(),
            'zipcode': zipcode.get()
        })

    #clear the text boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)


#create query function
def query():
    conn = sqlite3.connect('address_book.db')
    c =conn.cursor()
    c.execute("SELECT *,oid FROM addresses")
    fetchvar = c.fetchall()
    #print(fetchvar)

    #loop through results
    print_records = ''
    for record in fetchvar:
        print_records += str(fetchvar[0]) + "\n" 

    query_label = Label(root, text = print_records)
 #   query_label.grid(row = 9, column = 0, columnspan = 2)

f_name = Entry(root, width = 30)
#f_name.grid(row = 2,column = 9, padx = 20)

l_name = Entry(root, width = 30)
#l_name.grid(row = 4,column = 9, padx = 20)

address = Entry(root, width = 30)
#address.grid(row = 5,column = 9, padx = 20)

city = Entry(root, width = 30)
#city.grid(row = 6,column = 9, padx = 20)

state = Entry(root, width = 30)
#state.grid(row = 7,column = 9, padx = 20)

zipcode = Entry(root, width = 30)
#zipcode.grid(row = 8,column = 9, padx = 20)

#creating text box labels

f_name_label = Label(root, text= "First name")
#f_name_label.grid(row = 2,column  = 8)

l_name_label = Label(root, text= "Last name")
#l_name_label.grid(row = 3,column  = 8)

address_label = Label(root, text= "Address name")
#address_label.grid(row = 4,column  = 8)

city_label = Label(root, text= "City name")
#city_label.grid(row = 5,column  = 8)

state_label = Label(root, text= "State name")
#state_label.grid(row = 6,column  = 8)

zip_label = Label(root, text= "Zip code")
#zip_label.grid(row = 7,column  = 8)

#Create submit button for db

submit_btn = Button(root, text = "Add record to db", command= submit)
#submit_btn.grid(row = 8, column = 7, columnspan = 2, pady = 10, padx = 10,ipadx= 100)

#Creating query button
query_btn = Button(root, text = "Show records", command= query)
#query_btn.grid(row = 9, column =7, columnspan = 2, pady = 10, padx = 10, ipadx = 137)



#conn.commit()       #commiting changes

#conn.close          #close connection



