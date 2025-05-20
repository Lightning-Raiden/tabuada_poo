class Tabuada:
    __resultado = 0

    def __init__(self, num):
        self.num = num

    def soma(self):

        for i in range(1, 11):
            self.__resultado = self.num + i
            print(f"{self.num} + {i} = {self.__resultado}")

    def sub(self):
        
        for i in range(1, 11):
            self.__resultado = self.num - i
            print(f"{self.num} - {i} = {self.__resultado}")

    def mult(self):
        
        for i in range(1, 11):
            self.__resultado = self.num * i
            print(f"{self.num} * {i} = {self.__resultado}")

    def div(self):

        if self.num <= 0:
            print("Valor inválido!")
        
        else:
            for i in range(1, 11):
                self.__resultado = self.num / i
                print(f"{self.num} / {i} = {self.__resultado}")