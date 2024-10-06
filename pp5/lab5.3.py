bank_account=46_567.
deposit = bank_account
factor= 1.075

#po pierwszym roku
deposit*=factor
# po drugim
deposit*=factor
#po trzecim
deposit*=factor
print("Zysk z inwestycji wynosi", round(deposit-bank_account,2))


