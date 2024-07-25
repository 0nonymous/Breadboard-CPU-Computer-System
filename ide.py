import tkinter

root = tkinter.Tk()
root.geometry("350x250")
root.title("IDE Assembly Alpha")
root.minsize(height=250, width=350)
root.maxsize(height=250, width=350)


# adding scrollbar
scrollbar = tkinter.Scrollbar(root)

# packing scrollbar
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

text_info = tkinter.Text(root, yscrollcommand=scrollbar.set)
text_info.pack(fill=tkinter.BOTH)

# configuring the scrollbar
scrollbar.config(command=text_info.yview)

root.mainloop()
