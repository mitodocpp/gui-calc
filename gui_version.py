from tkinter import *


frame = Tk(className="calculator")
frame.config(bg="gray")
frame.geometry("500x80")

calc_input = Text(frame, height=1,width=50, bg="gray")
calc_input.pack()
def calc():
    global result_label
    result = calc_input.get(1.0, "end-1c")
    result_label.config(text="result: " + str(eval(result)), bg="black", fg="white")
    result_label.pack()

calculate = Button(frame, text="calculate", command=calc, bg="black", fg="white")
calculate.pack()

result_label = Label(frame, text="", bg="gray")
result_label.pack()

frame.mainloop()
