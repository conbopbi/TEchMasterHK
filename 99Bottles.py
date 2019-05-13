for i in reversed(range(1,100)):
    i-=1
    print('{}{}'.format(i,' bottles of beer on the wall'))
    print('{}{}'.format(i,' bottles of beer'))
    if i==1:
        break
