
import color_code_calcs
import tkinter as tk

screen = tk.Tk(screenName= "Resistor Color Code Calculator")


# column (digit) 1

button21 = tk.Button(text= "1", bg= "brown", fg= "white", width= 10, relief= "raised")
button31 = tk.Button(text= "2", bg= "red", fg= "white", width= 10, relief= "raised")
button41 = tk.Button(text= "3", bg= "orange", fg= "white", width= 10, relief= "raised")
button51 = tk.Button(text= "4", bg= "yellow", fg= "black", width= 10, relief= "raised")
button61 = tk.Button(text= "5", bg= "green", fg= "white", width= 10, relief= "raised")
button71 = tk.Button(text= "6", bg= "blue", fg= "white", width= 10, relief= "raised")
button81 = tk.Button(text= "7", bg= "violet", fg= "white", width= 10, relief= "raised")
button91 = tk.Button(text= "8", bg= "gray", fg= "white", width= 10, relief= "raised")
button101 = tk.Button(text= "9", bg= "white", fg= "black", width= 10, relief= "raised")

button21.grid(row= 2, column= 2)
button31.grid(row= 3, column= 2)
button41.grid(row= 4, column= 2)
button51.grid(row= 5, column= 2)
button61.grid(row= 6, column= 2)
button71.grid(row= 7, column= 2)
button81.grid(row= 8, column= 2)
button91.grid(row= 9, column= 2)
button101.grid(row= 10, column= 2)


# column (digit) 2

button12 = tk.Button(text= "0", bg= "black", fg= "white", width= 10, relief= "raised")
button22 = tk.Button(text= "1", bg= "brown", fg= "white", width= 10, relief= "raised")
button32 = tk.Button(text= "2", bg= "red", fg= "white", width= 10, relief= "raised")
button42 = tk.Button(text= "3", bg= "orange", fg= "white", width= 10, relief= "raised")
button52 = tk.Button(text= "4", bg= "yellow", fg= "black", width= 10, relief= "raised")
button62 = tk.Button(text= "5", bg= "green", fg= "white", width= 10, relief= "raised")
button72 = tk.Button(text= "6", bg= "blue", fg= "white", width= 10, relief= "raised")
button82 = tk.Button(text= "7", bg= "violet", fg= "white", width= 10, relief= "raised")
button92 = tk.Button(text= "8", bg= "gray", fg= "white", width= 10, relief= "raised")
button102 = tk.Button(text= "9", bg= "white", fg= "black", width= 10, relief= "raised")

button12.grid(row= 1, column= 3)
button22.grid(row= 2, column= 3)
button32.grid(row= 3, column= 3)
button42.grid(row= 4, column= 3)
button52.grid(row= 5, column= 3)
button62.grid(row= 6, column= 3)
button72.grid(row= 7, column= 3)
button82.grid(row= 8, column= 3)
button92.grid(row= 9, column= 3)
button102.grid(row= 10, column= 3)


# column 3 (multiplier)

button13 = tk.Button(text= "10^0", bg= "black", fg= "white", width= 10, relief= "raised")
button23 = tk.Button(text= "10^1", bg= "brown", fg= "white", width= 10, relief= "raised")
button33 = tk.Button(text= "10^2", bg= "red", fg= "white", width= 10, relief= "raised")
button43 = tk.Button(text= "10^3", bg= "orange", fg= "white", width= 10, relief= "raised")
button53 = tk.Button(text= "10^4", bg= "yellow", fg= "black", width= 10, relief= "raised")
button63 = tk.Button(text= "10^5", bg= "green", fg= "white", width= 10, relief= "raised")
button73 = tk.Button(text= "10^6", bg= "blue", fg= "white", width= 10, relief= "raised")
button83 = tk.Button(text= "10^7", bg= "violet", fg= "white", width= 10, relief= "raised")
button93 = tk.Button(text= "10^8", bg= "gray", fg= "white", width= 10, relief= "raised")
button103 = tk.Button(text= "10^9", bg= "white", fg= "black", width= 10, relief= "raised")
button113 = tk.Button(text= "10^-1", bg= "gold", fg= "black", width= 10, relief= "raised")
button123 = tk.Button(text= "10^-2", bg= "silver", fg= "black", width= 10, relief= "raised")
button133 = tk.Button(text= "10^-3", bg= "pink", fg= "black", width= 10, relief= "raised")


button13.grid(row= 1, column= 4)
button23.grid(row= 2, column= 4)
button33.grid(row= 3, column= 4)
button43.grid(row= 4, column= 4)
button53.grid(row= 5, column= 4)
button63.grid(row= 6, column= 4)
button73.grid(row= 7, column= 4)
button83.grid(row= 8, column= 4)
button93.grid(row= 9, column= 4)
button103.grid(row= 10, column= 4)
button113.grid(row= 11, column= 4)
button123.grid(row= 12, column= 4)
button133.grid(row= 13, column= 4)


# column 4 (tolerance)

button24 = tk.Button(text= "±1%", bg= "brown", fg= "white", width= 10, relief= "raised")
button34 = tk.Button(text= "±2%", bg= "red", fg= "white", width= 10, relief= "raised")
button44 = tk.Button(text= "±0.05%", bg= "orange", fg= "white", width= 10, relief= "raised")
button54 = tk.Button(text= "±0.02%", bg= "yellow", fg= "black", width= 10, relief= "raised")
button64 = tk.Button(text= "±0.5%", bg= "green", fg= "white", width= 10, relief= "raised")
button74 = tk.Button(text= "±0.25%", bg= "blue", fg= "white", width= 10, relief= "raised")
button84 = tk.Button(text= "±0.1%", bg= "violet", fg= "white", width= 10, relief= "raised")
button94 = tk.Button(text= "±0.01%", bg= "gray", fg= "white", width= 10, relief= "raised")
button114 = tk.Button(text= "±5%", bg= "gold", fg= "black", width= 10, relief= "raised")
button124 = tk.Button(text= "±10%", bg= "silver", fg= "black", width= 10, relief= "raised")


button24.grid(row= 2, column= 5)
button34.grid(row= 3, column= 5)
button44.grid(row= 4, column= 5)
button54.grid(row= 5, column= 5)
button64.grid(row= 6, column= 5)
button74.grid(row= 7, column= 5)
button84.grid(row= 8, column= 5)
button94.grid(row= 9, column= 5)
button114.grid(row= 11, column= 5)
button124.grid(row= 12, column= 5)






enter_button = tk.Button(text= "=", width=10, activebackground="blue", activeforeground="white")
enter_button.grid(row= 0, column= 4)







screen.mainloop()