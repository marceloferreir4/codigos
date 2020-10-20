import tkinter as tk


window = tk.Tk()

def attack(attack, monster):
    if monster == name1:
        life1 -= attack2[attack][1]
        drw_life1.coord(drw_life1, 0, 0)
    else:
        life2 -= attack1[attack][1]

# Monster 1
name1 = "Bulbasaur"
life1 = 100
attack1 = [["Investida", 10], ["Chicote de Vinha", 15], ["Folha Navalha", 20], ["Raio Solar", 30]]

lbl_name1 = tk.Label(window, text=name1)
can_life1 = tk.Canvas(window, width=100, height=20)
drw_life1 = can_life1.create_rectangle(0, 0, 100, 30, fill="green")
btn_attack11 = tk.Button(window, text=attack1[0][0], command=lambda: attack(0, name2))
btn_attack12 = tk.Button(window, text=attack1[1][0])
btn_attack13 = tk.Button(window, text=attack1[2][0])
btn_attack14 = tk.Button(window, text=attack1[3][0])


# Monster 2
name2 = "Charmander"
life2 = 100
attack2 = [["Investida", 10], ["Brasas", 15], ["Lança-chamas", 30], ["Explosão de Fogo", 20]]

lbl_name2 = tk.Label(window, text=name2)
can_life2 = tk.Canvas(window, width=100, height=20)
drw_life2 = can_life2.create_rectangle(0, 0, 100, 30, fill="green")
btn_attack21 = tk.Button(window, text=attack2[0][0])
btn_attack22 = tk.Button(window, text=attack2[1][0])
btn_attack23 = tk.Button(window, text=attack2[2][0])
btn_attack24 = tk.Button(window, text=attack2[3][0])


# Grid
lbl_name1.grid(row=0)
can_life1.grid(row=1)
btn_attack11.grid(row=2, sticky="we")
btn_attack12.grid(row=3, sticky="we")
btn_attack13.grid(row=4, sticky="we")
btn_attack14.grid(row=5, sticky="we")

lbl_name2.grid(row=0, column=1)
can_life2.grid(row=1, column=1)
btn_attack21.grid(row=2, column=1, sticky="we")
btn_attack22.grid(row=3, column=1, sticky="we")
btn_attack23.grid(row=4, column=1, sticky="we")
btn_attack24.grid(row=5, column=1, sticky="we")


window.mainloop()
