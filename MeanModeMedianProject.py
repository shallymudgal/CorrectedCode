import csv
from collections import Counter

with open("SOCR-HeightWeight.csv",newline='') as f:
    reader = csv.reader(f)
    list_data = list(reader)

list_data.pop(0)

whole_data = []
for i in range(len(list_data)):
    full_list = list_data[i][2]
    whole_data.append(float(full_list))     #(correction:you wrote  list_data.append)
    
#Calculating the mean
length = len(whole_data)
total = 0
for x in whole_data :
    total += x

mean = total/length

print("Mean of weight is -> " + str(mean))

#Calculating the median
whole_data.sort()
if length % 2 == 0:
    median1 = float(whole_data[length//2])
    median2 = float(whole_data[length//2 - 1])
    median = (median1 + median2)/2
else :
    median = whole_data[length//2]

print("Median is -> "+ str(median))

#Calculating the mode
data = Counter(whole_data)
mode_range_of_data = {
    "75-85" : 0,              #Correction(range will come like this because this is for weight not height)
    "85-95" : 0,
    "95-105" : 0
}
for weight, occurence in data.items():       #correction
    if 75 < float(weight) < 85:
        mode_range_of_data["75-85"] += occurence
    elif 85< float(weight) < 95:
        mode_range_of_data["85-95"] += occurence
    elif 95 < float(weight) < 105:
        mode_range_of_data["95-105"] += occurence

mode_range, mode_occurence = 0, 0
for range, occurence in mode_range_of_data.items():      #correction
    if occurence > mode_occurence:
        mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence
mode = float((mode_range[0] + mode_range[1]) / 2)
print(f"Mode is -> {mode:2f}")