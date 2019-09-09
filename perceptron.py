class Perceptron :
    def AND(self,x1,x2) :
        w1 = 0.5; w2 = 0.5; theta = 0.7
        tmp = x1 * w1 + x2 * w2
        if tmp <= theta :
            return 0
        elif tmp > theta :
            return 1
    
    def OR(self,x1,x2) :
        w1 = 0.5; w2 = 0.5; theta = 0.2
        tmp = x1 * w1 + x2 * w2
        if tmp <= theta :
            return 0
        elif tmp > theta :
            return 1
    def NAND(self,x1,x2) :
        w1 = 0.5; w2 = 0.5; theta = 0.7
        tmp = x1 * w1 + x2 * w2
        if tmp <= theta :
            return 1
        elif tmp > theta :
            return 0
    def NOT(self,x) :
        if x :
            return 0
        else :
            return 1

def Debug() :
    A = Perceptron()
    print(A.AND(0,0))
    print(A.AND(1,0))
    print(A.AND(0,1))
    print(A.AND(1,1))
    print("---------------------------------------")
    print(A.OR(0,0))
    print(A.OR(1,0))
    print(A.OR(0,1))
    print(A.OR(1,1))
    print("---------------------------------------")
    print(A.NAND(0,0))
    print(A.NAND(1,0))
    print(A.NAND(0,1))
    print(A.NAND(1,1))
    print("---------------------------------------")
    print(A.NOT(0))
    print(A.NOT(1))


Debug()
