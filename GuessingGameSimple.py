from random import randrange
mn =randrange(1, 101)
flag = 0
win = False
while flag < 7:
    hn = float(input('Nhap mot so:'))
    flag += 1
    if hn == mn:
        print('Ban da doan dung!')
        win = True
        break
    elif hn < mn:
        print('Hay doan cao hon mot chut nua...')
    else:
        print('Hay doan thap hon mot chut nua...')
if win == False:
    print('Game Over')