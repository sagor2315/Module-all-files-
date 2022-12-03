# if and else condition problem solution
#
# normal_bodytem = 98.2
# temp = int(input("Enter Your Body Temp: "))
# if temp > normal_bodytem:
#     print("Taka Paracitamal 2 Bela")
# else:
#     print("Taka Vitamin 3 bela")

# name = input("Enter Your Name: ")
# gender = input("Enter Your Gender: ")
# country = input("Enter Country Name: ")
#
# if gender == "M":
#     profession = "actor"
#     pronoun = "He"
#     known_as = "Hero"
# else:
#     gender = "F"
#     profession = "actress"
#     pronoun = "She"
#     known_as = "Heroin"
# print(f"{name} is an {profession} of {country}. {pronoun} is well known {known_as} still now.")

name = input("Enter the Name: ")
gender = input("Enter The Gender: ")
country = input("Enter The Country Name: ")

if gender == "m":
    profession = "Cricket Player"
    pro = "He"
    role = "Player"
else:
    gender = "f"
    profession = "Cricket Player"
    pro = "She"
    role = "Female Player"
print(f"{name} is a {profession}. He is well known {role} in {country}. ")


