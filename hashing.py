from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.geometry("400x400")
root.title("Encrypt")
Label(root, text="Enter The Word", font="comicsansms 13 bold").pack()
security = (('a', 'Z'),('b', 'Q'),('c','E'), ('d','T'),('e','J'),('f','Y'),('g','T'),('h','N'),('i','/'),('j','D'),('k','M'),('l','p'),('m','N'),('n','f'),('o','|'),('p','q'),('q','5'),('r','^'),('s','c'),('t','E'),('u','A'),('v','t'),('w','o'),('x','c'),('y','U'),('z','d'))
def encrypt():
    word_ = word.get()

    password = ""

    for i in word_:
        for k , v in security:
            if i == k:
                password += v
    word.delete(0, END)
    print(password, " is a pass")
    text1.insert(INSERT,password+"\n")
    


word = Entry(root)
word.pack()

b = Button(root, text = "Enter", command= encrypt)
b.pack()
text1 = Text(root, height= 10, width=50)

text1.pack()

root.mainloop()