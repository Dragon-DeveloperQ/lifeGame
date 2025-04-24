class Field:

    #field = []

    def __init__(self, sizeX, sizeY):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.CellPos = []


    def setCells(self, CellPos):
        self.CellPos = CellPos
        
        '''
        for i in range(self.sizeY):
            self.field.append([])
            for j in range(self.sizeX):
                self.field[i].append(0)
        
        for i in CellPos:
            self.field[i[0]][i[1]] = 1
        '''
        

    def clearField(self):
        self.CellPos = []


    def returnCells(self):
        return self.CellPos

    def step(self):
        CellPosNext = []
        for y in range(self.sizeY):
            for x in range(self.sizeX):
                count = 0
                
                duration = [
                    (-1, -1), (0, -1), (1, -1),
                    (-1, 0),           (1, 0),
                    (-1, 1),  (0, 1),  (1, 1)
                ]
                
                for dx, dy in duration:
                    nx, ny = dx+x, dy+y
                    if 0 <= nx < self.sizeX and 0 <= ny < self.sizeY:
                        if [nx, ny] in self.CellPos:
                            count += 1
                    pass

                if (x == 1) and (y == 1):
                    print(count)
                
                if (count > 1) and (count < 4):
                    CellPosNext.append([x, y])
                
        self.CellPos = CellPosNext
        pass


    def printfield(self):
        for y in range(self.sizeY):
            for x in range(self.sizeX):
                #print('{0} в {1}'.format([x, y], self.CellPos))
                if [x, y] in self.CellPos:
                    print(1, end='')
                else:
                    print(0, end='')
            print()
    