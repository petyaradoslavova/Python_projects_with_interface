import tkinter as tk
import json
import urllib.request
from io import BytesIO
from PIL import ImageTk, Image

import requests


def display_image(image_url):
    with urllib.request.urlopen(image_url) as url:
        image_data = url.read()

    image_stream = BytesIO(image_data)

    image = ImageTk.PhotoImage(Image.open(image_stream))

    image_label.config(image=image)
    image_label.image = image


def get_image_url():
    headers = {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMWM3OTIwMDAtZDgxYy00YTQ2LWIzN2UtMWJkMWY5M2I4YzRmIiwidHlwZSI6ImFwaV90b2tlbiJ9.HUyMbH5VA9Igdls-gHC2h72MvYfuD5lRYyCOt3q6Owo"}

    url = "https://api.edenai.run/v2/image/generation"
    payload = {
        "providers": "openai",
        "text": input_field.get(),
        "resolution": "256x256",
        "fallback_providers": ""
    }

    response = requests.post(url, json=payload, headers=headers)
    result = json.loads(response.text)
    return (result['openai']['items'][0]["image_resource_url"])


def render_image():
    try:
        error_label.place_forget()
        image_url = get_image_url()
    except KeyError:
        error_label.place(x=175,y=50)
    else:
        display_image(image_url)


window = tk.Tk()
window.title('AI Image Generator')
window.geometry("500x350")
window.configure(bg='black')

error_label = tk.Label(window,text="Prompt cannot be empty!",fg="red",bg='black')

input_field = tk.Entry(window,width=20)
input_field.place(x=165,y=20)

image_label = tk.Label(window,bg='black')
image_label.place(x=125,y=70)

generate_button = tk.Button(window,text = "Create",height=1,command=render_image,bg='white',fg='black')
generate_button.place(x=300,y=17)

window.mainloop()