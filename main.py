import pygame
import gamerule
import os


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


# Инициализация окна
pygame.init()
width, height = 1000, 1000
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Игра Жизнь")

# Создание таймера
clock = pygame.time.Clock()

# Создание рабочего поля
fieldSize = [100, 100]
field = gamerule.Field(fieldSize[0], fieldSize[1])

field.setCells([[2, 1], 
                [3, 2],
                [1, 3], [2, 3], [3, 3]])
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

    # Размета поля
    for i in range(0, height, height//fieldSize[1]):
        pygame.draw.line(screen, 'white', (i, 0), (i, height), width=1)
    for i in range(0, width, width//fieldSize[0]):
        pygame.draw.line(screen, 'white', (0, i), (width, i), width=1)

    # Вывод поля в терминал
    clear_terminal()
    # field.printfield()
    cells = field.returnCells()
    print('------------------------------------')
   
    # Закрашивание активных ячеек
    for y in range(fieldSize[1]):
        for x in range(fieldSize[1]):
            if [x, y] in cells:
                pygame.draw.rect(screen, 'white', (x*(height//fieldSize[0]), y*(height//fieldSize[1]), (height//fieldSize[0]), (height//fieldSize[1])))

    # Обработка времени
    field.step()

    # Обновление экрана
    pygame.display.flip()  
    clock.tick(5)  # 60 кадров в секунду