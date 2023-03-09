# *The calculations in this code may be outdated or inaccurate. Please don't rely on it for facts.*

import tkinter as tk
from tkinter import N, E, S, W

# Window
width, height = 300, 300
window = tk.Tk()
window.title("AUD Pay Calculator")

class PayClaculator:
    def __init__(self):
        self.total = 0
        self.postTax = 0
        self.newNum = 0

        # Entries and labels
        self.hintText = tk.Label(window, text="time in hours")
        self.hintText.grid(row=0, column=2, padx=5, pady=5)
        
        self.entry = tk.Entry(window)
        self.entry.grid(row=1, column=2, padx=5, pady=5)

        self.hintText2 = tk.Label(window, text="hourly rate")
        self.hintText2.grid(row=2, column=2, padx=5, pady=5)

        self.entry2 = tk.Entry(window)
        self.entry2.grid(row=3, column=2, padx=5, pady=5)

        self.multiplyText = tk.Label(window, text="Multipliers", font=("comicsans", 15))
        self.multiplyText.grid(row=4, column=2, padx=5, pady=5)

        # Buttons and labels
        self.multiplier1 = tk.Button(window, width=7, height=2, text="X1.5", command=self.multiply1)
        self.multiplier1.grid(row=5, column=1, padx=2, pady=5)

        self.multiplier2 = tk.Button(window, width=7, height=2, text="X2", command=self.multiply2)
        self.multiplier2.grid(row=5, column=2, padx=2, pady=5)

        self.multiplier3 = tk.Button(window, width=7, height=2, text="X2.5", command=self.multiply3)
        self.multiplier3.grid(row=5, column=3, padx=2, pady=5)

        self.calculateBtn = tk.Button(window, width=10, height=2, text="No Multiplier", command=self.addEntry)
        self.calculateBtn.grid(row=6, column=2, padx=5, pady=10)

        self.totalText = tk.Label(window, text=f"Before tax: ${self.total}", font=("comicsans", 15))
        self.totalText.grid(row=7, column=2, padx=5, pady=5)

        self.taxText = tk.Label(window, text=f"After tax: ${self.postTax}", font=("comicsans", 15))
        self.taxText.grid(row=8, column=2, padx=5, pady=5)

        self.clearBtn = tk.Button(window, width=10, height=2, text="CLEAR ALL", command=self.clearAll)
        self.clearBtn.grid(row=9, column=2, padx=5, pady=10)


        window.mainloop()

    def clearAll(self):
        self.total = 0
        self.newNum = 0
        self.updateTotal()
        self.entry.delete(0, 'end')
        self.entry2.delete(0, 'end')

    def multiply1(self):
        try:
            self.newNum = round(float((float(self.entry.get()) * 1.5) * float(self.entry2.get())), 2)
            self.updateTotal()
        except ValueError:
            pass

    def multiply2(self):
        try:
            self.newNum = round(float((float(self.entry.get()) * 2) * float(self.entry2.get())), 2)
            self.updateTotal()
        except ValueError:
            pass

    def multiply3(self):
        try:
            self.newNum = round(float((float(self.entry.get()) * 2.5) * float(self.entry2.get())), 2)
            self.updateTotal()
        except ValueError:
            pass

    def addEntry(self):
        try:
            self.newNum = round(float((float(self.entry.get()) * float(self.entry2.get()))), 2)
            self.updateTotal()
        except ValueError:
            pass

    def updateTotal(self):
        self.total += self.newNum
        self.totalText.configure(text=f"Before tax: ${self.total}")
        self.newNum = 0
        self.calculateTax()

    def calculateTax(self):
        self.salary = float(self.total * 26)
        self.taxCut = 0
        if self.salary > 120001:
            self.taxCut = float(29467 + ((self.salary - 120000) * 0.37))
        elif self.salary > 45001:
            self.taxCut = float(5092 + ((self.salary - 45000) * 0.325))
        elif self.salary > 18201:
            self.taxCut = float((self.salary - 18200) * 0.19)
        else:
            self.taxCut = 0

        self.postTax = round(float(self.total - (self.taxCut / 26)), 2)
        self.taxText.configure(text=f"After tax: ${self.postTax}")

pc = PayClaculator()
