from tkinter import *
from tkinter import ttk


def add_value(value):
    current_text = display.get()
    display.delete(0, END)
    display.insert(0, current_text + value)

def calculate():
    current_text = display.get()
    try:
        result = eval(current_text)
        display.delete(0, END)
        display.insert(0, str(result))
    except Exception as e:
        display.delete(0, END)
        display.insert(0, "Error")


def clear_display():
    display.delete(0, END)


janela = Tk()
janela.title("Calculadora")
janela.geometry("235x318")
janela.resizable(False, False)


frame_tela = Frame(janela, width=235, height=50, bg="lightgray")
frame_tela.grid(row=0, column=0)

display = Entry(frame_tela, font=("Arial", 18), borderwidth=2, relief="solid", justify=RIGHT)
display.grid(row=0, column=0, ipadx=5, ipady=5)

frame_botoes = Frame(janela, width=235, height=268)
frame_botoes.grid(row=1, column=0)

botoes = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3)
]


for (text, row, col) in botoes:
    if text == '=':
        btn = Button(frame_botoes, text=text, width=5, height=2, command=calculate)
    else:
        btn = Button(frame_botoes, text=text, width=5, height=2, command=lambda t=text: add_value(t))
    btn.grid(row=row, column=col, padx=2, pady=2)


btn_clear = Button(frame_botoes, text='C', width=5, height=2, command=clear_display)
btn_clear.grid(row=0, column=0, padx=2, pady=2, columnspan=4, sticky='we')


janela.mainloop()
