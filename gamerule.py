from numba import njit

@njit(cache=True)
def STEP(__CellPos, __sizeX, __sizeY):
        __CellPos = set(__CellPos)
        CellPosNext = set()
        duration = [
                    (-1, -1), (0, -1), (1, -1),
                    (-1, 0),           (1, 0),
                    (-1, 1),  (0, 1),  (1, 1)
                ]
                
        for i in __CellPos:
            for j in duration:
                x, y = i[0] + j[0], i[1] + j[1]
                count = 0
                if (x, y) not in CellPosNext:
                
                    for dx, dy in duration:
                        nx, ny = dx+x, dy+y
                        if 0 <= nx < (__sizeX - 1) and 0 <= ny < (__sizeY - 1):                        
                            if (nx, ny) in __CellPos:
                               count += 1
                        pass
                
                    if (x, y) in __CellPos and (count >= 2) and (count <= 3):
                        CellPosNext.add((x, y))
                    if (x, y) not in __CellPos and (count == 3):
                        CellPosNext.add((x, y))
                
        return CellPosNext
        pass



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

    
    def SetCell(self, x, y):
        if (x, y) not in self.__CellPos:
            self.__CellPos.append((x, y))


    def returnCells(self):
        return self.__CellPos

    def step(self):
        self.__CellPos =  STEP(self.__CellPos, self.__sizeX, self.__sizeY)
