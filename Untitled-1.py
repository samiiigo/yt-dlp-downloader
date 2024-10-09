from customtkinter import *
root = CTk()
frame=CTkFrame(root,width=100,height=100)
frame.pack()
label = CTkLabel(frame,text="Enter a digit that you guessed:").pack()
entry= CTkEntry(frame)
entry.pack()
root.after(500,lambda:entry.focus_set())
button1=CTkButton(root,width=4,height=1,text='ok')
button1.pack()

root.mainloop()
