from person import Person
from wallet import Wallet 

a_wallet = Wallet('black', True)

person_one = Person('david', 'brown', Wallet('black', True) )

print(person_one.name)
print(person_one.wallet.cash)

person_one.wallet.put_cash_in_wallet(100)

print(person_one.wallet.cash)



# from wallet import Wallet 


# jims_wallet = Wallet('Brown', False)
# carols_wallet = Wallet('Red', True)

# print(jims_wallet.color)
# print(jims_wallet.cash)
# print(carols_wallet.color)


# jims_wallet.put_cash_in_wallet(100)
# print(jims_wallet.cash)

