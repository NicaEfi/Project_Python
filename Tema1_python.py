#Ex1
list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
print("Lista mea:",list)
#Ex2
sorted_list_asc = sorted(list)
print("Lista sortata in sens crescator:",sorted_list_asc)

#Ex3
sorted_list_desc = sorted( list, reverse=True)
print("Lista sortata in sens descrescator:",sorted_list_desc)

#Ex4
indices_list_par = list[::2]
print("Numerele cu indicii pari:",indices_list_par)

#Ex5
indices_list_impar = list[1::2]
print("Numerele cu indicii impari:",indices_list_impar)

#Ex6
multiples_3 = [num for num in list if num % 3 == 0]
print("Multiplii ai lui 3:",multiples_3)