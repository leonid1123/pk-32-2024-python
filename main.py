from tkinter import *


def int_check(_user_input):
    tupoy = True
    while tupoy:
        try:
            tupoy = False
            tmp = int(_user_input)
            return tmp
        except:
            print("нужны чиселки")
            debug1 = input("Введите значение")
            tupoy = True
            return int_check(debug1)


root = Tk()  # создаем корневой объект - окно
root.title("Список покупок")  # устанавливаем заголовок окна
root.geometry("500x400")  # устанавливаем размеры окна
listbox = Listbox(root, font="Arial 16", width=40)
name_entry = Entry(root, font="Arial 16", width=40)
frame = Frame(root)
quantity_entry = Entry(frame, font="Arial 16", width=20)
price_entry = Entry(frame, font="Arial 16", width=20)
btn = Button(root, font="Arial 16", text="+", width=40)


names = []
quantities = []
prices = []
go = True
while go:
    name = input("Введите название продукта: ")
    quantity = int_check(input("Введите количество: "))
    price = int_check(input("Введите цену:"))

    names.append(name)
    quantities.append(quantity)
    prices.append(price)
    for i in range(0, len(names)):
        print(names[i], quantities[i], prices[i])
    print("Итоговая стоимость:", sum(prices))
    user_input = input("Еще? [Д]а/[Н]ет ")
    if user_input == "Д":
        go = True
    else:
        go = False

listbox.pack()
name_entry.pack()
frame.pack()
quantity_entry.pack(side=LEFT)
price_entry.pack()
btn.pack()

root.mainloop()
