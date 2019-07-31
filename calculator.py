# Ben Ryan
# Simple four function calculator

import tkinter
from tkinter import *
tk = tkinter.Tk()

#few global variables to make things easily accessible between classes/functions
num1 = ''
num2 = ''
operator = ''
ans = ''
display = ''

#calculator class for the actual calculations to take place
class Calculator:

    def multiply(self, x, y): return x * y

    def divide(self, x, y): return x / y

    def add(self, x, y): return x + y

    def subtract(self, x, y): return x - y


#gui class to handle buttons, labels etc
#using a grid layout
class GraphicalUserInterface:

    def drawWindow(self):
        tk.title("Calculator")
		
		#not resizable
        tk.resizable(0,0)
    
		#text box for display
		#row 1
        t1 = Text(tk, height=6, width=45, state = DISABLED)
        t1.grid(row=0, column = 0, columnspan = 4, rowspan=1)
		
		#setting the global display variable to the text box so I can access it and update from outside this class
        global display
        display = t1
		
		#labels for buttons in grid
        labels = ['7', '8', '9', '/', '4', '5', '6', 'x', '1', '2', '3', '-', 'cl', '0', '=', '+']
		
		#for iterating over labels list
        count = 0
		
		#for creating grid of 16 buttons, 4 rows, 4 cols
        for r in range(1, 5):
            for c in range(0,4):

				#getting value so we can add op to the operators so they are easily identifiable later
                val = labels[count]
                val2 = val

                if not val.isnumeric() and val != 'cl' and val != '=':
                    val2 = 'op' + val

				#create buttons, link them individually to the eventhandler function
                Button(tk, text = val, command=lambda val2 = val2: eventHandler(val2), height = 6, width = 12).grid(row = r, column = c)
                count += 1			
				
#handles all button clicks				
def eventHandler(id):
    global num1, num2, operator, ans
	
    msg = ''
	
	#if a number is pressed and no operator has been chosen num1 is still being input
    if id.isnumeric() and operator == '':
        num1 += id
	#if a number is pressed and an operator has been set num2 is being input
    elif id.isnumeric() and operator != '':
        num2 += id
	#if clear is pressed reset all variables
    elif id == 'cl':
        num1 = ''
        num2 = ''
        operator = ''
        ans = ''
	#if the id of the pressed button begins with op it is an operator
    elif id.startswith('op') and operator == '':
        operator = id
	#if equals is pressed
    elif id == "=":
		#check if trying to divide by 0
        if num2 == '0' and operator == 'op/':
            msg = "Can't divide by 0"
            num2 = ''
		#check if all required variables are filled in
        elif num1 == '' or num2 == '' or operator == '':
            msg = "Not Valid"
		#if all is ok execute the calculation and reset variables (num1 is set to ans)
        else:
            execute()
            num1 = str(ans)
            num2 = ''
            operator = ''
            ans = ''
			
	#update the display each time a button is clicked
    updateDisplay(msg)

def updateDisplay(msg):
	#make text box editable
    display.config(state = "normal")
	#clear contents
    display.delete('1.0', END)

	#if msg is empty display the caclulation
    if msg == '':
        display.insert(INSERT, num1 + " " + str(operator)[2:] + " " + num2)
    #otherwise display the msg
    else:
        display.insert(INSERT, msg)
		
	#disable the text box so the user can't edit it
    display.config(state = "disabled")

def execute():
	#get calculator
    calc = Calculator()
    global ans, num1, num2
	
	#convert to floats for calcuation
    x = float(num1)
    y = float(num2)
	
	#find ans
    if(operator == 'op/'):
        ans = calc.divide(x, y)
    elif(operator == 'opx'):
        ans = calc.multiply(x, y)
    elif(operator == 'op-'):
        ans = calc.subtract(x, y)
    elif(operator == 'op+'):
        ans = calc.add(x, y)

def main():
    gui = GraphicalUserInterface()
    gui.drawWindow()
    return 0


main()
tk.mainloop()
