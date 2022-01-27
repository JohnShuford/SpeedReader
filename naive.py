import time
import tkinter as tk
from tkinter import messagebox

ROOT = tk.Tk()

ROOT.withdraw()

first = "Five score years ago, a great American, in whose symbolic shadow we stand today, signed the Emancipation Proclamation.\
        This momentous decree came as a great beacon light of hope to millions of Negro slaves who had been seared in the flames of withering injustice.\
        It came as a joyous daybreak to end the long night of their captivity.But 100 years later, the Negro still is not free. \
        One hundred years later, the life of the Negro is still sadly crippled by the manacles of segregation and the chains of discrimination.\
        One hundred years later, the Negro lives on a lonely island of poverty in the midst of a vast ocean of material prosperity.\
        One hundred years later the Negro is still languished in the corners of American society and finds himself in exile in his own land. And so we've come\
        here today to dramatize a shameful condition. In a sense we've come to our nation's capital to cash a check."
#display = sentence.split()

def flashing(sentence):
    count = 0
    words = sentence.split()
    print (words)
    for word in words:
        messagebox.showinfo(message=word)
        time.sleep(0.1)

flashing(first)