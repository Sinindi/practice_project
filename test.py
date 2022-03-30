res = 0
for i in range(2,10,3):
    for fruit in ['사과', '딸기', '바나나']:
        if fruit =='딸기':
            continue
        res += i
        print(f'i ={i}, res = {res}')
        