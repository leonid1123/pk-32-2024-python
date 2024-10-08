#09.10 - работа по pack,place,grid
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
#root.resizable(0, 0)

for c in range(3):
    root.columnconfigure(index=c, weight=1)
for r in range(7):
    root.rowconfigure(index=r, weight=1)

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
listbox = Listbox(width=35, font="Arial 16")
email_label.grid(row=0, column=0)
email_entry.grid(row=0, column=1)
listbox.grid(row=0, column=2, rowspan=5, sticky=NSEW)
fname_label.grid(row=1, column=0)
fname_entry.grid(row=1, column=1)
name_label.grid(row=2, column=0)
name_entry.grid(row=2, column=1)
fname_label.grid(row=3, column=0)
fname_entry.grid(row=3, column=1)
sname_label.grid(row=4, column=0)
sname_entry.grid(row=4, column=1)
button.grid(row=5, column=0, columnspan=2)
res_label.grid(row=6, column=0)
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
