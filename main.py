#Find proton, nuetron, neculon and elctron number
fazool = print( 'Nuetron Calculator 1.0 ')
fazool2 = print("Made by Code With Maaz")
proton_number = input("Enter Proton Number  ")
proton_number = int(proton_number)

electron_number = input("Enter Electron Number " )
electron_number = int(electron_number)

Atomic_Maas = input("Enter Atomic Mass ")
Atomic_Maas = int(Atomic_Maas)

print("---- Wait We are caclculating nuetron number---- ")

if electron_number == proton_number:
    print("Proton number and electron number is same so there would be no valency")
else:
    print("Electron and protron number is not same so there will be valency")
    
nuetron_number =  Atomic_Maas - proton_number
print(nuetron_number)       
