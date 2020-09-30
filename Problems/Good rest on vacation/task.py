# put your python code here
days = int(input())
food_cost = int(input())
one_flight = int(input())
cost_night_hotel = int(input())

print(food_cost * days + one_flight * 2 + cost_night_hotel * (days -1))