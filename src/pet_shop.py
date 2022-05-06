def get_pet_shop_name(list):
    return list["name"]


def get_total_cash(list):
    return list["admin"]["total_cash"]


def add_or_remove_cash(list, num):
    list["admin"]["total_cash"] += num
    return


def get_pets_sold(list):
    return list["admin"]["pets_sold"]


def increase_pets_sold(list, num):
    list["admin"]["pets_sold"] += num
    return


def get_stock_count(list):
    return len(list["pets"])


def get_pets_by_breed(list, breed):
    pets_of_breed = []
    for pet in list["pets"]:
        if pet["breed"] == breed:
            pets_of_breed.append(pet)
    return pets_of_breed


def find_pet_by_name(list, name):
    for pet in list["pets"]:
        if pet["name"] == name:
            return pet


def remove_pet_by_name(list, name):
    for index, pet in enumerate(list["pets"]):
        if pet["name"] == name:
            del list["pets"][index]
    return


def add_pet_to_stock(list, new_pet):
    list["pets"].append(new_pet)
    return


def get_customer_cash(input):
    return input["cash"]


def remove_customer_cash(input, num):
    input["cash"] -= num
    return


def get_customer_pet_count(index):
    return len(index["pets"])


def add_pet_to_customer(index, dict):
    index["pets"].append(dict)
    return


def customer_can_afford_pet(index, pet):
    afford_pet = False
    if index["cash"] >= pet["price"]:
        afford_pet = True
    return afford_pet


def sell_pet_to_customer(dict, pet, customer):
    if pet is not None and customer_can_afford_pet(customer, pet) == True:
        add_pet_to_customer(customer, pet)
        increase_pets_sold(dict, 1)
        remove_customer_cash(customer, pet["price"])
        add_or_remove_cash(dict, pet["price"])
    return
