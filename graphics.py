
import tkinter as tk

screen = tk.Tk(screenName= "Resistor Color Code Calculator")

BUTTON_WIDTH = 15
BUTTONS_ROW_ONE = 2





# column (digit) 1

button21 = tk.Button(text= "1", bg= "brown", fg= "white", width= BUTTON_WIDTH, relief= "sunken")
button31 = tk.Button(text= "2", bg= "red", fg= "white", width= BUTTON_WIDTH)
button41 = tk.Button(text= "3", bg= "orange", fg= "white", width= BUTTON_WIDTH)
button51 = tk.Button(text= "4", bg= "yellow", fg= "black", width= BUTTON_WIDTH)
button61 = tk.Button(text= "5", bg= "green", fg= "white", width= BUTTON_WIDTH)
button71 = tk.Button(text= "6", bg= "blue", fg= "white", width= BUTTON_WIDTH)
button81 = tk.Button(text= "7", bg= "violet", fg= "white", width= BUTTON_WIDTH)
button91 = tk.Button(text= "8", bg= "gray", fg= "white", width= BUTTON_WIDTH)
button101 = tk.Button(text= "9", bg= "white", fg= "black", width= BUTTON_WIDTH)

button21.grid(row= BUTTONS_ROW_ONE + 1, column= 2)
button31.grid(row= BUTTONS_ROW_ONE + 2, column= 2)
button41.grid(row= BUTTONS_ROW_ONE + 3, column= 2)
button51.grid(row= BUTTONS_ROW_ONE + 4, column= 2)
button61.grid(row= BUTTONS_ROW_ONE + 5, column= 2)
button71.grid(row= BUTTONS_ROW_ONE + 6, column= 2)
button81.grid(row= BUTTONS_ROW_ONE + 7, column= 2)
button91.grid(row= BUTTONS_ROW_ONE + 8, column= 2)
button101.grid(row= BUTTONS_ROW_ONE + 9, column= 2)

# deafult sunken is 1 (10k)
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

button12 = tk.Button(text= "0", bg= "black", fg= "white", width= BUTTON_WIDTH, relief= "sunken")
button22 = tk.Button(text= "1", bg= "brown", fg= "white", width= BUTTON_WIDTH)
button32 = tk.Button(text= "2", bg= "red", fg= "white", width= BUTTON_WIDTH)
button42 = tk.Button(text= "3", bg= "orange", fg= "white", width= BUTTON_WIDTH)
button52 = tk.Button(text= "4", bg= "yellow", fg= "black", width= BUTTON_WIDTH)
button62 = tk.Button(text= "5", bg= "green", fg= "white", width= BUTTON_WIDTH)
button72 = tk.Button(text= "6", bg= "blue", fg= "white", width= BUTTON_WIDTH)
button82 = tk.Button(text= "7", bg= "violet", fg= "white", width= BUTTON_WIDTH)
button92 = tk.Button(text= "8", bg= "gray", fg= "white", width= BUTTON_WIDTH)
button102 = tk.Button(text= "9", bg= "white", fg= "black", width= BUTTON_WIDTH)

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

# deafult sunken is 0 (10k)
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

button13 = tk.Button(text= "10^0", bg= "black", fg= "white", width= BUTTON_WIDTH)
button23 = tk.Button(text= "10^1", bg= "brown", fg= "white", width= BUTTON_WIDTH)
button33 = tk.Button(text= "10^2", bg= "red", fg= "white", width= BUTTON_WIDTH)
button43 = tk.Button(text= "10^3", bg= "orange", fg= "white", width= BUTTON_WIDTH, relief= "sunken")
button53 = tk.Button(text= "10^4", bg= "yellow", fg= "black", width= BUTTON_WIDTH)
button63 = tk.Button(text= "10^5", bg= "green", fg= "white", width= BUTTON_WIDTH)
button73 = tk.Button(text= "10^6", bg= "blue", fg= "white", width= BUTTON_WIDTH)
button83 = tk.Button(text= "10^7", bg= "violet", fg= "white", width= BUTTON_WIDTH)
button93 = tk.Button(text= "10^8", bg= "gray", fg= "white", width= BUTTON_WIDTH)
button103 = tk.Button(text= "10^9", bg= "white", fg= "black", width= BUTTON_WIDTH)
button113 = tk.Button(text= "10^-1", bg= "gold", fg= "black", width= BUTTON_WIDTH)
button123 = tk.Button(text= "10^-2", bg= "silver", fg= "black", width= BUTTON_WIDTH)
button133 = tk.Button(text= "10^-3", bg= "pink", fg= "black", width= BUTTON_WIDTH)


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

# deafult sunken is 3 (10k)
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

button24 = tk.Button(text= "±1%", bg= "brown", fg= "white", width= BUTTON_WIDTH)
button34 = tk.Button(text= "±2%", bg= "red", fg= "white", width= BUTTON_WIDTH)
button44 = tk.Button(text= "±0.05%", bg= "orange", fg= "white", width= BUTTON_WIDTH)
button54 = tk.Button(text= "±0.02%", bg= "yellow", fg= "black", width= BUTTON_WIDTH)
button64 = tk.Button(text= "±0.5%", bg= "green", fg= "white", width= BUTTON_WIDTH)
button74 = tk.Button(text= "±0.25%", bg= "blue", fg= "white", width= BUTTON_WIDTH)
button84 = tk.Button(text= "±0.1%", bg= "violet", fg= "white", width= BUTTON_WIDTH)
button94 = tk.Button(text= "±0.01%", bg= "gray", fg= "white", width= BUTTON_WIDTH)
button114 = tk.Button(text= "±5%", bg= "gold", fg= "black", width= BUTTON_WIDTH, relief= "sunken")
button124 = tk.Button(text= "±10%", bg= "silver", fg= "black", width= BUTTON_WIDTH)


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

# deafult sunken is 11 (5%)
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

enter_button = tk.Button(text= "=", width= BUTTON_WIDTH, activebackground= "blue", activeforeground= "white")
enter_button.grid(row= 0, column= 4)








screen.mainloop()