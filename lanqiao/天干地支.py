tiangan = ['geng', 'xin', 'ren', 'gui', 'jia', 'yi', 'bing', 'ding', 'wu', 'ji']
dizhi = ['zi', 'chou', 'yin', 'mao', 'chen', 'si', 'wu', 'wei', 'shen', 'you', 'xu', 'hai']

n = int(input())

d = n - 2020
print(tiangan[d%10] + dizhi[d%12])
