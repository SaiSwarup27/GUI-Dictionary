import tkinter as tk
from tkinter import messagebox
from PyDictionary import PyDictionary

window=tk.Tk()
window.title('Dictionary')
dictionary = PyDictionary()

frame=tk.Frame(master=window,relief=tk.SUNKEN,bg='black',width=20)
frame.pack(ipadx=10)

label1=tk.Label(master=frame,text='Dictionary',font=("Arial", 15),fg='blue',bg='black')
label1.pack()

label2=tk.Label(master=frame,text='enter a word to search',font=("Arial", 10),bg='black',fg='white')
label2.pack()

entry1=tk.Entry(master=frame,width=15)
entry1.pack(pady=10)

button=tk.Button(master=frame,text='Proceed',relief=tk.RAISED,font=("Arial", 8),command=lambda: getmeaning())
button.pack()

label2=tk.Label(master=frame,text='Meaning:',font=("Arial", 10),width=10,bg='black',fg='white')
label2.pack()

text=tk.Label(master=frame,text=" ",font=("Arial", 10),height=1,bg='black',fg='white')
text.pack()

def getmeaning():
    response = dictionary.meaning(entry1.get())
    if(response):
        if('Noun' in response):
            meaning = response['Noun'][0]
        elif('Verb' in response):
            meaning = response['Verb'][0]
        elif('Adjective' in response):
            meaning = response['Adjective'][0]
        else:
            meaning = "Invalid word"
    else:
        messagebox.showinfo("Error", "Please add a Noun, Pronoun, verb or a valid word.")
    
    text.config(text=meaning)



window.mainloop()