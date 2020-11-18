from Car import Car1

value = float(input("Fluids: "))
unit = input("-- L for liters -- G  for galeons -- :  ")

myCar = Car1()
myCar.setTank(value, unit)
while True:
    choice = int(input("-- 0 liters to galeons -- 1 change tank size -- 2 exit --"))
    if choice == 2:
        break
    elif choice == 0:
        unit = input("-- L for liters -- G  for galeons -- :  ")
        print(myCar.getTank(unit))
    elif choice == 1:
        value = float(input("Fluids: "))
        unit = input("-- L for liters -- G  for galeons -- :  ")
        myCar.getTank(unit)
    else:
        pass