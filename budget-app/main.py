# Build a Budget App

class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.total = 0

    def deposit(self, amount, description=""):
        self.ledger.append({
            'amount': amount,
            'description': description
        })
        self.total += amount

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({
                'amount': -amount,
                'description': description
            })
            self.total -= amount
            return True
        else:
            return False

    def get_balance(self):
        return self.total

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False

    def check_funds(self, amount):
        return amount <= self.total

    def __str__(self):
        star = "*"
        space = " "
        n = (30-len(self.name)) // 2
        title = f"{star*n}{self.name}{star*n}\n"
        ledger_entry = ""
        for entry in self.ledger:
            description = entry['description']
            amount = entry['amount']
            if(len(description) > 23):
                description = description[:23]
            description_padded = description.ljust(23)
            amount_formatted = f"{amount:.2f}".rjust(7)
            ledger_entry += f"{description_padded}{amount_formatted}\n"
        total = f"Total: {self.get_balance()}"
        category = title + ledger_entry + total
        return category

def create_spend_chart(categories):
    # Calculate total spent in specific category
    # Calculate total spent in all categories
    cat_spent = {}
    total_spent = 0
    for category in categories: 
        cat_spent[category.name] = 0
        for entry in category.ledger:
                if entry['amount'] < 0:
                    cat_spent[category.name] += abs(entry['amount'])
        total_spent += cat_spent[category.name]
    # Calculate percentage
    for key, spent in cat_spent.items():
        percentage = (spent / total_spent) * 100
        cat_spent[key] = int(percentage // 10) * 10
    # Draw chart
    cat_count = len(cat_spent)
    bar1 = "o".rjust(2)
    bar2 = "o".rjust(3)
    space1 = "".rjust(2)
    space2 = "".rjust(3)
    final_bar_space = "".rjust(2)
    line = "-"*(cat_count * 3)

    bar_chart_string = ""
    title = "Percentage spent by category"
    bar_chart_string += title
    for y in range(100, -10, -10):
        bar_chart_string += "\n"
        bar_chart_string += str(y).rjust(3) + "|"
        for index, key in enumerate(cat_spent):
            if y <= cat_spent[key]:
                if index < 1:
                    bar_chart_string += bar1
                else:
                    bar_chart_string += bar2
            else:
                if index < 1:
                    bar_chart_string += space1
                else:
                    bar_chart_string += space2
        bar_chart_string += final_bar_space
    bar_chart_string += "\n"
    bar_chart_string += "-".rjust(5)
    bar_chart_string += line
    # Print category names vertically below the bars
    title_line = ""
    space = ""
    final_category_space = "".rjust(2)
    category_titles = [category for category in cat_spent]
    max_len = max([len(category) for category in category_titles])
    for i in range(0, max_len):
        title_line += "\n"
        title_line += space.rjust(3)
        for title in category_titles:
            try:
                title_line += title[i].rjust(3)
            except IndexError:
                title_line += space.rjust(3)
        title_line += final_category_space
    bar_chart_string += title_line
    return bar_chart_string

food = Category("Food")
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')

clothing = Category('Clothing')
auto = Category("Auto")

food.transfer(50, clothing)
food.transfer(50, auto)
clothing.withdraw(40, 'Shirt')
auto.withdraw(30)

print(food)
print(clothing)
print(auto)

print(create_spend_chart([food, clothing, auto]))
