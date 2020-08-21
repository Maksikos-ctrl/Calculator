from tkinter import *
import math

class Calc():
     def __init__(self):
         self.arithmetic_Operator=""
         self.result = False
         self.check_sum = False
         self.total = 0
         self.current = ""
         self.input_value = True   

     def numberEnter(self, num):
         self.result = False
         firstnum = txtDisplay.get()
         secondnum = str(num)
         if self.input_value:
             self.current = secondnum
             self.input_value = False
         else:
             if secondnum == '.':
                 if secondnum in firstnum:
                     return
             self.current = firstnum + secondnum
         self.display(self.current)

     def sum_of_total(self):
         self.result = True
         self.current = float(self.current) 
         if self.check_sum == True:
             self.valid_function()
         else:
             self.total = float(txtDisplay.get())


     def valid_function(self):
         if self.arithmetic_Operator == "add":
             self.total += self.current
         if self.arithmetic_Operator == "sub":
             self.total -= self.current
         if self.arithmetic_Operator == "multi":
             self.total *= self.current
         if self.arithmetic_Operator == "divide":
             self.total /= self.current
         self.input_value = True
         self.check_sum = False
         self.display(self.total) 

     def operation(self, arithmetic_Operator):
         self.current = float(self.current) 
         if self.check_sum:
             self.valid_function()
         elif not self.result:
             self.total = self.current
             self.input_value = True
         self.check_sum = True
         self.arithmetic_Operator = arithmetic_Operator
         self.result = False                            

     def display(self, value):
         txtDisplay.delete(0, END) 
         txtDisplay.insert(0, value)     


     def Clear_Entry(self): 
         self.result = False   
         self.current = "0"
         self.display(0)
         self.input_value = True

     def Clear_All_Entry(self): 
         self.Clear_Entry() 
         self.total = "0"

     def MathsPM(self): 
         self.result = False   
         self.current = -(float(txtDisplay.get()))
         self.display(self.current)   

     def Square_Root(self): 
         self.result = False   
         self.current = math.sqrt(float(txtDisplay.get()))
         self.display(self.current)         
    

added_value = Calc()
root = Tk()
root.title("PROMAXCALCULATOR")                       
calc = Frame(root)
calc.grid()

txtDisplay = Entry(calc, font = ('arial', 20, 'bold' ), bg="powder blue", bd=20, width=28, justify=RIGHT) 
txtDisplay.grid(row=0, column=0, columnspan=4, pady =1)
txtDisplay.insert(0,"0")
#========================================================================================================
numberpad = "789456123"
i = 0
btn = []
for j in range(2,5):
     for q in range(3):
         btn.append(Button(calc, width=6, height=2,font = ('arial', 20, 'bold' ),  bd=4,text=numberpad[i]))                                   
         btn[i].grid(row = j, column=q, pady=1)
         btn[i] ["command"] = lambda x = numberpad [i]: added_value.numberEnter(x)
         i +=1
#===========================================================================================================================
btnCE=(Button(calc, width=6, height=2,font = ('arial', 20, 'bold' ), bg="powder blue", bd=4,text="CE", command = added_value.Clear_All_Entry)).grid(row = 1, column=0, pady=1)

btnC=(Button(calc, width=6, height=2,font = ('arial', 20, 'bold' ), bg="powder blue", bd=4,text="C", command = added_value.Clear_Entry)).grid(row = 1, column=1, pady=1)

btnSqRoot=(Button(calc, width=6, height=2,font = ('arial', 20, 'bold' ), bg="powder blue", bd=4,text="√", command = added_value.Square_Root)).grid(row = 1, column=2, pady=1)
#=====================================================================================Operators====================================
btnAdd=(Button(calc, width=6, height=2,font = ('arial', 20, 'bold' ), bg="powder blue", bd=4,text=chr(43),command=lambda: added_value.operation("add"))).grid(row = 1, column=3, pady=1)

btnSub=(Button(calc, width=6, height=2,font = ('arial', 20, 'bold' ), bg="powder blue", bd=4,text=chr(45),command=lambda: added_value.operation("sub"))).grid(row = 2, column=3, pady=1)

btnMulti=(Button(calc, width=6, height=2,font = ('arial', 20, 'bold' ), bg="powder blue", bd=4,text=chr(42),command=lambda: added_value.operation("multi"))).grid(row = 3, column=3, pady=1)

btnDiv=(Button(calc, width=6, height=2,font = ('arial', 20, 'bold' ), bg="powder blue", bd=4,text=chr(247),command=lambda: added_value.operation("divide"))).grid(row = 4, column=3, pady=1)
#=====================================================================================Row 5=====================================
btn0=(Button(calc, width=6, height=2,font = ('arial', 20, 'bold' ), bg="powder blue", bd=4,text="0", command=lambda: added_value.numberEnter(0))).grid(row = 5, column=0, pady=1)

btnDot=(Button(calc, width=6, height=2,font = ('arial', 20, 'bold' ), bg="powder blue", bd=4,text=".",command=lambda: added_value.numberEnter("."))).grid(row = 5, column=1, pady=1)

btnPM=(Button(calc, width=6, height=2,font = ('arial', 20, 'bold' ), bg="powder blue", bd=4,text=chr(177), command = added_value.MathsPM)).grid(row = 5, column=2, pady=1)

btnEquals=(Button(calc, width=6, height=2,font = ('arial', 20, 'bold' ), bg="powder blue", bd=4,text="=",command = added_value.sum_of_total)).grid(row = 5, column=3, pady=1)
root.mainloop()                           
