import math

class Category():
    def __init__(self, name): #constructor - initialises with a category with name = name and an empty ledger
        self.name = name
        self.ledger = []

    def __str__(self): # creates a printable string of the ledger
        title = f"{self.name:*^30}\n" # with title centered with *
        items = ""
        for item in self.ledger: # and each ledger entry formatted with truncated description and right aligned amount
            desc = item["description"][:23]
            amount = f"{item['amount']:.2f}"[:7]
            items += f"{desc:<23}{amount:>7}\n"
        return f"{title}{items}Total: {self.get_balance():.2f}"

    def deposit(self, amount, description=""): # adds income to the ledger
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""): # subtracts from the ledger if sufficient funds exist
        if self.check_funds(amount):
            amount = amount * - 1
            self.ledger.append({ "amount" : amount, "description": description })
            return True
        else:
            return False

    def get_balance(self): # cals the current bal by summing all amounts in the ledger
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category): # moves money between categories using the withdraw and deposit methods
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to " + category.name)
            category.deposit(amount, "Transfer from " + self.name)
            return True
        else:
            return False

    def check_funds(self, amount): # returns true if the amount specified is available in bal
        return amount <= self.get_balance()

# builds a vertical bar chart showing percentage of total spending (negative ledger entries) for each category.
# truncates to the nearest 10%.
# renders the Y-axis from 100 to 0 with markers (o) for spending bars.
# adds a horizontal axis and vertical category labels
def create_spend_chart(categories):
    chart = "Percentage spent by category\n"
    spendings = {cat.name: 0 for cat in categories}
    total_spent = 0

    # calculate spendings
    for cat in categories:
        for entry in cat.ledger:
            if entry["amount"] < 0:
                spendings[cat.name] += -entry["amount"]
                total_spent += -entry["amount"]

    # convert to percentages
    percentages = {
        name: int((amount / total_spent) * 10) * 10
        for name, amount in spendings.items()
    }

    # chart bars
    for i in range(100, -1, -10):
        chart += f"{i:>3}|"
        for name in percentages:
            chart += " o " if percentages[name] >= i else "   "
        chart += " \n"

    # separator
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # category labels
    max_len = max(len(name) for name in spendings)
    for i in range(max_len):
        chart += "    "
        for name in spendings:
            chart += f" {name[i] if i < len(name) else ' '} "
        chart += " \n"

    return chart.rstrip("\n")