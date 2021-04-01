#2021年4月1日 软测每日代码1
#python学习代码练习1
'''
有四个数字：1、2、3、4，能组成多少个互
不相同且无重复数字的三位数？各是多少？
'''

for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if( i != k ) and (i != j) and (j != k):
                print (i,j,k)