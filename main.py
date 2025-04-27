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
fieldCount = [100, 100]
field = gamerule.Field(fieldCount[0], fieldCount[1])

# Стартовая позиция клеток
field.setCells(startposition.randomPos(fieldCount[0], fieldCount[1], 2))
#field.setCells(startposition.startPos)
                
# Инициализация цикла игры
running = True
all_time = []
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
    for x, y in cells:
        pygame.draw.rect(screen, 'white', (x*fieldSize[0], y*fieldSize[1], fieldSize[0], fieldSize[1]))

    start_time = time.time()

    # Обработка времени
    field.step()

    end_time = time.time()
    print(end_time - start_time)

    '''
    all_time.append(end_time - start_time)
    if len(all_time) > 20:
        sum_time = 0
        for i in all_time:
            sum_time += i
        print('Среднее время - {0}'.format(sum_time / len(all_time)))
        running = False
    '''

    # Обновление экрана
    pygame.display.flip()  
    clock.tick(60)  # кадров в секунду