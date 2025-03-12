def BMI(weight, high):
    return round(weight / (high**2), 2)

JH = BMI(48, 1.55)
HJ = BMI(76, 1.80)


print(f"형준BMI: {HJ}, 지현BMI: {JH}")
if JH < HJ:
    print("형준이가 돼지")
else:
    print("지현이가 돼지")