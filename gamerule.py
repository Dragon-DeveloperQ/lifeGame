class Field:

    #field = []

    def __init__(self, sizeX, sizeY):
        self.__sizeX = sizeX
        self.__sizeY = sizeY
        self.__CellPos = []


    def setCells(self, CellPos):
        self.__CellPos = CellPos
        
        '''
        for i in range(self.__sizeY):
            self.field.append([])
            for j in range(self.__sizeX):
                self.field[i].append(0)
        
        for i in __CellPos:
            self.field[i[0]][i[1]] = 1
        '''
        

    def clearField(self):
        self.__CellPos = []


    def returnCells(self):
        return self.__CellPos


    def step(self):
        CellPosNext = []
        
        duration = [
                    (-1, -1), (0, -1), (1, -1),
                    (-1, 0),           (1, 0),
                    (-1, 1),  (0, 1),  (1, 1)
                ]
                
        for i in self.__CellPos:
            for j in duration:
                x, y = i[0] + j[0], i[1] + j[1]
                count = 0
                if [x, y] not in CellPosNext:
                
                    for dx, dy in duration:
                        nx, ny = dx+x, dy+y
                        if 0 <= nx < self.__sizeX and 0 <= ny < self.__sizeY:                        
                            if [nx, ny] in self.__CellPos:
                               count += 1
                        pass
                
                    if [x, y] in self.__CellPos and (count >= 2) and (count <= 3):
                        CellPosNext.append([x, y])
                    if [x, y] not in self.__CellPos and (count == 3):
                        CellPosNext.append([x, y])
                
        self.__CellPos = CellPosNext
        pass


    def printfield(self):
        for y in range(self.__sizeY):
            for x in range(self.__sizeX):
                if [x, y] in self.__CellPos:
                    print(1, end='')
                else:
                    print(0, end='')
            print()
    