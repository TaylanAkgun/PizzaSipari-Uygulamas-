# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 21:39:58 2023

@author: Damla Kıran and Taylan Akgün
"""
#Gerekli kütüphaneler içe aktarıldı.

import csv
from datetime import datetime

#Pizza üst sınıfı oluşturulması

class Pizza:
    def __init__(self, description, cost):
        self.description = description
        self.cost = cost

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost

#Pizza alt sınıfları oluşturulması ve fiyatlarının belirlenmesi

class KlasikPizza(Pizza):
    def __init__(self):
        description = "Klasik Pizza"
        cost = 19.99
        super().__init__(description, cost)

class MargaritaPizza(Pizza):
    def __init__(self):
        description = "Margarita Pizza"
        cost = 24.99
        super().__init__(description, cost)

class TurkPizza(Pizza):
    def __init__(self):
        description = "Turk Pizza"
        cost = 29.99
        super().__init__(description, cost)
        
class SadePizza(Pizza):
    def __init__(self):
        description = "Sade Pizza"
        cost = 14.99
        super().__init__(description, cost)

#Decorator üst sınıfı oluşturulması ve fiyatlarının belirlenmesi

class Decorator(Pizza):
    def __init__(self, pizza):
        self.pizza = pizza

    def get_description(self):
        return self.pizza.get_description()

    def get_cost(self):
        return self.pizza.get_cost()

class Zeytin(Decorator):
    def __init__(self, pizza):
        description = "Zeytin"
        cost = 3.0
        super().__init__(pizza)
        self.description = f"{self.pizza.get_description()}, {description}"
        self.cost = self.pizza.get_cost() + cost

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost + self.pizza.get_cost()

class Mantar(Decorator):
    def __init__(self, pizza):
        description = "Mantar"
        cost = 5.0
        super().__init__(pizza)
        self.description = f"{self.pizza.get_description()}, {description}"
        self.cost = self.pizza.get_cost() + cost
        
        def get_description(self):
            return self.description

        def get_cost(self):
            return self.cost + self.pizza.get_cost()
        
class KeciPeyniri(Decorator):
    def __init__(self, pizza):
        description = "Keci Peyniri"
        cost = 6.0
        super().__init__(pizza)
        self.description = f"{self.pizza.get_description()}, {description}"
        self.cost = self.pizza.get_cost() + cost
        
        def get_description(self):
            return self.description

        def get_cost(self):
            return self.cost + self.pizza.get_cost()
        
class Et(Decorator):
    def __init__(self, pizza):
        description = "Et"
        cost = 10.0
        super().__init__(pizza)
        self.description = f"{self.pizza.get_description()}, {description}"
        self.cost = self.pizza.get_cost() + cost
        
        def get_description(self):
            return self.description

        def get_cost(self):
            return self.cost + self.pizza.get_cost()

class Sogan(Decorator):
    def __init__(self, pizza):
        description = "Sogan"
        cost = 4.0
        super().__init__(pizza)
        self.description = f"{self.pizza.get_description()}, {description}"
        self.cost = self.pizza.get_cost() + cost
        
        def get_description(self):
            return self.description

        def get_cost(self):
            return self.cost + self.pizza.get_cost()
        
class Misir(Decorator):
    def __init__(self, pizza):
        description = "Misir"
        cost = 3.5
        super().__init__(pizza)
        self.description = f"{self.pizza.get_description()}, {description}"
        self.cost = self.pizza.get_cost() + cost
        
        def get_description(self):
            return self.description

        def get_cost(self):
            return self.cost + self.pizza.get_cost()

# Menu.txt dosyasının içe aktarılması ve yazdırılması

def print_menu():
    with open("Menu.txt", "r") as menu_file:
        menu_text = menu_file.read()
    print(menu_text)

#Pizza tabanı seçimi

def get_pizza_choice():
    while True:
        print("Lutfen bir pizza tabani seciniz:\n1. Klasik Pizza\n2. Margarita Pizza\n3. Turk Pizza\n4. Sade Pizza")
        choice = input("Sectiginiz pizza tabani numarasını girin: ")
        if choice == "1":
            return KlasikPizza()
        elif choice == "2":
            return MargaritaPizza()
        elif choice == "3":
            return TurkPizza()
        elif choice == "4":
            return SadePizza()
        else:
            print("Gecersiz secim yaptınız. Tekrar deneyin.")

#Pizza malzemeleri seçimi

def get_topping_choice(pizza):
    selected_toppings = []
    while True:
        print("Lutfen eklemek istediginiz malzemeleri seciniz:\n1. Zeytin\n2. Mantar\n3. Keci Peyniri\n4. Et\n5. Sogan\n6. Misir\n7. Tamam")
        choice = input("Sectiginiz malzemenin numarasını girin: ")
        if choice == "1":
            selected_toppings.append("Zeytin")
        elif choice == "2":
            selected_toppings.append("Mantar")
        elif choice == "3":
            selected_toppings.append("Keci Peyniri")
        elif choice == "4":
            selected_toppings.append("Et")
        elif choice == "5":
            selected_toppings.append("Sogan")
        elif choice == "6":
            selected_toppings.append("Misir")
        elif choice == "7":
            break
        else:
            print("Gecersiz secim yaptınız. Tekrar deneyin.")
    
    # return the pizza object with selected toppings added
    for topping in selected_toppings:
        pizza = get_topping_choice(pizza)
    return pizza
        
#Toplam tutarın hesaplanması

def calculate_total_price(pizza):
    total_price = pizza.get_cost()
    print(f"Toplam tutar: {total_price:.2f}")
    return total_price

#Kullanıcı bilgilerinin alınması

def get_user_info():
    name = input("Lutfen adınız ve soyadınızı yazın: ")
    id_number = input("Lutfen TC kimlik numaranızı girin: ")
    return name, id_number

#Kredi kartı bilgilerinin alınması

expiration_date = None
cvv = None

def get_credit_card_info():
    while True:
        credit_card_number = input("Kredi kartı numarasını girin: ")
        if credit_card_number.isdigit() and len(credit_card_number) == 16:
            break
        print("Geçersiz kart numarası. Lütfen 16 haneli bir sayı girin.")
            
    expiration_date = input("Kredi kartı son kullanma tarihini (AA/YY) girin: ")
    cvv = input("Kredi kartı CVV'sini girin: ")
    
    return credit_card_number, expiration_date, cvv


#Alınan kullanıcı bilgilerinin Order_Database.csv dosyasına kaydedilmesi

def write_to_database(name, id_number, credit_card_number, pizza_description, total_price, expiration_date, cvv):
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    with open("Orders_Database.csv", "a", newline="") as orders_file:
        writer = csv.writer(orders_file)
        writer.writerow([name, id_number, credit_card_number, pizza_description, total_price, current_time, expiration_date, cvv])


#Main function oluşturulması

def main():
    print_menu()
    pizza = get_pizza_choice()
    pizza = get_topping_choice(pizza)
    total_price = calculate_total_price(pizza)
    name, id_number = get_user_info()
    credit_card_number, expiration_date, cvv = get_credit_card_info()
    write_to_database(name, id_number, credit_card_number, pizza.get_description(), total_price, expiration_date, cvv )
    print("Tesekkürler, siparisiniz alinmistir!")

if __name__ == "__main__":
    main()
