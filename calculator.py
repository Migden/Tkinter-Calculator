from tkinter import *

expression = ""

def button_press(num):
        global expression
        expression += str(num)
        equation.set(expression)

def eqaul_press():
        try:
                global expression
                final = str(eval(expression))
                equation.set(final)
                expression = ""
        except:
                equation.set(" ERROR ")
                expression = ""

def press_clear():
        global expression
        equation.set("")
        expression = ""


if __name__ == "__main__":
        calc = Tk()
        calc.title("Calculator")
        calc.configure(background="white")
        calc.geometry("260x150")
        equation = StringVar()
        grid = Entry(calc, textvariable=equation)
        grid.grid(columnspan=4, ipadx=70)
        button1 = Button(calc, text=' 7 ', fg='black', bg='red', command=lambda: button_press(7), height=1, width=7)
        button1.grid(row=2, column=0)
        button2 = Button(calc, text=" 8 ", fg='black', bg='red', command=lambda: button_press(8), height=1, width=7)
        button2.grid(row=2, column=1)
        button3 = Button(calc, text=" 9 ", fg="black", bg='red', command=lambda: button_press(9), height=1, width=7)
        button3.grid(row=2, column=2)
        button4 = Button(calc, text=" clear ", fg='black', bg='red', command=press_clear, height=1, width=7)
        button4.grid(row=2, column=3)
        button5 = Button(calc, text=' / ', fg='black', bg='red', command=lambda: button_press('/'), height=1, width=7)
        button5.grid(row=3, column=3)
        button6 = Button(calc, text=" - ", fg='black', bg='red', command=lambda: button_press('-'), height=1, width=7)
        button6.grid(row=4, column=3)
        button7 = Button(calc, text=' * ', fg='black', bg='red', command=lambda: button_press('*'), height=1, width=7)
        button7.grid(row=5, column=3)
        button8 = Button(calc, text=' 6 ', fg='black', bg='red', command=lambda: button_press(6), height=1, width=7)
        button8.grid(row=3, column=2)
        button9 = Button(calc, text=' 5 ', fg='black', bg='red', command=lambda: button_press(5), height=1, width=7)
        button9.grid(row=3, column=1)
        button10 = Button(calc, text=' 4 ', fg='black', bg='red', command=lambda: button_press(4), height=1, width=7)
        button10.grid(row=3, column=0)
        button11 = Button(calc, text=' = ', fg='black', bg='red', command=eqaul_press, height=1, width=7)
        button11.grid(row=6, column=3)
        button12 = Button(calc, text=' 1 ', fg='black', bg='red', command=lambda: button_press(1), height=1, width=7)
        button12.grid(row=4, column=0)
        button13 = Button(calc, text=' 2 ', fg='black', bg='red', command=lambda: button_press(2), height=1, width=7)
        button13.grid(row=4, column=1)
        button14 = Button(calc, text=' 3 ', fg='black', bg='red', command=lambda: button_press(3), height=1, width=7)
        button14.grid(row=4, column=2)
        button15 = Button(calc, text=' 0 ', fg='black', bg='red', command=lambda: button_press(0), height=1, width=7)
        button15.grid(row=5, column=0)
        button16 = Button(calc, text=' . ', fg='black', bg='red', command=lambda: button_press('.'), height=1, width=7)
        button16.grid(row=5, column=1)
        button17 = Button(calc, text=' + ', fg='black', bg='red', command=lambda: button_press('+'), height=1, width=7)
        button17.grid(row=5, column=2)
        button18 = Button(calc, text=' ( ', fg='black', bg='red', command=lambda: button_press('('), height=1, width=7)
        button18.grid(row=6, column=0)
        button19 = Button(calc, text=' ) ', fg='black', bg='red', command=lambda: button_press(')'), height=1, width=7)
        button19.grid(row=6, column=1)
        calc.resizable(False, False)
        calc.mainloop()