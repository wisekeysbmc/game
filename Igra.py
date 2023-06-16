import tkinter as tk
from PIL import ImageTk, Image
from pygame import mixer
import pygame
pygame.mixer.init()

Jena = 6
Health = 5
Psyho = 5

new_window = None
five_window = None
third_window = None
four_window = None
next_level_window = None


#Hi)

def reset_stats():
    global Jena, Health, Psyho
    Jena = 6
    Health = 5
    Psyho = 5
    update_labels()
    next_level()


def play_game():
    global Jena, Health, Psyho
    Jena -= 1
    Health += 1
    Psyho = Psyho
    update_labels()
    next_level()

#def study():
#    global Jena, Health, Psyho
#    Jena += 1
#    Health -= 1
#    Psyho = Psyho + 1
#    update_labels()
#   next_level()

def pismo():
    global Jena, Health, Psyho
    if Health >= 10:
        Jena += 5
    else:
        Jena += 1
    Health -= 1
    Psyho = Psyho -1
    update_labels()
    next_level()


def gitara():
    global Jena, Health, Psyho
    if Health >= 10:
        Psyho = Psyho + 5
        Health = Health 
    else:
        Psyho = Psyho + 1
        Health -= 1
    Jena -= 0
    
    
    update_labels()
    next_level()

#def demo():
#    global Jena, Health, Psyho
#    Jena -= 0
#    Health -= 1
#    Psyho = Psyho + 1
#    update_labels()
#    next_level()

def close_all():
        if root:
            root.destroy()
        if new_window:
            new_window.destroy()
        if third_window:
            third_window.destroy()
        if four_window:
            four_window.destroy()
        if five_window:
            five_window.destroy()
        if next_level_window:
            next_level_window.destroy()
        if new_level:
            new_level.destroy()


def update_labels():
    global new_window
    global third_window
    jena_label.configure(text=f"Jena: {Jena}")
    health_label.configure(text=f"Health: {Health}")
    psyho_label.configure(text=f"Psyho: {Psyho}")
    if Jena <= 0 or Health <= 0 or Psyho <= 0:
        open_five_window()

def new_level():
        global new_level

        new_level = tk.Toplevel(root)
        new_level.attributes("-topmost", True)  # Установка нового окна поверх родительского
        new_level.geometry("720x480+{}+{}".format(root.winfo_x() + root.winfo_width() // 2 - 100, root.winfo_y() + root.winfo_height() // 2 - 100))
        new_level.title("Новый уровень")
        new_level.grab_set()  # Захват фокуса для нового окна
        new_level.iconbitmap("D:\Code\CBeTbl\Igra\game\photo_2023-05-28_22-20-54.ico")
        
        
        # Загрузка фонового изображения
        background_image = Image.open("D:\Code\CBeTbl\Igra\game\lojka.png")
        background_photo = ImageTk.PhotoImage(background_image)
        
        # Создание виджета Label с фоновым изображением
        background_label = tk.Label(new_level, image=background_photo)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)


        button = tk.Button(new_level, text="Выход", command=close_all, width=9, height=1, highlightthickness=0, cursor="hand2", bg="#C09B74", font=("TkDefaultFont", 14))
        button.pack(anchor="s")
        

        if new_window:
            new_window.destroy()
        if third_window:
            third_window.destroy()
        if four_window:
            four_window.destroy()
        if five_window:
            five_window.destroy()
        if next_level_window:
            next_level_window.destroy()

        next_level.mainloop()





def next_level():
    global next_level_window
    if Jena >= 10 and Health >= 10 and Psyho >= 10:
        next_level = tk.Toplevel(root)
        next_level.attributes("-topmost", True)
        next_level.geometry("328x232+{}+{}".format(root.winfo_x() + root.winfo_width() // 2 - 100, root.winfo_y() + root.winfo_height() // 2 - 100))
        next_level.title("Молодец!")
        next_level.grab_set()  # Захват фокуса для нового окна
        
        # Загрузка фонового изображения
        background_image = Image.open("D:\Code\CBeTbl\Igra\game\ext.bmp")
        background_photo = ImageTk.PhotoImage(background_image)
        
        # Создание виджета Label с фоновым изображением
        background_label = tk.Label(next_level, image=background_photo)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Создание кнопки "Следующий уровень"
        button = tk.Button(next_level, text="Следующий уровень", command=new_level, width=18, height=1, highlightthickness=0, cursor="hand2", bg="#FFFFFF", font=("TkDefaultFont", 14))
        button.place(x=150, y=49)
        button.configure(relief=tk.FLAT)
        button.pack()
        next_level.mainloop()
    
    
  



def on_closing():
    # Обработчик события закрытия окна
    # Здесь вы можете добавить логику или очистку перед закрытием
    # Здесь я просто печатаю сообщение перед закрытием окна
    label = tk.Label(root, text="Не уходи...")
    label.pack()
    root.after(1000, root.destroy)  # Закрыть окно через 5 секунд (2000 миллисекунд)

def open_new_window():
    global new_window

    # Создание нового окна
    new_window = tk.Toplevel(root)
    new_window.attributes("-topmost", True)
    new_window.geometry("200x200+{}+{}".format(root.winfo_x() + root.winfo_width() // 2 - 100, root.winfo_y() + root.winfo_height() // 2 - 100))
    new_window.title("Комп")

    # Загрузка и установка фонового изображения
    background_image = Image.open("D:\Code\CBeTbl\Igra\game\windows.png")
    background_photo = ImageTk.PhotoImage(background_image)
    background_label = tk.Label(new_window, image=background_photo)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    new_window.grab_set()
    new_window.iconbitmap("D:\\Code\\CBeTbl\\Igra\\game\\photo_2023-05-28_22-20-54.ico")


    # Создание четырех кнопок в новом окне
    #button1 = tk.Button(new_window, text="Поиграть в игру", command=play_game)
    #button1.pack()

    #button2 = tk.Button(new_window, text="Поучиться", command=study)
    #button2.pack()

    

    button4 = tk.Button(new_window, text="Написать жене", command=pismo)
    button4.pack()

    button5 = tk.Button(new_window, text="выход", command=new_window.destroy)
    button5.pack()

    new_window.mainloop()

def open_third_window():
    global third_window

    # Создание нового окна
    third_window = tk.Toplevel(root)
    third_window.attributes("-topmost", True)
    third_window.geometry("200x200+{}+{}".format(root.winfo_x() + root.winfo_width() // 2 - 100, root.winfo_y() + root.winfo_height() // 2 - 100))
    third_window.title("Комп")

    # Загрузка и установка фонового изображения
    background_image = Image.open("D:\Code\CBeTbl\Igra\game\music.jpg")
    background_photo = ImageTk.PhotoImage(background_image)
    background_label = tk.Label(third_window, image=background_photo)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    third_window.grab_set()
    third_window.iconbitmap("D:\\Code\\CBeTbl\\Igra\\game\\photo_2023-05-28_22-20-54.ico")


    # Создание четырех кнопок в новом окне
    #button1 = tk.Button(new_window, text="Поиграть в игру", command=play_game)
    #button1.pack()

    #button2 = tk.Button(new_window, text="Поучиться", command=study)
    #button2.pack()

    

    button4 = tk.Button(third_window, text="Поиграть на гитаре", command=gitara)
    button4.pack()

    button5 = tk.Button(third_window, text="выход", command=third_window.destroy)
    button5.pack()

    
    third_window.mainloop()


def open_four_window():
    global four_window
    four_window = tk.Toplevel(root)  # Создание четвертого окна с помощью Toplevel()
    four_window.attributes("-topmost", True)  # Установка нового окна поверх родительского
    four_window.geometry("600x200+{}+{}".format(root.winfo_x() + root.winfo_width() // 2 - 100, root.winfo_y() + root.winfo_height() // 2 - 100))
    four_window.title("Инструкции")
    four_window.grab_set()  # Захват фокуса для нового окна
    four_window.iconbitmap("D:\Code\CBeTbl\Igra\game\photo_2023-05-28_22-20-54.ico")
    label = tk.Label(four_window, text="""Статы не ниже нуля. Статы > 10 = Следующий уровень.\n Люди, которые занимаются спортом, обладают массой преимуществ. \n Они совершенно по-другому смотрят на жизнь и воспринимают себя. В обществе чувствуют себя увереннее и сильнее. Они начинают по-настоящему радоваться жизни и получать удовольствие от каждого мгновения.\n Старайтесь и вы бывать на свежем воздухе каждый день не менее часа, и тогда вы забудете такие слова, как лишние килограммы, бессонница, депрессия, стрессы и даже медицина!\nПОМНИТЕ:
    Деньги потерял — ничего не потерял, время потерял — многое потерял, \n Здоровье потерял — всё потерял. """, justify="left", wraplength=four_window.winfo_width())
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



def open_six_window():
    global six_window

    # Создание нового окна
    six_window = tk.Toplevel(root)
    six_window.attributes("-topmost", True)
    six_window.geometry("200x200+{}+{}".format(root.winfo_x() + root.winfo_width() // 2 - 100, root.winfo_y() + root.winfo_height() // 2 - 100))
    six_window.title("Турник")

    # Загрузка и установка фонового изображения
    background_image = Image.open("D:\Code\CBeTbl\Igra\game\IMG_0283-700x899.jpg")
    background_photo = ImageTk.PhotoImage(background_image)
    background_label = tk.Label(six_window, image=background_photo)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    six_window.grab_set()
    six_window.iconbitmap("D:\\Code\\CBeTbl\\Igra\\game\\photo_2023-05-28_22-20-54.ico")


    # Создание четырех кнопок в новом окне
    button1 = tk.Button(six_window, text="Вкачать руки-базуки", command=play_game)
    button1.pack()


    button2 = tk.Button(six_window, text="выход", command=six_window.destroy)
    button2.pack()
    six_window.mainloop()
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

music_file = "D:\Code\CBeTbl\Igra\game\Alexei Kalinkin - Animals.mp3"  # Укажите путь к вашему музыкальному файлу




# Создание кнопки



def play_music():
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play()
def stop_music():
    pygame.mixer.music.stop()
# Здесь должен быть код, который обрабатывает события кнопки
# Например:
button12 = tk.Button(root, text=" ", command=stop_music, width=1, height=1, highlightthickness=0, cursor="hand2", bg="#1D1D1D", font=("TkDefaultFont", 6))
button12.place(x=900, y=310)
button12.configure(relief=tk.FLAT)

button1 = tk.Button(root, text=" ", command=play_music, width=1, height=1, highlightthickness=0, cursor="hand2", bg="#1D1D1D", font=("TkDefaultFont", 6))
button1.place(x=850, y=315)
button1.configure(relief=tk.FLAT)

button = tk.Button(root, text=" ", command=open_new_window, width=1, height=1, highlightthickness=0, cursor="hand2", bg="#1D1D1D", font=("TkDefaultFont", 6))
button.place(x=761, y=349)
button.configure(relief=tk.FLAT)

button = tk.Button(root, text=" ", command=open_third_window, width=6, height=1, highlightthickness=0, cursor="hand2", bg="#C09B74", font=("TkDefaultFont", 14))
button.place(x=95, y=650)
button.configure(relief=tk.FLAT)

button = tk.Button(root, text=" ", command=open_six_window, width=1, height=1, highlightthickness=0, cursor="hand2", bg="#9A9A9A", font=("TkDefaultFont", 14))
button.place(x=170, y=64)
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

