from tkinter import *


def tik():
    user_input = email_entry.get()
    dog_pos = user_input.find("@")
    if dog_pos >- 1:
        login = user_input[0:dog_pos]
        print(login)


root = Tk()
root.geometry("400x400")
root.title("Программа генерации логина и пароля")

email_label = Label(text="Введите адрес электронной почты",
                    font="Arial 16")
email_entry = Entry(font="Arial 16")
fname_label = Label(text="Введите фамилию", font="Arial 16")
fname_entry = Entry(font="Arial 16")
name_label = Label(text="Введите имя", font="Arial 16")
name_entry = Entry(font="Arial 16")
sname_label = Label(text="Введите отчество",font="Arial 16")
sname_entry = Entry(font="Arial 16")

button = Button(text="Жмяк", command=tik, font="Arial 16")

res_label = Label(text="Логин: \nПароль:", font="Arial 16")
ui_elements = [email_label, email_entry,
               fname_label, fname_entry,
               name_label, name_entry,
               sname_label,
               sname_entry, button,
               res_label]
for item in ui_elements:
    item.pack()

root.mainloop()
