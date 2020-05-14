import random

from modules.death_var import *
from modules.person import Jason_V
from modules.Dzheyson_vurkhiz import person


D_knife = input("Введите оружие Джейсона: ")
D_mask = input("Введите маску Джейсона: ")
Jason = Jason_V(D_mask, D_knife)
Jason.go_hunt()

def quant():
    try:
        kol = int(input("Введите количество персонажей\nЭто должно быть целое число!\nВвод: "))
    except Exception:
        print("Вас просили ввести число!\nПопробуйте ещё раз!")
        quant()
    return kol

def pers(kol):
    persons = []
    for i in range(kol):
        name_p = input("Введите имя нового персонажа: ")
        persons.append(person(name_p))
    return persons

kolvo = quant()
persons = pers(kolvo)

for i in range(len(persons)):
    fun_num = 1
    #fun_num = random.randint(1, 6)
    if fun_num == 1:
        trapped(persons[i])
    elif fun_num == 2:
        polet_v_okno(persons[i])
    elif fun_num == 3:
        burned_v_alive(persons[i])
    elif fun_num == 4:
        drowned(persons[i])
    elif fun_num == 5:
        head_cut_off(persons[i])
    elif fun_num == 6:
        run_away(persons[i])