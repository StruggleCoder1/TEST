import random

from main import print_hi


def printInfo(info):
    # 复制列表
    newInfo = info[:];
    newInfo.insert(0, "hello")
    newInfo.remove("hello")
    for line in newInfo:
        print(line)
    print(sorted(info, reverse=True))
    print(sorted(info))


def testArray(array):
    n = len(array)
    a, b = 3, 1
    # 把b的值给a，把a+b的值给b
    a, b = b, a + b
    print("a的值为：",a,"b的值为：",b)
    for i in array:
        print(i)
    while n > 0:
        n -= 1
        print(f"数组当前值为{n}")


def testDict(dict):
    for key, value in dict.items():
        print("当前的key", key)
        print("当前的value", value)
    print(dict.get("10", "nothing"))


if __name__ == '__main__':
    info = [];
    array = ('Google', 'Runoob', 'Taobao')
    dict = {}
    # printInfo('helloWorld!!!')
    for line in range(10):
        info.append(random.randint(0, 10))
        dict[str(line)] = line
    printInfo(info[-5:])

    #    测试元组
    testArray(array)

    #    测试字典
    testDict(dict)
    for i in range(1, 769, 20):
        print(i)
