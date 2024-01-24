class Solution:
    # number of rows
    m = 0
    # number of columns
    n = 0
    # direction
    # 0 east right
    # 1 south down
    # 2 west left
    # 3 north up
    # by default set to east
    direction = 0
    
    # row index
    i = 0
    # column index
    j = -1
    
    # get number of steps to be moved forward based on direction
    def getSteps(self):
        # if direction is east or west return number of columns
        if self.direction == 0 or self.direction == 2:
            return self.n
        # if direction is north or south return number of rows
        elif self.direction == 1 or self.direction == 3:
            return self.m
    
    def modifyBoundry(self):
         # if direction is east or west return number of columns
        if self.direction == 0 or self.direction == 2:
            self.n = self.n -1
        # if direction is north or south return number of rows
        elif self.direction == 1 or self.direction == 3:
            self.m = self.m -1
            
    def changeDirection(self):
        self.direction = self.direction + 1
        if self.direction >= 4 :
            self.direction = self.direction % 4
    
    def changeAccessIndex(self):
        if self.direction == 0:
            self.j = self.j + 1
        elif self.direction == 1:
            self.i = self.i + 1
        elif self.direction == 2:
            self.j = self.j -1
        elif self.direction == 3:
            self.i = self.i -1

            
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
       
        spiral_order = []
       
        self.m = len(matrix)
        if self.m:
            self.n = len(matrix[0])
 
        while (self.m > 0 and self.n > 0):
        # steps to move forward
            steps = self.getSteps()
            # print(f"steps {steps}")
            # print(f"pre position ({self.i},{self.j})")
            while (steps > 0):
                self.changeAccessIndex()
                # print(f"({self.i},{self.j})")
                spiral_order.append(matrix[self.i][self.j])
                steps = steps -1
                
                

            self.changeDirection()
            # print(f"change direction {self.direction}")
            self.modifyBoundry()
            # print(f"modify boundary rows->{self.m} columns->{self.n}")
            # print(f"post position ({self.i},{self.j})")
            # self.changeAccessIndex()
            # print(f"change index row index->{self.i} column index->{self.j}")
        
        return spiral_order
        
