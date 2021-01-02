try:
    import wget
    from tkinter import *
    import sys
    import os
    from tkinter.filedialog import *

    root = Tk()
    root.title("Github Repository Downloader By Aaditya Kandel")

    def cont():
        btn1.config(text="Download",command=dwn)
        l1.config(state=NORMAL)
        l2.config(state=NORMAL)
        en1.config(state=NORMAL)
        en2.config(state=NORMAL)

    def progress(current, total, width=80):
        progress_message = "Downloading: %d%% [%d / %d] bytes" % (current / total * 100, current, total)
        root.update()
        if btn1['text'] == "100":
            btn1.config(text="Downloading 100%")
        else:
            btn1.config(text=f"{progress_message[0:16]}")
        sys.stdout.flush()

    def dwn():
        try:
            os.system(f'echo {(rep.get())}>rp.data')
            os.system(f'echo {(namee.get())}>nm.data')
            l1.config(state=DISABLED)
            l2.config(state=DISABLED)
            en1.config(state=DISABLED)
            en2.config(state=DISABLED)
            btn1.config(state=DISABLED,text="Downloading..")
            name = askdirectory(initialdir="C:/Users",
                                )
            loc.set(name)
            try:
                url = f"https://github.com/{(namee.get())}/{(rep.get())}/archive/master.zip"
                wget.download(url,(loc.get()),progress)
            except:
                url = f"https://github.com/{(namee.get())}/{(rep.get())}/archive/main.zip"
                wget.download(url, (loc.get()), progress)
            btn1.config(text="Download Complete [ Click To Continue ]",command = cont,state=NORMAL)
        except:
            btn1.config(text="Download Error [ Click To Continue ]",state=NORMAL,command=cont)
    # Giving String Variables
    loc = StringVar()
    namee = StringVar()
    rep = StringVar()

    try:
        f = open('nm.data','r+')
        for words in f:
            pass
        namee.set(words[0:-1])
        f.close()
        try:
            f = open('rp.data','r+')
            for words in f:
                pass
            rep.set(words[0:-1])
            f.close()
        except:
            pass
    except:
        pass

    f1 = Frame(borderwidth = 10,bg="black")
    f2 = Frame(borderwidth = 10,bg="black")
    f3 = Frame(borderwidth = 10,bg="black")

    l1 = Label(f1,text = "Name Of Github ID: ",
               bg = "black",
               fg ="white",
               font="comicsansms 15 bold")
    en1 = Entry(f1,textvariable = namee,
                bg = "white",
                fg = "black",
                font = "comicsansms 15 bold")
    l1.pack(side=LEFT)
    en1.pack(side=LEFT)

    l2 = Label(f2,text = "Name Of Repository: ",
               bg = "black",
               fg ="white",
               font="comicsansms 15 bold")
    en2 = Entry(f2,textvariable = rep,
                bg = "white",
                fg = "black",
                font = "comicsansms 15 bold")
    l2.pack(side=LEFT)
    en2.pack(side=LEFT)

    btn1 = Button(text="Download",
                bg = "black",
                fg = "white",
                font = "comicsansms 15 bold",
                pady=8,
                padx=8,
                relief=SUNKEN,
                command=dwn)
    f1.pack(anchor = "w")
    f2.pack(anchor = "w")
    f3.pack(anchor = "w")
    Label(text="",bg="black").pack()

    btn1.pack()
    root.config(bg="black")
    root.mainloop()
except:
    quit()