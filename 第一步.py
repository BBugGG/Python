import random
print('------猜数字游戏------')
b=int(input('输入数字范围，0到:'))
realnumber=random.randint(0,b)
print('----数字已经生成----')
i=0
while True:
    i=i+1
    tmp = int(input('输入你猜的数字:'))
    if tmp<realnumber:
        print('小了！重新输入你的数字:')
        continue
    elif tmp>realnumber:
        print('大了！重新输入你的数字:')
        continue
    elif tmp==realnumber:
        break
print('恭喜你对了！！用了{0}步噢'.format(i))
