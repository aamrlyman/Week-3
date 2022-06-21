class Wallet: 

    def __init__(self, color_passed_in, does_fold):
        
        self.color = color_passed_in
        self.cash = 0
        self.does_fold = does_fold

    def put_cash_in_wallet(self, amount_of_cash):
        self.cash += amount_of_cash
    
    def take_cash_out(self, amount_of_cash):
        self.cash -= amount_of_cash


