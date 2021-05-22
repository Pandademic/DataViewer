# import the library
from appJar import gui
# create a GUI variable called app
app = gui("Login Window", "400x200")
app.setBg("orange")
app.setFont(18)
app.setIcon("test.jpg")
# add & configure widgets - widgets get a name, to help referencing them later
def press(button):
    if button == "Cancel":
        app.stop()
    else:
        usr = app.getEntry("Username")
        pwd = app.getEntry("Password")
        print("User:", usr, "Pass:", pwd)
app.addLabel("title", "Welcome to appJar")
app.setLabelBg("title", "red")
app.addLabelEntry("Username")
app.addLabelSecretEntry("Password")
app.addButtons(["Submit", "Cancel"], press)


app.go()
