# _*_ coding: utf-8 _*_

def one():
    ten = 45678
    six = 0x12fd2
    return ten + six

def two():
    string = 'Learn Python in imooc'
    return string

def three():
    print 100 < 99
    print 0xff == 255

if __name__ == '__main__':
    one = one()
    two = two()
    print one
    print two
    three = three()