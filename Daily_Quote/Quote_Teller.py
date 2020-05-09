import os
import random
from tkinter import *
from csv import DictReader
from datetime import datetime

os.chdir('/home/hemant/PycharmProjects/Daily_Quote')

data = open('Quotes_02.csv', 'r')

thoughts = []
writer = []
file = DictReader(data)

for row in file:
    thoughts.append(row['QUOTE'])
    writer.append(row['AUTHOR'])

random_initialize = random.randint(0, len(thoughts) - 1)

thought_for_the_day = thoughts[random_initialize]

i = 1
thought = []
temp = ''
for text in thought_for_the_day.split():
    temp += ' ' + text
    if i == 5:
        thought.append(temp)
        temp = ''
        i = 0
    i += 1

thought.append(temp)
thought.append(f' = {writer[random_initialize]}')

window = Tk()
window.geometry('550x400+260+140')
window.resizable(0, 0)
window.title('Thought Of The Day')

good_morning_image = PhotoImage(file='~/PycharmProjects/Daily_Quote/image/good_morning.png')
good_afternoon_image = PhotoImage(file='~/PycharmProjects/Daily_Quote/image/good_afternoon.png')
good_evening_image = PhotoImage(file='~/PycharmProjects/Daily_Quote/image/good_evening.png')

if len(thought) > 6:
    window.geometry('550x450+260+140')
if len(thought) > 8:
    window.geometry('550x500+260+130')
if len(thought) > 10:
    window.geometry('550x550+260+120')
if len(thought) > 12:
    window.geometry('550x620+260+100')

time = datetime.now().strftime('%H hours and %M minutes')
time_list = time.split()
if int(time_list[0]) < 12:
    current_image = good_morning_image
elif int(time_list[0]) > 12 and int(time_list[0]) < 17:
    current_image = good_afternoon_image
else:
    current_image = good_evening_image

Label(window, image=current_image).pack()

title_image = PhotoImage(file='~/PycharmProjects/Daily_Quote/image/title_image.png')
Label(window, image=title_image).pack(side=LEFT)

thought = '\n'.join(thought)
th = thought.replace("=", "-by")

Label(window, text=th, font=('Caviar Dreams', 15)).place(x=150, y=230)

window.mainloop()
