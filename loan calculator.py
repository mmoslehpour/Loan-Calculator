#Mina Moslehpour
#1020241
#hw5-3
#Use Program set 2 codes and use tkinter module to create a GUI program for the Loan program

from tkinter import *
import tkinter.messagebox
import tkinter.simpledialog

window=Tk() #creates window
window.title("Loan Calculator") #sets the window title

Label(window, text="Annual Interest Rate: ").grid(row=0) #creates the label and grid is alignment
Label(window, text="Number of Years: ").grid(row=1) 
Label(window, text="Loan Amount: ").grid(row=2)

Label(window, text="Monthly Payment: ").grid(row=3)
Label(window, text="Total Payment: ").grid(row=4)

box1=Entry(window,justify=RIGHT) #creates text box to enter info
box1.grid(row=0, column=1)

box2=Entry(window,justify=RIGHT)
box2.grid(row=1, column=1)

box3=Entry(window,justify=RIGHT)
box3.grid(row=2, column=1)

def calc():
    intRate=float(e1.get()) #gets values in text boxes 
    numYears=float(e2.get())   
    loanAmount=float(e3.get())
    monthlyIntRate=intRate/1200   
    monthlyPayment=loanAmount*monthlyIntRate/(1-(1/(1+monthlyIntRate)**(numYears*12))) 
    totalPayment=monthlyPayment*numYears*12 #calculates the total payment
    output1 =str(round(monthlyPayment,2))
    output2 =str(round(totalPayment,2))
    labelMonthPay=Label(window,text = output1).grid(row=3, column=1,sticky=E) #creates two new labels to print details
    labelTotalPay=Label(window,text = output2).grid(row=4, column=1,sticky=E)
    return
  
  

Button(window, text='Compute Payment', command=calc).grid(row=5, column=1, sticky=W, pady=4) 

mainloop()
