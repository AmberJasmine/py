class A:
    a = []

    def __eq__(self, other):
        if self.a is other.a:
            return True
        # else:
        #     return False


a1 = A()
a2 = A()
print(a1 == a2, a1 is a2)


x=[i for i in range(1,12,3)]
print(type(x),x)

y=(i for i in range(1,12,3))
print(type(y),y)

z={i for i in range(1,12,3)}
print(type(z),z)

# 取出x的偶数，采用列表推导式
x=[i for i in x if i%2==0]
print(x)

# 新增方法，验证字典推导式
def dict_iterable():
    # 使用字典推导式生成字典
    d = {i: i**2 for i in range(1, 6)}
    print(type(d), d)

# 调用dict_iterable方法
dict_iterable()

import datetime
dt = datetime.datetime(2025,2,28)
print(dt)
dt = datetime.datetime(2025,4,10)
print(dt)
print(dt.strftime("%Y-%m-%d %H:%M:%S"))