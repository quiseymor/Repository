numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
val_numb=[x for x in numbers if x is not None]
sum_numb=sum(val_numb)
count_numb=len(numbers)

if count_numb >0:
     result = sum_numb/count_numb
else:
    result=0

numbers=[result if x is None else x for x in numbers]
print("Измененный список:", numbers)
