#Run program in Command Prompt 
#Prompts user to input Budget, Family Size, Fuel Preference and annual salary
#Returns closest match to the intital three parameters 
#Returns annual salary divided by 12 and multiplied by .2 as "Budget should not exceed 20% of your monthly income, which is..."

def get_user_input():
    fuel_preference = input("What is your preferred fuel type? (gas/electric): ").lower()
    family_size = int(input("What is your family size? (1-7): "))
    budget = int(input("What is your budget for a car? (no dollar signs or commas): "))
    annual_salary = int(input("What is your annual salary? (no dollar signs or commas): "))
    annual_salary_percentage = budget / (annual_salary / 12) / 0.2
    return fuel_preference, family_size, budget, annual_salary, annual_salary_percentage

def find_cars(cars, budget, family_size, fuel_preference):
    matching_cars = []
    for category, car_list in cars.items():
        if category == fuel_preference:
            for car in car_list:
                if car[2] >= family_size and car[1] <= budget:
                    matching_cars.append(car)
    if not matching_cars:
        return "No cars found within your budget and family size. Consider increasing your budget or decreasing your family size."
    else:
        closest_car = min(matching_cars, key=lambda x: abs(x[1] - budget))
        return f"The closest car to your budget is the {closest_car[0]} with {closest_car[2]} seats."

def main():
    cars = {
        'gas': [
            ['Kia Sorento', 24000, 5],
            ['Honda Pilot', 34000, 5],
            ['Toyota Rav 4', 36000, 5],
            ['Ford Explorer', 39000, 7],
            ['Land Rover Defender', 65000, 5],
            ['BMW x3', 45000, 5],
            ['BMW x5', 52000, 7],
            ['Audi Q3', 42000, 5],
            ['Audi Q5', 51000, 5],
            ['Mercedes GLA', 37000, 5],
            ['Mercedes GLB', 39999, 5],
            ['Jaguar XE', 32000, 4],
            ['Mercedes C class', 29000, 4],
            ['Mercedes E class', 39000, 4],
            ['BMW 3 series', 34000, 4],
            ['Audi A4', 31000, 4],
            ['Porsche Boxter/Cayman', 69000, 2],
            ['BMW 5 Series', 65000, 4],
            ['Mercedes S class', 70000, 4],
            ['BMW 7 Series', 71000, 4]
        ],
        'electric': [
            ['Toyota Prius', 26000, 4],
            ['Hyundai Elantra', 19000, 4],
            ['Tesla Model X', 35000, 4],
            ['Porsche Taycan', 90000, 4]
        ]
    }
    fuel_preference, family_size, budget, annual_salary, annual_salary_percentage = get_user_input()

    matching_cars = find_cars(cars, budget, family_size, fuel_preference)

    if isinstance(matching_cars, str):
        print(matching_cars)
    else:
        print(matching_cars)
        print(f"Your car payment should not exceed {annual_salary_percentage:.2f}% of your monthly income, which is ${annual_salary/12:.2f}.")

if __name__ == "__main__":
    main()