import ttkbootstrap as ttk
from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import showerror, askyesno
from tkinter import colorchooser
from PIL import Image, ImageOps, ImageTk, ImageFilter, ImageGrab


def apply_filter(filter):
    global image, photo_image
    try:
        if is_flipped:

            flipped_image = Image.open(file_path).transpose(Image.FLIP_LEFT_RIGHT)

            rotated_image = flipped_image.rotate(rotation_angle)

            if filter == "Black and White":
                rotated_image = ImageOps.grayscale(rotated_image)
            elif filter == "Blur":
                rotated_image = rotated_image.filter(ImageFilter.BLUR)
            elif filter == "Contour":
                rotated_image = rotated_image.filter(ImageFilter.CONTOUR)
            elif filter == "Detail":
                rotated_image = rotated_image.filter(ImageFilter.DETAIL)
            elif filter == "Emboss":
                rotated_image = rotated_image.filter(ImageFilter.EMBOSS)
            elif filter == "Edge Enhance":
                rotated_image = rotated_image.filter(ImageFilter.EDGE_ENHANCE)
            elif filter == "Sharpen":
                rotated_image = rotated_image.filter(ImageFilter.SHARPEN)
            elif filter == "Smooth":
                rotated_image = rotated_image.filter(ImageFilter.SMOOTH)
            else:
                rotated_image = Image.open(file_path).transpose(Image.FLIP_LEFT_RIGHT).rotate(rotation_angle) #?
        elif rotation_angle != 0:

            rotated_image = Image.open(file_path).rotate(rotation_angle)

            if filter == "Black and White":
                rotated_image = ImageOps.grayscale(rotated_image)
            elif filter == "Blur":
                rotated_image = rotated_image.filter(ImageFilter.BLUR)
            elif filter == "Contour":
                rotated_image = rotated_image.filter(ImageFilter.CONTOUR)
            elif filter == "Detail":
                rotated_image = rotated_image.filter(ImageFilter.DETAIL)
            elif filter == "Emboss":
                rotated_image = rotated_image.filter(ImageFilter.EMBOSS)
            elif filter == "Edge Enhance":
                rotated_image = rotated_image.filter(ImageFilter.EDGE_ENHANCE)
            elif filter == "Sharpen":
                rotated_image = rotated_image.filter(ImageFilter.SHARPEN)
            elif filter == "Smooth":
                rotated_image = rotated_image.filter(ImageFilter.SMOOTH)
            else:
                rotated_image = Image.open(file_path).rotate(rotation_angle)
        else:
            image = Image.open(file_path)
            if filter == "Black and White":
                image = ImageOps.grayscale(image)
            elif filter == "Blur":
                image = image.filter(ImageFilter.BLUR)
            elif filter == "Sharpen":
                image = image.filter(ImageFilter.SHARPEN)
            elif filter == "Smooth":
                image = image.filter(ImageFilter.SMOOTH)
            elif filter == "Emboss":
                image = image.filter(ImageFilter.EMBOSS)
            elif filter == "Detail":
                image = image.filter(ImageFilter.DETAIL)
            elif filter == "Edge Enhance":
                image = image.filter(ImageFilter.EDGE_ENHANCE)
            elif filter == "Contour":
                image = image.filter(ImageFilter.CONTOUR)
            rotated_image = image

        new_width = int((WIDTH / 2))
        rotated_image = rotated_image.resize((new_width, HEIGHT), Image.LANCZOS)

        photo_image = ImageTk.PhotoImage(rotated_image)
        canvas.create_image(0, 0, anchor="nw", image=photo_image)
    except:
        showerror(title='Ошибка', message='Пожалуйста, сначала выберите изображение!')


def open_image():
    root=ttk.Window()
    root.title("")
    root.geometry('300x300+1150+80')
    button1=ttk.Button(root, text='Выберите изображение', command=select_image)
    button1.pack(side=LEFT,padx=10, pady=50)
    button2=ttk.Button(root,text='Создать новый', command=create_new)
    button2.pack(side=RIGHT,padx=10,pady=50)
    root.mainloop()


def select_image():
    global file_path
    file_path = filedialog.askopenfilename(title='Открыть файл изображения', filetypes=[('ImageFiles','*.jpg;*.jpeg;*.png;*.gif;*.bmp')], initialdir='C:\ ')
    if file_path:
        global image, photo_image
        image = Image.open(file_path)
        new_width=int((WIDTH/2))
        image=image.resize((new_width,HEIGHT),Image.LANCZOS)

        image=ImageTk.PhotoImage(image)
        canvas.create_image(0,0,anchor='nw', image=image)


def create_new():
    global file_path
    file_path = filedialog.askopenfilename(title='Открыть файл изображения',filetypes=[('ImageFiles', '*.jpg;*.jpeg;*.png;*.gif;*.bmp')],initialdir="C:\pythonProject\canvas")
    if file_path:
        global image, photo_image
        image = Image.open(file_path)
        new_width = int((WIDTH / 2))
        image = image.resize((new_width, HEIGHT), Image.LANCZOS)

        image = ImageTk.PhotoImage(image)
        canvas.create_image(0, 0, anchor='nw', image=image)


is_flipped = False
def flip_image():
    try:
        global image, photo_image, is_flipped
        if not is_flipped:
            image = Image.open(file_path).transpose(Image.FLIP_LEFT_RIGHT)
            is_flipped = True
        else:
            image = Image.open(file_path)
            is_flipped = False

        new_width = int((WIDTH / 2))
        image = image.resize((new_width, HEIGHT), Image.LANCZOS)

        photo_image = ImageTk.PhotoImage(image)
        canvas.create_image(0, 0, anchor="nw", image=photo_image)
    except:
        showerror(title='Ошибка переворота изображения', message='Пожалуйста, выберите изображение, которое нужно перевернуть!')


rotation_angle = 0
def rotate_image():
    try:
        global image, photo_image,rotation_angle
        image=Image.open(file_path)
        new_width = int((WIDTH / 2))
        image = image.resize((new_width, HEIGHT), Image.LANCZOS)
        rotated_image=image.rotate(rotation_angle+90)
        rotation_angle+=90
        if rotation_angle %360==0:
            rotation_angle=0
            image = Image.open(file_path)
            image = image.resize((new_width, HEIGHT), Image.LANCZOS)
            rotated_image=image
        photo_image=ImageTk.PhotoImage(rotated_image)
        canvas.create_image(0,0, anchor='nw',image=photo_image)
    except:
        showerror(title='Ошибка поворота изображения', message='Пожалуйста, выберите изображение для поворота!')


def draw(event):
    global file_path
    if file_path:
        x1, y1 = (event.x-pen_size),(event.y - pen_size)
        x2, y2 = (event.x + pen_size), (event.y + pen_size)
        canvas.create_oval(x1,y1,x2,y2,fill=pen_color,outline="",width=pen_size, tags='oval')


def change_color():
    global pen_color
    pen_color=colorchooser.askcolor(title="Выберите цвет пера")[1]


def back():
    global file_path
    if file_path:
        canvas.delete('oval')

def erase_wh(event):
    global file_path
    if file_path:
        x1, y1 = (event.x - pen_size), (event.y - pen_size)
        x2, y2 = (event.x + pen_size), (event.y + pen_size)
        canvas.create_oval(x1, y1, x2, y2, fill='WHITE', outline="", width=pen_size, tags='oval')


def save_image():
    global file_path,is_flipped,rotation_angle
    if file_path:
        #grab
        image=ImageGrab.grab(bbox=(canvas.winfo_rootx(), canvas.winfo_rooty() ,canvas.winfo_rootx()+canvas.winfo_width(),canvas.winfo_rooty()+canvas.winfo_height()))
        if is_flipped or rotation_angle % 360 != 0:
            new_width=int((WIDTH/2))
            image=image.resize((new_width,HEIGHT),Image.LANCZOS)
            if is_flipped:
                image=image.transpose(Image.FLIP_LEFT_RIGHT)
            if rotation_angle %360 != 0:
                image=image.rotate(rotation_angle)



        filter=filter_combobox.get()
        if filter:
            if filter == "Black and White":
                image=ImageOps.grayscale(image)
            elif filter=="Blur":
                image=image.filter(ImageFilter.BLUR)
            elif filter=="Sharpen":
                image=image.filter(ImageFilter.SHARPEN)
            elif filter=="Smooth":
                image=image.filter(ImageFilter.SMOOTH)
            elif filter=="Emboss":
                image=image.filter(ImageFilter.EMBOSS)
            elif filter=="Detail":
                image=image.filter(ImageFilter.DETAIL)
            elif filter=="Edge Enhance":
                image=image.filter(ImageFilter.EDGE_ENHANCE)
            elif filter=="Contour":
                image=image.filter(ImageFilter.CONTOUR)



        file_path=filedialog.askopenfilename(defaultextension='.jpg')

        if file_path:
            if askyesno(title='Сохранить картинку',message='Вы хотите сохранить картинку?'):
               image.save(file_path)


win=ttk.Window()
win.title("Графический редактор")
win.geometry('580x580+1150+80')
icon = ttk.PhotoImage(file="editor.png")
win.iconphoto(False,icon)



WIDTH = 850
HEIGHT = 560
file_path = ""
pen_size = 3
pen_color = "black"

left_frame = ttk.Frame(win, width=200, height=600)
left_frame.pack(side="left", fill="y")

canvas = ttk.Canvas(win, width=WIDTH, height=HEIGHT)
canvas.pack()
canvas.bind("<B1-Motion>",draw)
canvas.bind("<B3-Motion>",erase_wh)


filter_label = ttk.Label(left_frame, text="Выберите Фильтр:", background="white")
filter_label.pack(padx=0, pady=2)

image_filters = ["Contour", "Black and White", "Blur", "Detail", "Emboss", "Edge Enhance", "Sharpen", "Smooth"]

filter_combobox = ttk.Combobox(left_frame, values=image_filters, width=15)
filter_combobox.pack(padx=10, pady=5)
filter_combobox.bind('<<ComboboxSelected>>', lambda event: apply_filter(filter_combobox.get()))#???lambda


image_icon=ttk.PhotoImage(file='add.png').subsample(12,12)
flip_icon=ttk.PhotoImage(file='flip.png').subsample(6,6)
rotate_icon=ttk.PhotoImage(file='rotate.png').subsample(6,6)
color_icon=ttk.PhotoImage(file='color.png').subsample(6,6)
back_icon=ttk.PhotoImage(file='back.png').subsample(5, 5)
save_icon=ttk.PhotoImage(file='saves.png').subsample(4,4)


image_button=ttk.Button(left_frame, image=image_icon,bootstyle='light', command=open_image)
image_button.pack(pady=10)

flip_button=ttk.Button(left_frame, image=flip_icon,bootstyle='light', command=flip_image)
flip_button.pack(pady=10)

rotate_button=ttk.Button(left_frame,image=rotate_icon,bootstyle='light', command=rotate_image)
rotate_button.pack(pady=10)

color_button=ttk.Button(left_frame,image=color_icon,bootstyle='light',command=change_color)
color_button.pack(pady=10)

back_button=ttk.Button(left_frame,image=back_icon, bootstyle='light',command=back)
back_button.pack(pady=10)

save_button=ttk.Button(left_frame,image=save_icon,bootstyle='light',command=save_image)
save_button.pack(pady=10)
win.mainloop()