
import tkinter as tk

screen = tk.Tk(screenName= "Resistor Color Code Calculator")

BUTTON_WIDTH = 10
BUTTONS_ROW_ONE = 2

# default pressed is 10k with 5% tolerance

# column (digit) 1

button21 = tk.Button(text= "1", bg= "BROWN", fg= "white", width= BUTTON_WIDTH, bd= 5, relief= "ridge")
button31 = tk.Button(text= "2", bg= "RED", fg= "white", width= BUTTON_WIDTH, bd= 5)
button41 = tk.Button(text= "3", bg= "ORANGE", fg= "white", width= BUTTON_WIDTH, bd= 5)
button51 = tk.Button(text= "4", bg= "YELLOW", fg= "BLACK", width= BUTTON_WIDTH, bd= 5)
button61 = tk.Button(text= "5", bg= "GREEN", fg= "white", width= BUTTON_WIDTH, bd= 5)
button71 = tk.Button(text= "6", bg= "BLUE", fg= "white", width= BUTTON_WIDTH, bd= 5)
button81 = tk.Button(text= "7", bg= "PURPLE", fg= "white", width= BUTTON_WIDTH, bd= 5)
button91 = tk.Button(text= "8", bg= "GRAY", fg= "white", width= BUTTON_WIDTH, bd= 5)
button101 = tk.Button(text= "9", bg= "WHITE", fg= "BLACK", width= BUTTON_WIDTH, bd= 5)

button21.grid(row= BUTTONS_ROW_ONE + 1, column= 2)
button31.grid(row= BUTTONS_ROW_ONE + 2, column= 2)
button41.grid(row= BUTTONS_ROW_ONE + 3, column= 2)
button51.grid(row= BUTTONS_ROW_ONE + 4, column= 2)
button61.grid(row= BUTTONS_ROW_ONE + 5, column= 2)
button71.grid(row= BUTTONS_ROW_ONE + 6, column= 2)
button81.grid(row= BUTTONS_ROW_ONE + 7, column= 2)
button91.grid(row= BUTTONS_ROW_ONE + 8, column= 2)
button101.grid(row= BUTTONS_ROW_ONE + 9, column= 2)

column1 = [
    button21,
    button31,
    button41,
    button51,
    button61,
    button71,
    button81,
    button91,
    button101
]


# column (digit) 2

button12 = tk.Button(text= "0", bg= "BLACK", fg= "white", width= BUTTON_WIDTH, bd= 5, relief= "ridge")
button22 = tk.Button(text= "1", bg= "BROWN", fg= "white", width= BUTTON_WIDTH, bd= 5)
button32 = tk.Button(text= "2", bg= "RED", fg= "white", width= BUTTON_WIDTH, bd= 5)
button42 = tk.Button(text= "3", bg= "ORANGE", fg= "white", width= BUTTON_WIDTH, bd= 5)
button52 = tk.Button(text= "4", bg= "YELLOW", fg= "BLACK", width= BUTTON_WIDTH, bd= 5)
button62 = tk.Button(text= "5", bg= "GREEN", fg= "white", width= BUTTON_WIDTH, bd= 5)
button72 = tk.Button(text= "6", bg= "BLUE", fg= "white", width= BUTTON_WIDTH, bd= 5)
button82 = tk.Button(text= "7", bg= "PURPLE", fg= "white", width= BUTTON_WIDTH, bd= 5)
button92 = tk.Button(text= "8", bg= "GRAY", fg= "white", width= BUTTON_WIDTH, bd= 5)
button102 = tk.Button(text= "9", bg= "white", fg= "BLACK", width= BUTTON_WIDTH, bd= 5)

button12.grid(row= BUTTONS_ROW_ONE, column= 3)
button22.grid(row= BUTTONS_ROW_ONE + 1, column= 3)
button32.grid(row= BUTTONS_ROW_ONE + 2, column= 3)
button42.grid(row= BUTTONS_ROW_ONE + 3, column= 3)
button52.grid(row= BUTTONS_ROW_ONE + 4, column= 3)
button62.grid(row= BUTTONS_ROW_ONE + 5, column= 3)
button72.grid(row= BUTTONS_ROW_ONE + 6, column= 3)
button82.grid(row= BUTTONS_ROW_ONE + 7, column= 3)
button92.grid(row= BUTTONS_ROW_ONE + 8, column= 3)
button102.grid(row= BUTTONS_ROW_ONE + 9, column= 3)

column2 = {
    button12,
    button22,
    button32,
    button42,
    button52,
    button62,
    button72,
    button82,
    button92,
    button102
}

# column 3 (multiplier)

button13 = tk.Button(text= "10^0", bg= "BLACK", fg= "white", width= BUTTON_WIDTH, bd= 5)
button23 = tk.Button(text= "10^1", bg= "BROWN", fg= "white", width= BUTTON_WIDTH, bd= 5)
button33 = tk.Button(text= "10^2", bg= "RED", fg= "white", width= BUTTON_WIDTH, bd= 5)
button43 = tk.Button(text= "10^3", bg= "ORANGE", fg= "white", width= BUTTON_WIDTH, bd= 5, relief= "ridge")
button53 = tk.Button(text= "10^4", bg= "YELLOW", fg= "BLACK", width= BUTTON_WIDTH, bd= 5)
button63 = tk.Button(text= "10^5", bg= "GREEN", fg= "white", width= BUTTON_WIDTH, bd= 5)
button73 = tk.Button(text= "10^6", bg= "BLUE", fg= "white", width= BUTTON_WIDTH, bd= 5)
button83 = tk.Button(text= "10^7", bg= "PURPLE", fg= "white", width= BUTTON_WIDTH, bd= 5)
button93 = tk.Button(text= "10^8", bg= "GRAY", fg= "white", width= BUTTON_WIDTH, bd= 5)
button103 = tk.Button(text= "10^9", bg= "white", fg= "BLACK", width= BUTTON_WIDTH, bd= 5)
button113 = tk.Button(text= "10^-1", bg= "GOLD", fg= "BLACK", width= BUTTON_WIDTH, bd= 5)
button123 = tk.Button(text= "10^-2", bg= "SILVER", fg= "BLACK", width= BUTTON_WIDTH, bd= 5)
button133 = tk.Button(text= "10^-3", bg= "PINK", fg= "BLACK", width= BUTTON_WIDTH, bd= 5)


button13.grid(row= BUTTONS_ROW_ONE, column= 4)
button23.grid(row= BUTTONS_ROW_ONE + 1, column= 4)
button33.grid(row= BUTTONS_ROW_ONE + 2, column= 4)
button43.grid(row= BUTTONS_ROW_ONE + 3, column= 4)
button53.grid(row= BUTTONS_ROW_ONE + 4, column= 4)
button63.grid(row= BUTTONS_ROW_ONE + 5, column= 4)
button73.grid(row= BUTTONS_ROW_ONE + 6, column= 4)
button83.grid(row= BUTTONS_ROW_ONE + 7, column= 4)
button93.grid(row= BUTTONS_ROW_ONE + 8, column= 4)
button103.grid(row= BUTTONS_ROW_ONE + 9, column= 4)
button113.grid(row= BUTTONS_ROW_ONE + 10, column= 4)
button123.grid(row= BUTTONS_ROW_ONE + 11, column= 4)
button133.grid(row= BUTTONS_ROW_ONE + 12, column= 4)

column3 = {
    button13,
    button23,
    button33,
    button43,
    button53,
    button63,
    button73,
    button83,
    button93,
    button103,
    button113,
    button123,
    button133
}


# column 4 (tolerance)

button24 = tk.Button(text= "±1%", bg= "BROWN", fg= "white", width= BUTTON_WIDTH, bd= 5)
button34 = tk.Button(text= "±2%", bg= "RED", fg= "white", width= BUTTON_WIDTH, bd= 5)
button44 = tk.Button(text= "±0.05%", bg= "ORANGE", fg= "white", width= BUTTON_WIDTH, bd= 5)
button54 = tk.Button(text= "±0.02%", bg= "YELLOW", fg= "BLACK", width= BUTTON_WIDTH, bd= 5)
button64 = tk.Button(text= "±0.5%", bg= "GREEN", fg= "white", width= BUTTON_WIDTH, bd= 5)
button74 = tk.Button(text= "±0.25%", bg= "BLUE", fg= "white", width= BUTTON_WIDTH, bd= 5)
button84 = tk.Button(text= "±0.1%", bg= "PURPLE", fg= "white", width= BUTTON_WIDTH, bd= 5)
button94 = tk.Button(text= "±0.01%", bg= "GRAY", fg= "white", width= BUTTON_WIDTH, bd= 5)
button114 = tk.Button(text= "±5%", bg= "GOLD", fg= "BLACK", width= BUTTON_WIDTH, bd= 5, relief= "ridge")
button124 = tk.Button(text= "±10%", bg= "SILVER", fg= "BLACK", width= BUTTON_WIDTH, bd= 5)


button24.grid(row= BUTTONS_ROW_ONE + 1, column= 5)
button34.grid(row= BUTTONS_ROW_ONE + 2, column= 5)
button44.grid(row= BUTTONS_ROW_ONE + 3, column= 5)
button54.grid(row= BUTTONS_ROW_ONE + 4, column= 5)
button64.grid(row= BUTTONS_ROW_ONE + 5, column= 5)
button74.grid(row= BUTTONS_ROW_ONE + 6, column= 5)
button84.grid(row= BUTTONS_ROW_ONE + 7, column= 5)
button94.grid(row= BUTTONS_ROW_ONE + 8, column= 5)
button114.grid(row= BUTTONS_ROW_ONE + 10, column= 5)
button124.grid(row= BUTTONS_ROW_ONE + 11, column= 5)

column4 = {
    button24,
    button33,
    button44,
    button54,
    button64,
    button74,
    button84,
    button94,
    button114,
    button124
}



# top components

lower_bound = 0  
lower_bound_text = tk.Message(text= "Lower bound: " + str(lower_bound))
lower_bound_text.grid(row= BUTTONS_ROW_ONE - 1, column= 2)

upper_bound = 0
upper_bound_text = tk.Message(text= "Upper bound: " + str(upper_bound))
upper_bound_text.grid(row= BUTTONS_ROW_ONE - 1, column= 4)

value = 0
nominal_text = tk.Message(text= "Nominal value: " + str(value))
nominal_text.grid(row= BUTTONS_ROW_ONE - 1, column= 3)

tolerance = 0
tolerance_text = tk.Message(text= "Tolerance: " + str(tolerance), width= 100)
tolerance_text.grid(row= BUTTONS_ROW_ONE - 1, column= 5)

enter_button = tk.Button(text= "CALCULATE", width= BUTTON_WIDTH, bg= "teal", fg= "white")
enter_button.grid(row= BUTTONS_ROW_ONE - 2, column= 5)














