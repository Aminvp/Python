class Drug:
    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price


class Pharmacy:
    def __init__(self, name):
        self.name = name
        self.drugs = []
        self.employees = []

    def add_drug(self, drug):
        self.drugs.append(drug)

    def add_employee(self, first_name, last_name, age):
        self.employees.append(
            {"first_name": first_name, "last_name": last_name, "age": age})

    def total_value(self):
        sum = 0
        for drug in self.drugs:
            s = drug.price * drug.amount
            sum += s
        return sum

    def employees_summary(self):
        employees = 'Employees:\n'
        i = 0
        for e in self.employees:
            i += 1
            emp = f'The employee number {i} is {e["first_name"]} {e["last_name"]} who is {e["age"]} years old.\n'
            employees += emp
        return employees
