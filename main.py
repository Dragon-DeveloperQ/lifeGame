import pygame
import os
import time

import gamerule
import startposition

# Инициализация окна
pygame.init()
width, height = 800, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Игра Жизнь")

# Создание таймера
clock = pygame.time.Clock()

# Создание рабочего поля
fieldCount = [70, 70]
field = gamerule.Field(fieldCount[0], fieldCount[1])

# Стартовая позиция клеток
field.setCells(startposition.randomPos(fieldCount[0], fieldCount[1], 4))
#field.setCells(startposition.startPos)
'''
field.setCells([[2, 1], 
                [2, 2],
                [2, 3]])
'''
                
# Инициализация цикла игры
running = True
while running:

    # Обработка события выхода
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Отчистка экрана
    screen.fill((0, 0, 0))  

    # Разметка поля
    fieldSize = [width//fieldCount[0], height//fieldCount[1]]
    for i in range(0, fieldCount[0]+1):
        pygame.draw.line(screen, 'white', (i*fieldSize[0], 0), (i*fieldSize[0], fieldCount[0] * fieldSize[0]), width=1)
    for i in range(0, fieldCount[1]+1):
        pygame.draw.line(screen, 'white', (0, i*fieldSize[1]), (fieldCount[0] * fieldSize[0], i*fieldSize[1]), width=1)

    pygame.draw.rect(screen, 'green', (width, height, fieldSize[0], fieldSize[1]))
    # Вывод поля в терминал
    #os.system('clear')
    #field.printfield()

    # Получение массива активных клеток
    cells = field.returnCells()
   
    # Закрашивание активных ячеек
    for y in range(fieldCount[1]):
        for x in range(fieldCount[1]):
            if [x, y] in cells:
                pygame.draw.rect(screen, 'white', (x*(width//fieldCount[0]), y*(height//fieldCount[1]), (width//fieldCount[0]), (height//fieldCount[1])))

    start_time = time.time()

    # Обработка времени
    field.step()

    end_time = time.time()
    print(end_time - start_time)

    # Обновление экрана
    pygame.display.flip()  
    clock.tick(10000)  # 60 кадров в секунду