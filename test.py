from tkinter import*
root = Tk()
def clicked():
    ls = [89,79,85,65,82,69,71,65,89]
    st = ""
    count = 0
    for i in ls:
        st+=chr(i)
        count+=1
        if count == 3 or count == 6:
            st+=" "

    l1.config(text=st)
    
root.title("Test gui")
root.geometry("600x600")
l1 = Label(root,font=("Time New Roman",20),text="")
l1.pack()
b1 = Button(root,text="click here",font=("Time New Roman",20),command=clicked)
b1.config(width=50)
b1.pack()
root.mainloop()