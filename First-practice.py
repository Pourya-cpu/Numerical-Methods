readings = [12.5 , 98.2, -3.0, 45.7, 102.4 , 67.1, 0.0, 83.6]
print()
print(f"Original data is: {readings}")


sum_org = 0
count_org = 0

for k in readings:
    sum_org += k
    count_org += 1


mean_org = sum_org/count_org

print(f"Mean of original data is: {mean_org}")
print()


valid_data = []
invalid_data = []

for i in readings:
    if 0 <= i <= 100:
        valid_data.append(i)
    else:
        invalid_data.append(i)

print(f"Valid data is: {valid_data}")



sum_val = 0 
count_val = 0

for j in valid_data:
    sum_val +=  j
    count_val += 1

mean_val = sum_val/count_val

print(f"Mean of valid data is: {mean_val}")
print()
print(f"Invalid data is: {invalid_data}")
print()

print(f"{invalid_data} rejected.")
print()