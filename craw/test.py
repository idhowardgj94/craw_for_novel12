class test:
    def __init__(self):
        print("inside init")
        self.fun1()
    def fun1(self):
        print("inside fun1")
if __name__ == '__main__':
    test()
