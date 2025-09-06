type_of_flower = input()
number_of_flowers = int(input())
budget = int(input())

prize = 0

if type_of_flower == "Roses":
    prize = 5
    if number_of_flowers > 80 :
        prize = prize - (prize*0.10)
elif type_of_flower == "Dahlias":
    prize = 3.8
    if number_of_flowers > 90 :
        prize = prize*0.85

cost = prize*number_of_flowers
final_cost = abs(budget - cost)

if cost <= budget:
    print(f"Hey, you have a great garden wth {number_of_flowers} {type_of_flower} and {final_cost:.2f} leva left.")
else:
    print(f"Not enough money, you need {final_cost} leva more.")