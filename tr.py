import os
print("Welcome to the  online auction ")
dict={}
h_bid=[]
while True:
    name=input("Enter the name : ")
    bid=int(input(" What is ur bid :"))
    dict[name]=bid
    ex=input(" Is any one to bid, if yes enter 'YES' else 'NO':").upper()
    if ex=='NO':
        break
    else:
        os.system('cls')
h_bid=0
for name in dict:
    bids=dict[name]
    if bids>h_bid:
        h_bid=bids
for name in dict:
    if h_bid==dict[name]:
        print(f'The winner of auction if {name} with amount {h_bid}')
