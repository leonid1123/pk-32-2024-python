from tkinter import *


def tik():
    user_input = email_entry.get()
    dog_pos = user_input.find("@")
    if dog_pos > - 1:
        login = user_input[0:dog_pos]
        #print(login)
        fam = fname_entry.get()
        name = name_entry.get()
        otch = sname_entry.get()
        password = (fam[0] + fam[len(fam) - 1] +
                    name[0] + name[len(name) - 1] +
                    otch[0] + otch[len(otch) - 1])
        res_label["text"] = f"Логин: {login}\nПароль: {password}"
        listbox.insert(0, f"Логин: {login} Пароль: {password}")


root = Tk()
root.geometry("800x600")
root.title("Программа генерации логина и пароля")
root.resizable(0, 0)
email_label = Label(text="Введите адрес электронной почты",
                    font="Arial 16")
email_entry = Entry(font="Arial 16")
fname_label = Label(text="Введите фамилию", font="Arial 16")
fname_entry = Entry(font="Arial 16")
name_label = Label(text="Введите имя", font="Arial 16")
name_entry = Entry(font="Arial 16")
sname_label = Label(text="Введите отчество", font="Arial 16")
sname_entry = Entry(font="Arial 16")

button = Button(text="Жмяк", command=tik, font="Arial 16")

res_label = Label(text="Логин: \nПароль:", font="Arial 16")
listbox = Listbox(width=65, font="Arial 16")
email_label.place(x=0, y=0)
email_entry.place(x=400, y=0)
fname_label.place(x=0, y=30)
fname_entry.place(x=400, y=30)
name_label.place(x=0, y=60)
name_entry.place(x=400, y=60)
sname_label.place(x=0, y=90)
sname_entry.place(x=400, y=90)
button.place(x=350, y=125)
res_label.place(x=0, y=155)
listbox.place(x=10, y=220)
'''
ui_elements = [email_label, email_entry,
               fname_label, fname_entry,
               name_label, name_entry,
               sname_label,
               sname_entry, button,
               res_label, listbox]
for item in ui_elements:
    item.pack(anchor=W, padx=10, pady=2, side=BOTTOM)
'''
root.mainloop()
