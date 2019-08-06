import random


def binary_search(data,target,low_index,high_index):# retorna True o False si encuentra o no el valor
    if low_index>high_index:  # termina la busqueda
        return False

    mid=(high_index + low_index)//2 # se aproxima a el entero menor proximo

    if target == data [mid]:# verificamos si el valor buscado esta en la mitad
        return True
    elif target < data[mid]:
        return binary_search(data,target,low_index,mid-1) #asumiendo que el numero esta en la mitad menor
    else:
        return binary_search(data,target,mid+1,high_index) # asumiendo que el numero esta en la mitad mayor


if __name__ == '__main__':
    data = [random.randint(0,100) for i in range(10)] # crear un vector de 10 elemntos con random 100
    data.sort()# ordenar los datos antes de aplicar la funcione de busqueda
    print(data)
    target = int(input('what number do you want?'))
    found = binary_search(data,target,0,len(data)-1)
    print(found)
