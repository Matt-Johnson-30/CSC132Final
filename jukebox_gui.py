# imports our window stuff
from Tkinter import *
# imports listdir function, which lists all files in a folder
import os

# width and height of our window
WIDTH = 800
HEIGHT = 600

print "line 10"

### BUTTON FUNCTIONS
def Skip():
    s = 'Skipping current song...'
    os.system("curl -G -d 'song=' -d 'function={}' 192.168.0.130:5000".format("skip"))
    text.insert(END, s + '\n')
    text.see(END)

def Pause():
    s = 'Pausing current song'
    os.system("curl -G -d 'song=' -d 'function={}' 192.168.0.130:5000".format("pause"))
    text.insert(END, s + '\n')
    text.see(END)

def Unpause():
    s = 'Unpausing song'
    os.system("curl -G -d 'song=' -d 'function={}' 192.168.0.130:5000".format("play"))
    text.insert(END, s + '\n')
    text.see(END)


# # # initialization
ButtonFunc = {1: "Skip", 2:"Pause", 3:"Unpause", 4:"Extra", 5:"Extra"}
ButtonNames = {1:"Skip", 2:"Pause", 3:"Unpause", 4:"Extra", 5:"Extra"}

print "starting Jukebox class"
# this is a class that describes our window
# it inherits from Tk class, which is a basic window
class Jukebox(Tk):

        # this function creates our Jukebox window
        def __init__(self):

                # pass creation on to basic window, we will modify it in the next steps
                Tk.__init__(self)
                # set the WIDTH and HEIGHT of our jukebox window
                self.geometry("{}x{}".format(WIDTH, HEIGHT))
                # set the title to whatever we want, this will show at the top of the jukebox window
                self.title("CSC 132 Jukebox")
                # this is a background square that will cover the back of the whole window
                frame = Frame(self, bg="pink")
                # add it to the jukebox so that it fills the whole window like we want
                # without this, it would just be a square that doesnt fill the window
                frame.pack(fill=BOTH, expand=1)

                # this is a label, which contains the name of the current song playing
                self.titleLabel = Label(frame, bg="pink", text="placeholder")
                # add the label as a child of the frame background
                self.titleLabel.pack(side=BOTTOM)

                # add another label that we don't care about that just says "CURRENT SONG:"
                Label(frame, bg="pink", text="SUCCESSFULLY QUEUED SONG").pack(side=BOTTOM)

                # list all of our songs in the songs folder and store it in a variable
                self.files = os.listdir("./songs")
                # we will use this dropDownOption variable to keep track of which song we select to play
                # when we select the song from the drop down menu, the name of the song will be put into this variable
                # when we first create this variable, we will set it to the first song in the list
                self.dropDownOption = StringVar(self, self.files[0])

                # this is the actual drop down menu
                # we will put it inside of the parent pink background "frame" variable
                # we will set the default option to whatever we put into the dropDownOption variable
                # this will allow us to know which song we picked from the menu
                # lastly, we add all of the songs in the list of songs as options
                # OptionMenu(<parent_widget>, <selection_storage_variable>, <menu_option>)
                self.dropDown = OptionMenu(frame, self.dropDownOption, *self.files)
                # then we add it to the pink background
                self.dropDown.pack(side=TOP)

                # this button will load the file that we selected in the drop down menu and eventually play the song
                # the first argument is the parent widget
                # the second argument says we set the text of the button to "Load"
                # the third argument tells the button what to do when we click it, which to to load the file that we currently
                # selected in the drop down menu
                self.loadButton = Button(frame, text="Queue", command=lambda: self.loadFile(self.dropDownOption.get()))
                self.loadButton.pack(side=TOP)

                # load and start the first song
                self.loadFile(self.dropDownOption.get())

        # set the text of the title label
        def setTitle(self, title):
                self.titleLabel["text"] = title

        # loads the file we selected in the drop down menu and updates the title label
        def loadFile(self, name):
                self.setTitle(name)
                os.system("curl -G -d 'song={}' 192.168.0.130:5000".format(name.replace(" ", "_")))
                
print "Finished Jukebox class"

# # # callback function
def CallBack(id, tex):
    return lambda : Out(id)


# # # what callback returns
def Out(id):
    print "Started button functions"
    if(ButtonFunc[id] == "Skip"):
        Skip()
        print "Finished 'Skip'"
    elif(ButtonFunc[id] == "Pause"):
        Pause()
        print "Finished 'Pause'"
    elif(ButtonFunc[id] == "Unpause"):
        Unpause()
        print "Finished 'Unpause'"
    text.insert(END, s)
    text.see(END)
    


print "finished declaring functions"

# # # window
jukebox = Jukebox()
jukebox.configure(bg="pink")
text = Text(master=jukebox)
text.pack(side=RIGHT)
bop = Frame(bg="pink")
bop.pack(side=LEFT)
for k in range(1,4):
        b = Button(bop, text=ButtonNames[k], command=CallBack(k, text))
        b.pack()
        
print "finished with the window initialization"

# # # Welcome (is below everything because of initialization)
text.insert(END, "Welcome to our music player!\n")

Button(bop, text='Exit', command=jukebox.destroy).pack()
jukebox.mainloop()
print "finished with all code: closing program"

while True:
    print "bleeeh"
