class Student():
    def __init__(self,std):
        self.standard = std
    def print_std(self):
        for x in range(self.standard):
            print(x)

if __name__ == '__main__':
    Student(5).print_std()