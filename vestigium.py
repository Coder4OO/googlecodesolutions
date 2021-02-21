import sys

class SquareMatrix():
    def __init__(self, rows):
        self.matrix = self.create_matrix(rows)


    def create_matrix(self, rows):
        matrix = []
        for i in range(rows):
            matrix.append([])
            for j in range(rows):
                matrix[i].append(0)
        return matrix

    def print_matrix(self):
        for i in range(len(self.matrix)):
            rowstring = ""
            for j in range(len(self.matrix[i])):
                rowstring += str(self.matrix[i][j])+" "
            print(rowstring)

    def edit_matrix(self, ins):
        for i in range(len(ins)):
            line = ins[i]
            line = line.split(' ')
            for j in range(len(line)):
                line[j] = int(line[j])
            self.matrix[i] = line

    def calculate_trace(self):
        addlist = []
        for i in range(len(self.matrix)):
            addlist.append(self.matrix[i][i])
        return sum(addlist)

    def get_row_repeats(self):
        repeatcount = 0
        for i in range(len(self.matrix)):
            if len(set(self.matrix[i])) != len(self.matrix[i]):
                repeatcount += 1
        return repeatcount

    def get_coloumn_repeats(self):
        repeatcount = 0
        for i in range(len(self.matrix)):
            testlist = []
            for j in range(len(self.matrix)):
                testlist.append(self.matrix[j][i])
            if len(set(testlist)) != len(testlist):
                repeatcount += 1
        return repeatcount


def take_input(ins):
    for i in range(len(ins)):
        ins[i] = ins[i].rstrip('\n')
    t = int(ins[0])
    del ins[0]
    for i in range(t):
        n = int(ins[0])
        del ins[0]
        d = []
        for j in range(n):
            d.append(ins[0])
            del ins[0]
        matrix = SquareMatrix(n)
        matrix.edit_matrix(d)
        k = matrix.calculate_trace()
        r = matrix.get_row_repeats()
        c = matrix.get_coloumn_repeats()
        print("Case #"+str(i+1)+": " +str(k)+" "+str(r)+" "+str(c))

ins = sys.stdin.readlines()
take_input(ins)
                
