import math
import pandas
import pandas as pd
import random
import openpyxl
label = None

maslo=random.randint(10,60)
toplbak=random.randint(500,2500)
S=int(input("Введите расстояние, например 665 узла - "))
n=int(input("Укажите число оборотов вала от 420 до 800 - ")) # число оборотов в минуту
W=3.14*n/30 # угловая скорость вала
g=0.15 # удельный расход топлива на ед мощности, кг
rashodvchas=1.5 # расход топлива в час
dvig=14000 # мощность двигателяп в л. с.

if maslo>=20:
    maslo=" "+ str(maslo)
else:
    maslo="Требуется дозапрвка "+ str(maslo)

if toplbak>=900:
    toplbak=" "+ str(toplbak)
else:
    toplbak="требуется дозапрвка "+ str(toplbak)
G=1/14000*110*g*W

v=int(input("Укажите скорость танкера,км/ч - "))
coltech=int(input("Укажите количество течений - "))
list=[]
for i in range (coltech, 0, -1):
    tech = int(input("Укажите скорость течения,км/ч  - "))
    R=v+tech # общая скорость танкера и течения
    list.append(R)

print("общая скорость корабля и течения в км/ч - ", round(sum(list)/len(list),1))
print("Расход топлива на ед работы в кг/час - ",G)

xl = pd.DataFrame({"Sensor_name": ["Кол-во топлива", "Кол-во масла"],
                            "xl and time":[toplbak, maslo]
                            })
xl.to_excel('./sas.xlsx')
