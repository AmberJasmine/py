'''com'''

name = 'Ark'
age = 18
placle1 = '西安'
placle2 = '咸阳'

def welcome(somebody):
    '''方法'''
    print(f'欢迎{somebody}，来到{placle2}')

def headNote(string):
    '''测试方法备注信息'''
    print('\n',str(string).rjust(30,'*'))


def swap(a, b):
    '''swap'''
    return b, a