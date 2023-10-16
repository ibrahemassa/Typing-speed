from tkinter import *
import requests
import spacy
import time


response = requests.get('https://api.kanye.rest')
quote = response.json()['quote']
nlp = spacy.load("en_core_web_sm")
start_time = time.time()


def check_sim(event):
    global quote
    global start_time

    txt = input_box.get()
    doc1 = nlp(quote)
    doc2 = nlp(txt)
    similarity = abs(doc1.similarity(doc2) * 100)
    end_time = time.time()
    elapsed_time = end_time - start_time
    words = txt.split()
    words_count = len(words)
    wpm = int(words_count*60/elapsed_time)
    sim_text.config(text=f'{similarity:.1f}%\n{wpm} WPM.', font=("Helvetica", 20))


def restart_program():
    global quote
    global start_time
    global response

    response = requests.get('https://api.kanye.rest')
    quote = response.json()['quote']
    quote_label.config(text=quote)
    start_time = time.time()
    sim_text.config(text='')
    input_box.delete(0, 'end')


window = Tk()
window.title('Typing speed test')
window.config(padx=30, pady=20)
window.minsize(500, 500)

quote_label = Label(text=quote, font=("Helvetica", 20), fg='red')
quote_label.pack(fill="both", expand=True)

hint = Label(text='Press Enter to submit!')
hint.pack()

input_box = Entry(window, font=("Helvetica", 20))
input_box.pack(fill=X, expand=True)
input_box.bind("<Return>", check_sim)


sim_text = Label()
sim_text.pack()

restart_btn = Button(text='Restart!!', command=restart_program)
restart_btn.pack()

window.mainloop()