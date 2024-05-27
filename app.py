from enum import Enum
import json


class Actions(Enum):
    ADD = 1
    DEL = 2
    UPD = 3
    PRINT = 4
    EXIT = 5

class car():
    def __init__(self,color,type,model) -> None:
        self.color = color
        self.type = type
        self.model = model

    def __str__(self) -> str:
        return f"Color: {self.color}, Type: {self.type}, Model: {self.model}"

def load_data():
    try:
        with open('car_data.json', 'r') as file:
            data = json.load(file)
            return [car(c['color'], c['type'], c['model']) for c in data]
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []



def save_data(cars):
    cars_dict = [car_to_dict(c) for c in cars]
    with open('car_data.json', 'w') as file:
        json.dump(cars_dict, file, indent=4)

cars = load_data()

def display_menu():
    for action in Actions:
        print(f'{action.name} - {action.value}')
    return int(input("Input selection: "))

def add_car():
    temp_car = car(input("Color: "),input("Type: "),input("Model: ") )
    cars.append(temp_car)

def print_cars():
    for index, car in enumerate(cars):
        print(f'{index} - {car}')

def del_car():
    print_cars()
    temp_del = int(input("Please enter the index of the selected car: "))
    cars.pop(temp_del)

def update_car():
    print_cars()
    temp_upd = int(input("Please enter the index of the selected car: "))
    cars[temp_upd] = car(input("Color: "),input("Type: "),input("Model: ") )

def car_to_dict(car_obj):
    return {
        'color': car_obj.color,
        'type': car_obj.type,
        'model': car_obj.model
    }



if __name__ == '__main__':
    while True:
        user_input =display_menu()
        if user_input == Actions.EXIT.value:
            save_data(cars)
            exit()
        if user_input == Actions.ADD.value: add_car()
        if user_input == Actions.PRINT.value: print_cars()
        if user_input == Actions.DEL.value: del_car()
        if user_input == Actions.UPD.value: update_car()


    