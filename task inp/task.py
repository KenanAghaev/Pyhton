class Class:
    def __init__(self):
        self.array = [1, 2, 3, 4, 5, 6]

    def indexler(self, eded):
        cemler = [(self.array[i] + self.array[j], (i, j))
                     for i in range(len(self.array))
                     for j in range(i + 1, len(self.array))]
        
        indexler = [(i, j) for cem, (i, j) in cemler if cem == eded]

        if indexler:
            print("İndeksler:", indexler)
        else:
            print("-1")

Class = Class()
eded = int(input("ededi daxil edin: "))
Class.indexler(eded)
