class CoinCollector:
    def __init__(self):
        self.penny = 0
        self.nickel = 0
        self.dime = 0
        self.quarter = 0
        self.half_dollar = 0
        self.whole_dollar = 0
        self.rejected_change = []

    def parse_change(self, change):
        split_change = list(change)
        for char in split_change:
            if char == 'P':
                self.penny += 1
            elif char == 'N':
                self.nickel += 1
            elif char == 'D':
                self.dime += 1
            elif char == 'Q':
                self.quarter += 1
            elif char == 'H':
                self.half_dollar += 1
            elif char == 'W':
                self.whole_dollar += 1
            else:
                self.rejected_change.append(char)
        
        return(self.calculate_amount())

    def calculate_amount(self):
        amount = self.penny * .01
        amount += self.nickel * .05
        amount += self.dime * .1
        amount += self.quarter * .25
        amount += self.half_dollar * .5
        amount += self.whole_dollar

        print(f'${amount:,.2f} in coins deposited into account')
        return amount
