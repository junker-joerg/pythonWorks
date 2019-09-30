# -*- coding=utf-8 -*-
#1 immer "git push" machen am Ende 
def testfnktMK():
    print("Hallo Welt")
    
def main():
    a = 1
    testfnktMK()
    a= "hallo nochmal"
    f1(a)
for i in range(10):
    print(i)
else:
    print("Ende")

def f1(a: str):
    print(a)

class MK_CLASS(object):
    """docstring for MK_CLASS."""
    def __init__(self, arg):
        super(MK_CLASS, self).__init__()
        self.arg = arg
        

if __name__ == '__main__':
    a = 12
    main()
    