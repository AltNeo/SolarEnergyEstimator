from tkinter import *
from tkinter import messagebox
from mainSP import *

root = Tk() # generating the window
root.title("Solar Power Generation Estimator") # this will appear in the title bar 

# our own icon for the window
root.iconbitmap('solar-estimation_logo.ico')

label1 = Label(root, text="Hello!", fg="red").pack()
label2 = Label(root, text="My name is SolarBot!\nI can determine the total solar energy you can harvest \n& how much you can earn with the surplus.\n", fg="green").pack()

# creating a frame for location input
frame = LabelFrame(root, text="Tell us your location", padx=15, pady=15)
frame.pack(padx=15, pady=15)

# creating a tkinter string variable for the radio buttons
r = StringVar()
r.set("This location") # setting a default value

def clickedRadio(value):
    label = Label(root, text=value)
    #label.pack()
    return label

# creating 2 radio buttons
r1 = Radiobutton(frame, text="Use current address", variable=r, value="This location", command= lambda: clickedRadio(r.get()))
r1.grid(row=0, column=0)
r2 = Radiobutton(frame, text="Use other address", variable=r, value="Other location", command= lambda: clickedRadio(r.get()))
r2.grid(row=0, column=3)


# creating a tkinter string variable for the drop-down menu
clickedDrop = StringVar()
clickedDrop.set("Select location")

# list of all the states & union territories of India
options = ["Andaman and Nicobar", "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chandigarh", "Chhattisgarh", "Dadra and Nagar Haveli", "Daman and Diu", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jammu and Kashmir", "Jharkhand", "Karnataka", "Kerala", "Lakshadweep", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "NCT of Delhi", "Odisha", "Puducherry", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal"]

# creating the drop-down menu
drop = OptionMenu(frame, clickedDrop, *options)
drop.grid(row=1, column=1, padx=15, pady=10) 

# function to handle clicking of showLocation button
def show():
    myLabel = Label(frame, text=clickedDrop.get()).grid(column=1)

# button to show the selected location
showLocation = Button(frame, text="Show selected location", command=show, padx=10, pady=5).grid(row=2, column=1)


areaLabel = Label(root, text= "Enter area you wish to apply solar panels to (in meter square):").pack()
# taking input of solar panels' area
e = Entry(root, width=70)
e.pack()
e.get() # getting the input

# a label in the middle
myLabel1 = Label(root, text="").pack()


# function for the popup that will show the analysed data
def popup():
    # formulas & variables
    global area_input
    area_input=int(e.get())
    global power
    power=float(s4)*int(area_input)*10*0.7
    global powerleft
    powerleft=int(power)-206
    global energyThatCanBeProd
    energyThatCanBeProd = "Energy that can be produced at your location: " + str(s4) + " kWh/ sq meter\n"
    global output1
    output1 = "Calculations are done considering that your location gets 10 Hrs of sunlight and a power conversion factor of 0.7\n" + "Total Energy Produced in one day= " + str(power) + " kWh\n" + "An average household consumes 206 KWh per day (according to statista.com , refer to documentation for more info)"
    global output2
    output2 = "After household consumption, energy left= " + str(power-206) + " kWh\n" + "This much energy is enough to run a fan and a lightbulb for " + str((powerleft*1000)/100) + " hrs\n" + "Or at rate of ₹3 per unit buyback offered by the government, you can earn ₹" + str(powerleft*3) + " per day\n" + "Or ₹" + str(powerleft*90) + " per month"

    messagebox.showinfo("Solar Energy Harvest Analysis", energyThatCanBeProd+output1+output2)

# submit button that will, on clicking, show the analysed data popup
submitButton = Button(root, text="Enter", command=popup, padx=15, pady=5, bg="yellow").pack()

# a label in the middle
myLabel2 = Label(root, text="\n").pack()


# creating a button in our root window with text "Exit Program" and quit command
button_quit = Button(root, text = "Exit Program", command = root.quit)
button_quit.pack() # pack the button

root.mainloop()