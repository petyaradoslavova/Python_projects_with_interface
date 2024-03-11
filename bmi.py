from tkinter import StringVar,IntVar,Label
from tkinter import messagebox
import customtkinter

app = customtkinter.CTk()
app.geometry("300x460")
app.maxsize(300,460)
app.minsize(300,460)

app.title("BMI Calculator")
app.config(bg='black')

top = Label(app, text=' Adult BMI Calculator', font=('Arial', 20, 'bold'), fg='#FFFFFF', bg='#181935', width=30, height=1,
            pady=5)
top.pack()

height_label = Label(app, font=('Arial', 20, 'bold'), fg='#FFFFFF', bg='#181935', width=24, height=4,)
height_label.place(x=20, y=60)

height_text_label = Label(app, text='Height cm', font=('Arial', 20, 'bold',), fg='#FFFFFF', bg='#181935', width=10,
                          height=1, )
height_text_label.place(x=140, y=70)

weight_label = Label(app, font=('Arial', 20, 'bold'), fg='#FFFFFF', bg='#181935', width=24, height=4)
weight_label.place(x=20, y=210)

weight_text_label = Label(app, text='Weight kg', font=('Arial', 20, 'bold'), fg='#FFFFFF', bg='#181935', width=10,
                          height=1)
weight_text_label.place(x=140, y=220)

height = StringVar()
weight = StringVar()

height_value = IntVar()
weight_value = IntVar()

text = StringVar()


def get_height_value():
    return height_value.get()


def slider1(event):
    return height.set(str(get_height_value()))


def get_weight_value():
    return weight_value.get()


def slider2(event):
    return weight.set(str(get_weight_value()))


height_entry = customtkinter.CTkEntry(app, textvariable=height,
                                      bg_color='#181935',
                                      fg_color='#181935',
                                      border_width=0, font=('Arial', 20, 'bold'))

height_entry.place(x=130, y=80)

weight_entry = customtkinter.CTkEntry(app, textvariable=weight,
                                      bg_color='#181935',
                                      fg_color='#181935',
                                      border_width=0, font=('Arial', 20, 'bold'))

weight_entry.place(x=130, y=180)

height_slider = customtkinter.CTkSlider(app, variable=height_value, from_=0, to=260, width=260, bg_color='#181935',
                                        fg_color='#FFFFFF',
                                        button_hover_color='#bf0d97', command=slider1)
height_slider.place(x=20, y=108)

weight_slider = customtkinter.CTkSlider(app, variable=weight_value, from_=0, to=500, width=260, bg_color='#181935',
                                        fg_color='#FFFFFF',
                                        button_hover_color='#bf0d97', command=slider2)
weight_slider.place(x=20, y=209)


def bmi():
    global bmi
    try:
        cm = int(height_entry.get())
        m = (cm / 100) * (cm / 100)
        kg = int(weight_entry.get())
        bmi = float(format(kg / m))
        if bmi <= 18.5:
            text.set('Underweight')
        elif bmi <= 24.5:
             text.set('Normal weight')
        elif bmi <= 29.9:
            text.set('Overweight')
        elif bmi <= 34.9:
              text.set('Class I Obesity')
        elif bmi <= 39.9:
              text.set('Class II Obesity')
        else:
              text.set('Class III Obesity')
    except:
        messagebox.showerror(title='Error',message='Height or weight cannot be 0 !')

    result1 = customtkinter.CTkLabel(app, text=f'BMI: {bmi:.2f}', font=('Arial', 33, 'bold'),bg_color='black')
    result1.place(x=65, y=350)

    result2 = customtkinter.CTkLabel(app, textvariable=text, font=('Arial', 16, 'bold'),bg_color='black')
    result2.place(x=92, y=400)


calc_button=customtkinter.CTkButton(app,text='Calculate',command=bmi,
                                    width=170,
                                    height=50,
                                    font=('Arial',20,'bold'),
                                    fg_color='#bf0d97',
                                    hover_color='#006994',
                                    )
calc_button.place(x=63,y=270)

app.mainloop()
