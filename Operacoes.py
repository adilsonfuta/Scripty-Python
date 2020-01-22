
n1=int(input('infome o valor 1 : \n ==> '))

n2=int(input('infome o valor 2 : \n ==> '))

R=n1+n2
print(' A soma de {} + {} = {}'.format(n1,n2,R))

try:
    
    R=n1/n2
    print(' A diviisao de {} / {} = {}'.format(n1,n2,R))
    
except ZeroDivisionError as A:
        print('erros '+A)


R=n1*n2
print(' A Multiplicacao de {} * {} = {}'.format(n1,n2,R))



R=n1-n2
print(' A Subtracao de {} - {} = {}'.format(n1,n2,R))

