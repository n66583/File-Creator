from tkinter import *
import os
window = Tk()
window.title('File Creator')
window.iconbitmap('favicon.ico')
window.geometry("300x70")
# Functions
def rm_logs():
    try:
        os.remove("ErrorFileNotFound.log")
    except FileNotFoundError:
        pass
def create_folder():
    try:
        folder_path_name = input.get()
        f = open(folder_path_name, "x")
        f.close()
        f = open(folder_path_name, "r")
        x = f.read()
        y = None
        label.config(text=folder_path_name, fg="black")
    except FileNotFoundError:
        try:
            f = open("ErrorFileNotFound.log", "x")
            f.close()
            f = open("ErrorFileNotFound.log", "w")
            f.write("Error: Your file isn't support or your os not found file")
            f.close()
            f = open("ErrorFileNotFound.log", "r")
            y = f.read()
            label.config(text="Error: File Not Found", fg="red")
        except FileExistsError:
            os.remove("ErrorFileNotFound.log")
            f = open("ErrorFileNotFound.log", "x")
            f.close()
            f = open("ErrorFileNotFound.log", "w")
            f.write("Error: Your file isn't support or your os not found file")
            f.close()
            f = open("ErrorFileNotFound.log", "r")
            y = f.read()
            label.config(text="Error: File Not Found", fg="red")
    except FileExistsError:
        os.remove(folder_path_name)
        f = open(folder_path_name, "x")
        f.close()
        f = open(folder_path_name, "r")
        z = f.read()
        y = None
        label.config(text=folder_path_name, fg="black")
    
    root = Tk()
    root.title(folder_path_name)
    root.geometry("300x400")
    def file_editor():
        f = open(folder_path_name, "w")
        f.write(input2.get())
        f.close()
        f = open(folder_path_name, "r")
        label2.config(text=f.read())
    l = Label(root, text=folder_path_name, bg="blue", fg="white")
    l.pack()
    input2 = Entry(root, width=100)
    input2.pack(padx=10, pady=10)
    button2 = Button(root, text="edit file", font=('sans-serif 16'), command=file_editor)
    button2.pack(padx=10, pady=20)
    label2 = Label(root, text="")
    label2.pack()
    # footer
    def file_edit_exit():
        f = open(folder_path_name, "w")
        f.write(input2.get())
        f.close()
        f = open(folder_path_name, "r")
        label2.config(text=f.read())
        close_win()
    def close_win():
        root.destroy()
    b_exit = Button(root, text="exit", command=close_win)
    b_exit.place(y=100)
    b_save_exit = Button(root, text="save and exit", command=file_edit_exit)
    b_save_exit.place(y=127)
    
    try:
        name, ext = folder_path_name.split('.')
    except ValueError:
        folder_path_name = folder_path_name+"."
        name, ext = folder_path_name.split('.')
    if ext == "":
        folder_path_name = folder_path_name[:-1]
    if ext == "html" or ext == "htm":
        root.iconbitmap('icons\html.ico')
    elif ext == "css":
        root.iconbitmap('icons\css.ico')
    elif ext == "js":
        root.iconbitmap('icons\javascript.ico')
    elif ext == "php":
        root.iconbitmap('icons\php.ico')
    elif ext == "py":
        root.iconbitmap('icons\python.ico')
    elif ext == "java":
        root.iconbitmap('icons\java.ico')
    elif ext == "json":
        root.iconbitmap('icons\json.ico')
    elif ext == "md":
        root.iconbitmap('icons\markdown.ico')
    elif ext == "c":
        root.iconbitmap('icons\c.ico')
    elif ext == "cpp":
        root.iconbitmap('icons\cpp.ico')
    elif ext == "cs":
        root.iconbitmap('icons\csharp.ico')
    elif ext == "go":
        root.iconbitmap('icons\go.ico')
    elif ext == "sql":
        root.iconbitmap('icons\sql.ico')
    elif ext == "ts":
        root.iconbitmap('icons/typescript.ico')
    elif ext == "xml":
        root.iconbitmap('icons/xml.ico')
    elif ext == "bat":
        root.iconbitmap('icons/powershell.ico')
    elif ext == "yaml":
        root.iconbitmap('icons/yaml.ico')
    elif ext == "xml":
        root.iconbitmap('icons/xml.ico')
    elif ext == "ruby":
        root.iconbitmap('icons/ruby.ico')
    elif ext == "vue":
        root.iconbitmap('icons/vue.ico')
    elif ext == "less":
        root.iconbitmap('icons/less.ico')
    elif ext == "react":
        root.iconbitmap('icons/react.ico')
    else:
        root.iconbitmap('icons/default.ico')
    if y != None:
        root.destroy()
# Buttons
button = Button(window, text="Create!", command=create_folder)
button.pack()
# Inputs
input = Entry(window)
input.pack()
# Labels
label = Label(window, text="")
label.pack()
rm_logs = Button(window, text="remove logs", command=rm_logs)
rm_logs.place(y=45)
window.mainloop()
