def ekzamen(*list, term=4):
    counter = 0
    for i in list:
        if i > term:
            counter =  counter +1
    return counter
z = ekzamen (2,3,4,5,6,7,8,9,7,6,5)
print (f'колічество сдавшіх экзамен равно {z}')






















