import random
ware=[1,2,3,4,5,6,7,8,9]
num_rule=int(''.join(map(str, random.sample(ware, 4)[:])))
count=0
while count<10:
    a=0
    b=0
    num_player=input('请输入猜测的互不相同的四位数字')
    if len(str(num_player)) != 4 or num_player.isdigit()==False:
        print('您的输入有误，请重新输入!')
        continue
    if len(str(num_player)) !=len(set(str(num_player))):
        print('您的输入有重复数字，请重新输入!')
        continue
    for i in range(0,4,1):
        if num_player[i] == str(0):
            print('您的输入含有0，请重新输入!')
            continue
        if num_player[i]==str(num_rule)[i]:
            a+=1
        for j in range(0,4,1):
            if num_player[i]==str(num_rule)[j]:
                b+=1
    b-=a
    if a!=4:
        print(f'本次的结果为{a}A{b}B')
    else:
        print('完全正确!')
        break
    count+= 1
if count == 10:
    print('猜测次数用尽，你输了！')
print(f'正确结果是{num_rule}')
