def subtrai_pares(n):
    if n < 10:
        return n 
    if n % 2 == 0:
        return subtrai_pares(n//10) - n%10
    else:
        return subtrai_pares(n//10) # para ignorar o 5 que é impar 
print(subtrai_pares(8564))