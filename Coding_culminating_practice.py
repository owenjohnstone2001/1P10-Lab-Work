class Guest:

    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.stamina = 0
        self.hunger = 0
        self.money_spent = 0.0

    def get_name(self):
        return self.name

    def get_money(self):
        return self.money

    def get_stamina(self):
        return self.stamina

    def get_hunger(self):
        return self.hunger

    def get_money_spent(self):
        return self.money_spent

    def set_name(self, name):
        self.name = name

    def set_money(self, money):
        self.money = money

    def set_stamina(self, stamina):
        self.stamina = stamina

    def set_hunger(self, hunger):
        self.hunger = hunger

    def set_money_spent(self):
        percent_spent = (self.get_stamina() + (2 * self.get_hunger())) / 30
        total_money_spent = self.get_money() * percent_spent
        self.money_spent = total_money_spent
        return self.money_spent

def park_expenses(num_employees, wage, num_rides):
    expenses = num_employees * wage * 8 + num_rides * 10000
    return expenses

def revenue_and_profit(expenses, gross_margin_percent):
    daily_required_revenue = expenses / (1 - gross_margin_percent)
    gross_profit = daily_required_revenue - expenses
    return [daily_required_revenue, gross_profit]

def create_guests(guest_attributes):
    new_guest = Guest(guest_attributes[0], guest_attributes[1])
    new_guest.set_stamina(guest_attributes[2])
    new_guest.set_hunger(guest_attributes[3])
    new_guest.set_money_spent()
    return new_guest
    
def main():
    start_up = 1000000
    num_rides = 15
    num_employees = 250
    wage = 25
    gross_margin_percent = 0.20
    parkexpenses = park_expenses(num_employees, wage, num_rides)
    print("Park expenses: " + str(round(parkexpenses, 2)))

    revenueandprofit = revenue_and_profit(parkexpenses, gross_margin_percent)
    print("Daily required revenue: " + str(round(revenueandprofit[0], 2)))
    print("Daily gross profit margin: " + str(round(revenueandprofit[1], 2)))

    day = 1
    profit = 0
    print("Gross Profit\tDay #")
    while profit < start_up:
        profit += revenueandprofit[1]
        print(str(round(profit, 2)) + '\t', str(day))
        day += 1

    active_guest = create_guests(['Active Guest', 500, 10, 4])
    hungry_guest = create_guests(["Hungry Guest", 500, 4, 7])
    active_guest.set_money_spent()
    hungry_guest.set_money_spent()

    if active_guest.get_money_spent() > hungry_guest.get_money_spent():
        print(str(active_guest.get_name()) + " will spend more money than " + str(hungry_guest.get_name()) + ". They will spend $" + str(active_guest.get_money_spent) + ".")
    elif active_guest.get_money_spent() < hungry_guest.get_money_spent():
        print(str(hungry_guest.get_name()) + " will spend more money than " + str(active_guest.get_name()) + ". They will spend $" + str(hungry_guest.get_money_spent) + ".")
    else:
        print(str(active_guest.get_name()) + " and " + str(hungry_guest.get_name()) + " will both spend $" + str(active_guest.get_money_spent()))

    guest_file = open('/Users/owenjohnstone/Desktop/Wk-9 Lab (Winter) - Practice (Part C)/guest_list.txt', 'r')
    guest_attributes = guest_file.readlines()
    guest_file.close()

    for line in guest_attributes:
        split_str = line.split()
        guest = [str(split_str[0]), int(split_str[1]), int(split_str[2]), int(split_str[3])]
        new_guest = create_guests(guest)
        new_guest.set_money_spent()
        print(str(new_guest.get_name()) + " will spend $" + str(round(new_guest.get_money_spent(), 2)) + " at the park.")

main()