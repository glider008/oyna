import random
random_number = random.randint(1,10)
print("Менің ойымдағы санды табыңыз. Ол сан 1-10 арасында")
flag1 = True
flag = True
while flag:
    a = int(input())
    if a == random_number:
        #print("Мәссаған! Мықты екенсіз!\nТағыда ойнаймыз ба?! ")
        while flag1:
            print("Мәссаған! Мықты екенсіз!\nТағыда ойнаймыз ба?!\n1 Ойнау\n0 Шығу ")
            b = int(input())
            if b == 1:
                print("Қайта оралуыңызбен\nМенің ойымдағы санды табыңыз. Ол сан 1-10 арасында")
                break
                flag = True
            elif b == 0:
                flag1 = False
                flag = False
                print("Сау Болыңыз! ")
    elif a < random_number:
            print("Менің саным бұдан үлкенірек! ")
    elif a > random_number:
            print("Менің саным бұдан кішігірек!")