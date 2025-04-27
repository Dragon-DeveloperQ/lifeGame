import pygame
import os
import time

import gamerule
import startposition

# Инициализация окна
pygame.init()
width, height = 900, 900
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Игра Жизнь")

# Создание таймера
clock = pygame.time.Clock()

# Создание рабочего поля
fieldSize = [70, 70]
field = gamerule.Field(fieldSize[0], fieldSize[1])

# Стартовая позиция клеток
field.setCells(startposition.randomPos(fieldSize[0], fieldSize[1], 7))
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
    for i in range(0, height, height//fieldSize[1]):
        pygame.draw.line(screen, 'white', (i, 0), (i, height), width=1)
    for i in range(0, width, width//fieldSize[0]):
        pygame.draw.line(screen, 'white', (0, i), (width, i), width=1)

    # Вывод поля в терминал
    #os.system('clear')
    #field.printfield()

    # Получение массива активных клеток
    cells = field.returnCells()
   
    # Закрашивание активных ячеек
    for y in range(fieldSize[1]):
        for x in range(fieldSize[1]):
            if [x, y] in cells:
                pygame.draw.rect(screen, 'white', (x*(width//fieldSize[0]), y*(height//fieldSize[1]), (width//fieldSize[0]), (height//fieldSize[1])))

    start_time = time.time()

    # Обработка времени
    field.step()

    end_time = time.time()
    print(end_time - start_time)

    # Обновление экрана
    pygame.display.flip()  
    clock.tick(10000)  # 60 кадров в секунду