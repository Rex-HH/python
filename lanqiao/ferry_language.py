n = int(input())

language = set()

flag = 'NO'

for _ in range(n):

    input_ = input()
    
    if input_ in language:
        
        if flag == 'NO':
            flag = input_

    else:
        language.add(input_)


print(flag)
