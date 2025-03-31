
from graphics import *
import color_code_calcs

def update_col(col, btn):
    # update the current button that is "pressed" to btn
    for button in col:
        button.configure(relief= "raised")
    btn.configure(relief="ridge")

def update_col1(btn):
    update_col(column1, btn)

def update_col2(btn):
    update_col(column2, btn)

def update_col3(btn):
    update_col(column3, btn)

def update_col4(btn):
    update_col(column4, btn)


# column 1
button21.configure(command= lambda: update_col1(button21))
button31.configure(command= lambda: update_col1(button31))
button41.configure(command= lambda: update_col1(button41))
button51.configure(command= lambda: update_col1(button51))
button61.configure(command= lambda: update_col1(button61))
button71.configure(command= lambda: update_col1(button71))
button81.configure(command= lambda: update_col1(button81))
button91.configure(command= lambda: update_col1(button91))
button101.configure(command= lambda: update_col1(button101))

# column 2
button12.configure(command= lambda: update_col2(button12))
button22.configure(command= lambda: update_col2(button22))
button32.configure(command= lambda: update_col2(button32))
button42.configure(command= lambda: update_col2(button42))
button52.configure(command= lambda: update_col2(button52))
button62.configure(command= lambda: update_col2(button62))
button72.configure(command= lambda: update_col2(button72))
button82.configure(command= lambda: update_col2(button82))
button92.configure(command= lambda: update_col2(button92))
button102.configure(command= lambda: update_col2(button102))

# column 3
button13.configure(command= lambda: update_col3(button13))
button23.configure(command= lambda: update_col3(button23))
button33.configure(command= lambda: update_col3(button33))
button43.configure(command= lambda: update_col3(button43))
button53.configure(command= lambda: update_col3(button53))
button63.configure(command= lambda: update_col3(button63))
button73.configure(command= lambda: update_col3(button73))
button83.configure(command= lambda: update_col3(button83))
button93.configure(command= lambda: update_col3(button93))
button103.configure(command= lambda: update_col3(button103))
button113.configure(command= lambda: update_col3(button113))
button123.configure(command= lambda: update_col3(button123))
button133.configure(command= lambda: update_col3(button133))

# column 4
button24.configure(command= lambda: update_col4(button24))
button34.configure(command= lambda: update_col4(button34))
button44.configure(command= lambda: update_col4(button44))
button54.configure(command= lambda: update_col4(button54))
button64.configure(command= lambda: update_col4(button64))
button74.configure(command= lambda: update_col4(button74))
button84.configure(command= lambda: update_col4(button84))
button94.configure(command= lambda: update_col4(button94))
button114.configure(command= lambda: update_col4(button114))
button124.configure(command= lambda: update_col4(button124))



