import tkinter as tk
from PIL import ImageTk, Image

Jena = 10
Health = 10
Psyho = 10

new_window = None
five_window = None
third_window = None
four_window = None

#Hi)

def reset_stats():
    global Jena, Health, Psyho
    Jena = 10
    Health = 10
    Psyho = 10
    update_labels()



def play_game():
    global Jena, Health, Psyho
    Jena -= 1
    Health += 1
    Psyho = Psyho + 1
    update_labels()

def study():
    global Jena, Health, Psyho
    Jena += 1
    Health -= 1
    Psyho = Psyho + 1
    update_labels()

def pismo():
    global Jena, Health, Psyho
    Jena += 1
    Health -= 1
    Psyho = Psyho -1
    update_labels()

def bariga():
    global Jena, Health, Psyho
    if Jena < 5:
        Jena += 1  
    else:
        Jena -= 1
    
    Health -= 1
    Psyho = Psyho + 1
 
    update_labels()

def gitara():
    global Jena, Health, Psyho
    Jena -= 0
    Health -= 1
    Psyho = Psyho + 1
    update_labels()

def demo():
    global Jena, Health, Psyho
    Jena -= 0
    Health -= 5
    Psyho = Psyho + 15
    update_labels()


def update_labels():
    global new_window
    global third_window
    jena_label.configure(text=f"Jena: {Jena}")
    health_label.configure(text=f"Health: {Health}")
    psyho_label.configure(text=f"Psyho: {Psyho}")
    if Jena <= 0 or Health <= 0 or Psyho <= 0:
        open_five_window()


    
 



def on_closing():
    # Обработчик события закрытия окна
    # Здесь вы можете добавить логику или очистку перед закрытием
    # Здесь я просто печатаю сообщение перед закрытием окна
    label = tk.Label(root, text="Не уходи...")
    label.pack()
    root.after(1000, root.destroy)  # Закрыть окно через 5 секунд (2000 миллисекунд)


def open_new_window():
    global new_window
    # Функция для открытия нового окна с четырьмя кнопками
    new_window = tk.Toplevel(root)
    new_window.attributes("-topmost", True)  # Установка нового окна поверх родительского
    new_window.geometry("200x200+{}+{}".format(root.winfo_x() + root.winfo_width() // 2 - 100, root.winfo_y() + root.winfo_height() // 2 - 100))
    new_window.title("Комп")
    new_window.grab_set()  # Захват фокуса для нового окна
    new_window.iconbitmap("D:\Code\CBeTbl\Igra\game\photo_2023-05-28_22-20-54.ico")

    # Создание четырех кнопок в новом окне
    button1 = tk.Button(new_window, text="Поиграть в игру", command=play_game)
    button1.pack()

    button2 = tk.Button(new_window, text="Поучиться", command=study)
    button2.pack()

    button3 = tk.Button(new_window, text="Написать другу", command=bariga)
    button3.pack()

    button4 = tk.Button(new_window, text="Написать жене", command=pismo)
    button4.pack()

    button5 = tk.Button(new_window, text="выход", command=new_window.destroy)
    button5.pack()


def open_third_window():
    global third_window
    third_window = tk.Toplevel(root)  # Создание третьего окна с помощью Toplevel()
    third_window.attributes("-topmost", True)  # Установка нового окна поверх родительского
    third_window.geometry("200x200+{}+{}".format(root.winfo_x() + root.winfo_width() // 2 - 100, root.winfo_y() + root.winfo_height() // 2 - 100))
    third_window.title("Музыка")
    third_window.grab_set()  # Захват фокуса для нового окна
    third_window.iconbitmap("D:\Code\CBeTbl\Igra\game\photo_2023-05-28_22-20-54.ico")

    button1 = tk.Button(third_window, text="Поиграть на гитаре", command=gitara)
    button1.pack()

    button2 = tk.Button(third_window, text="Записать демо", command=demo)  # Замените study на demo
    button2.pack()

    button3 = tk.Button(third_window, text="выход", command=third_window.destroy)
    button3.pack()

def open_four_window():
    global four_window
    four_window = tk.Toplevel(root)  # Создание четвертого окна с помощью Toplevel()
    four_window.attributes("-topmost", True)  # Установка нового окна поверх родительского
    four_window.geometry("200x200+{}+{}".format(root.winfo_x() + root.winfo_width() // 2 - 100, root.winfo_y() + root.winfo_height() // 2 - 100))
    four_window.title("Инструкции")
    four_window.grab_set()  # Захват фокуса для нового окна
    four_window.iconbitmap("D:\Code\CBeTbl\Igra\game\photo_2023-05-28_22-20-54.ico")
    label = tk.Label(four_window, text='Статы не ниже нуля. Можно брать комп и гитару.', justify="left", wraplength=four_window.winfo_width())
    label.pack( padx=2, pady=20)

def open_five_window():
    global five_window
    five_window = tk.Toplevel(root)
    five_window.attributes("-topmost", True)
    five_window.geometry("200x200+{}+{}".format(root.winfo_x() + root.winfo_width() // 2 - 100, root.winfo_y() + root.winfo_height() // 2 - 100))
    five_window.title("G.O.")
    five_window.grab_set()
    five_window.iconbitmap("D:\Code\CBeTbl\Igra\game\photo_2023-05-28_22-20-54.ico")
    label = tk.Label(five_window, text='Ты проиграл! Ещё попробуешь?', justify="left")
    label.pack(anchor="n", padx=10, pady=10)

    def button_click():
        five_window.destroy()
        reset_stats()
        if new_window:
            new_window.destroy()
        if third_window:
            third_window.destroy()
        if four_window:
            four_window.destroy()
        if five_window:
            five_window.destroy()
    
    button = tk.Button(five_window, text="Выход", command=root.destroy, width=9, height=1, highlightthickness=0, cursor="hand2", bg="#C09B74", font=("TkDefaultFont", 14))
    button.pack()
    button = tk.Button(five_window, text="Ещё раз", command=button_click, width=9, height=1, highlightthickness=0, cursor="hand2", bg="#C09B74", font=("TkDefaultFont", 14))
    button.pack()


#reset_button = tk.Button(root, text="Сбросить статистику", command=reset_stats)
#reset_button.pack()

# Создание главного окна
root = tk.Tk()  # Создание экземпляра Tk
root.title("Мрачная дрочильня")  # Заголовок окна
root.geometry("720x480")  # Размер окна

# Установка иконки
root.iconbitmap("D:\Code\CBeTbl\Igra\game\photo_2023-05-28_22-20-54.ico")  # Замените "path/to/icon.ico" на путь к вашей иконке

# Привязка обработчика события закрытия окна
root.protocol("WM_DELETE_WINDOW", on_closing)

# Создание фона с картинкой
background_image = Image.open("D:\Code\CBeTbl\Igra\game\Background.png")
background_photo = ImageTk.PhotoImage(background_image)
background_label = tk.Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
root.geometry(f"{background_image.width}x{background_image.height}")  # Установка размера окна по размеру изображения

# Создание кнопки


button = tk.Button(root, text=" ", command=open_new_window, width=1, height=1, highlightthickness=0, cursor="hand2", bg="#1D1D1D", font=("TkDefaultFont", 6))
button.place(x=761, y=349)
button.configure(relief=tk.FLAT)

button = tk.Button(root, text=" ", command=open_third_window, width=1, height=1, highlightthickness=0, cursor="hand2", bg="#C09B74", font=("TkDefaultFont", 14))
button.place(x=95, y=664)
button.configure(relief=tk.FLAT)

button = tk.Button(root, text="Инструкции", command=open_four_window, width=9, height=1, highlightthickness=0, cursor="hand2", bg="#C09B74", font=("TkDefaultFont", 14))
button.place(x=1215, y=700)

button = tk.Button(root, text="Выход", command=root.destroy, width=9, height=1, highlightthickness=0, cursor="hand2", bg="#C09B74", font=("TkDefaultFont", 14))
button.place(x=1215, y=762)

jena_label = tk.Label(root, text=f"Jena: {Jena}")
jena_label.pack()

health_label = tk.Label(root, text=f"Health: {Health}")
health_label.pack()

psyho_label = tk.Label(root, text=f"Psyho: {Psyho}")
psyho_label.pack()





# Запуск главного цикла обработки событий
root.mainloop()

