import tkinter as tk 
from tkinter import filedialog, Text
import os

root = tk.Tk()
root.title("Programs To Do List ")
root.iconbitmap("to_do_list_apps.ico")
apps = []

if os.path.isfile("previous-apps.txt"):
    with open("previous-apps.txt","r") as pa:
        tempapps = pa.read()
        tempapps = tempapps.split(",")
        apps = [item for item in tempapps if item.strip()]
            
def addApps():
    for widget in frame.winfo_children():
        widget.destroy()

    fileName = filedialog.askopenfilename(initialdir="/",title="Select Application",
                                        filetypes=(("Executables","*.exe"),("All files","*.*"))
                                        )  
    if fileName != "":
        apps.append(fileName)

    for app in apps:
        label = tk.Label(frame,text=app,bg="gray")
        label.pack()

def runApps():
    for app in apps:
        os.startfile(app)

def delApps():
    apps.clear()

    for widget in frame.winfo_children():
        widget.destroy()

canvas = tk.Canvas(root,height=700,width=700,bg="#263D42")
canvas.pack()

frame = tk.Frame(root,bg="white")
frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

infoframe = tk.Frame(root,bg="white")
infoframe.place(relwidth=0.8,relheight=0.05,relx=0.1,rely=0.01)

introinfo = tk.Label(infoframe,text="To add applications to be opened, use the open file button")
introinfo.pack()

selectFiles = tk.Button(
                        root,text="Open File",padx=10,
                        pady=6,bg="white",fg="#263D42",command=addApps
                        )
selectFiles.place(relwidth=0.2,relheight=0.05,relx=0.2,rely=0.92)

runApp = tk.Button(
                    root,text="Run Applications",padx=10,
                    pady=6,bg="white",fg="#263D42",command=runApps
                    )
runApp.place(relwidth=0.2,relheight=0.05,relx=0.4,rely=0.92)

delApp = tk.Button(
                    root,text="Delete Applications",padx=10,
                    pady=6,bg="white",fg="#263D42",command=delApps
                    )
delApp.place(relwidth=0.2,relheight=0.05,relx=0.6,rely=0.92)

for app in apps:
        label = tk.Label(frame,text=app,bg="gray")
        label.pack()

root.mainloop()

with open("previous-apps.txt",'w') as pa:
    for app in apps:
        pa.write(app+",")
    