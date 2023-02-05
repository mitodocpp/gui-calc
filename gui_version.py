from tkinter import *

frame = Tk(className="calculator")
frame.config(bg="gray")
frame.geometry("300x300")

result_label = Label(frame, text="", bg="gray", fg="white")
operation = Text(frame, width=30, height=1, bg="gray", fg="white")

def calculate():
    global result_label
    global operation
    result_label.config(text="result: " + str(eval(operation.get(1.0, "end-1c"))))
    result_label.pack()


orientation = Label(frame, text="enter the operation below:", bg="gray", fg="white")
orientation.pack()

operation.pack()

calculate = Button(frame, text="calculate", bg="gray", fg="white", command=calculate)
calculate.pack()

frame.mainloop()
