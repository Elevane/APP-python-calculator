from tkinter import *

HEIGHT, WIDTH = 100, 250


class App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.grid(row=0, column=0)
        self.master.title("Calculator")

        self.val = ""
        self.createButtons()

    def createButtons(self):
        self.text = Label(self.master, text=self.val, bg="white", width=1)
        self.text.grid(row=0, column=0, padx=2, pady=2, columnspan=6)
        self.reset = Button(self.master, text="r", command=self.reset())
        self.reset.grid(row=0, column=2 , padx=2, pady=2)

        for i in range(10):
            if i > 0:
                button = Button(self.master, text=i, command=lambda value=i: self.addValue(value))
                if 0 < i <= 3:
                    col = abs((10 - i) - 9)
                    button.grid(row=1, column=col, padx=5, pady=5)

                if 3 < i <= 6:
                    col = abs((10 - i) - 6)
                    button.grid(row=2, column=col, padx=5, pady=5)
                if i > 6:
                    col = abs((10 - i) - 3)
                    button.grid(row=3, column=col, padx=5, pady=5)

        self.plus = Button(self.master, text="+", command=lambda value="+": self.addOperator(value))
        self.plus.grid( row= 4, column=0, padx=5, pady=5)
        self.less = Button(self.master, text="-", command=lambda value="-": self.addOperator(value))
        self.less.grid(row= 4 ,column=2 , padx=5, pady=5)
        self.zero = Button(self.master, text="0", command= lambda value="0":self.addValue(value))
        self.zero.grid(row=4, column=1 , padx=5, pady=5)
        self.divide = Button(self.master, text="/", command=lambda value="/": self.addOperator(value))
        self.divide.grid(row=5, column=0 , padx=5, pady=5)
        self.multiply = Button(self.master, text="*", command=lambda value="*": self.addOperator(value))
        self.multiply.grid(row=5, column=1, padx=5, pady=5)
        self.equal = Button(self.master, text="=", command=self.equal)
        self.equal.grid(row=5, column=2, padx=5, pady=5)

    def addValue(self, value):
        self.val += str(value)
        self.text["text"] = self.val

    def addOperator(self, value):
        if self.val and len(self.val) > 0:
            last = int(self.val[-1])
        else:
            last = False

        if last:
            self.val += "-"
            self.text["text"] = self.val

    def equal(self):
        res = str(eval(self.val))
        self.val = str(res)
        self.text['text'] = self.val

    def reset(self):
        self.val = ""
        self.text["text"] = self.val

if __name__ == "__main__":
    root = Tk()
    root.geometry("{}x{}".format(HEIGHT, WIDTH))
    App(master=root)
    root.mainloop()
