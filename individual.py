#Ввод данных
V1=int(input("Введите скорость первого автомобиля:"))
V2=int(input("Введите скорость второго автомобиля:"))
s1=int(input("Введите какое расстояние будет между ними:"))
t=0.5
#Решение
S=(s1+V1/t-V2/t)
#Вывод данных при соблюдении условия
if V1<V2:
        print("Ошибка условия")
else:
        print("Расстояние:",S)