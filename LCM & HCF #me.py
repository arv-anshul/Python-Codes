# MADE BY ARV # LCM & HCF
print("\n-=>This projet is used for calculating HCF and LCM of two numbers.<=-\n")
num1 = int(input("1st number= "))  # taking-2
num2 = int(input("2nd number= "))  # taking-3

if num1 > num2:
    lcm = num1  # error
else:
    lcm = num2  # -=>20

while True:
    if lcm % num1 == 0 and lcm % num2 == 0:
        break
    else:
        lcm = lcm+1

hcf = (num1*num2)//lcm

print("\nLCM("+str(num1)+","+str(num2)+") =", lcm, "\n")
print("HCF("+str(num1)+","+str(num2)+") =", hcf, "\n")
