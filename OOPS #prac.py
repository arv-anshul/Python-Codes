# class practice
class Computer:
    typeOfComputer = "Laptop"

    @classmethod
    def info(cls): return cls.typeOfComputer

    def __init__(self, nameOfComputer, ram, processor, company):
        self.nameOfComputer = nameOfComputer
        self.ram = ram.upper()
        self.processor = processor.upper()
        self.company = company.upper()
        # this is a cpu class
        self.cpuInfo = self.CpuInfo()

    def compare(self, toCompare):
        p1 = int(self.ram[:-2])
        p2 = int(toCompare.ram[:-2])
        if p1 > p2:
            string = f"{self.nameOfComputer} is better than {toCompare.nameOfComputer}."
            return string
        else:
            string = f"{toCompare.nameOfComputer} is better than {self.nameOfComputer}."
            return string

    def get_name(self): return self.nameOfComputer

    # made a other class in a class
    class CpuInfo():

        def __init__(self):
            self.company = "intel"
            self.model = "i5"
            self.price = "10000"
            self.gpu = "8"

            # this is customized
        # def __init__(self, company, model, price, gpu):
            # self.company = company
            # self.model = model
            # self.price = price
            # self.gpu = gpu

        def show(self): return "I am cpuInfo"

        def performance(self, toCompare):
            gpu_1 = int(self.gpu)
            gpu_2 = int(toCompare.gpu)

            return f"{self.gpu} is better than {toCompare.gpu}" if gpu_1 > gpu_2 else f"{toCompare.gpu} is better than {self.gpu}"


macBook_Air = Computer("MacBook Air", "12gb", "m1", "apple")
dell_Aspiron_1050 = Computer("Dell Aspiron 1050", "8gb", "i5", "dell")

# print(macBook_Air.compare(dellAspiron_1050))
# print(macBook_Air.get_name())
# print(Computer.info())
# print(macBook_Air.cpuInfo.performance(dell_Aspiron_1050))


# ------------------------------------------------
class A():
    def func_1(self):
        print("--> in A func_1")


class B(A):
    # pass
    def func_1(self):
        super().func_1()
        print("--> in B func_1")


obj = B()
obj.func_1()


# ----------- claculations in class -------------------------
class forSum():
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def __add__(self, other):
        let = forSum(0, 0)
        let.num1 = self.num1 + other.num1
        let.num2 = self.num2 + other.num2
        return let

    def display(self): print(self.num1, self.num2)


number1 = forSum(12, 20)
number2 = forSum(30, 23)
result = number1 + number2
# result.display()
