print("Welcome to mumbai")
sum=0 #Starting everything will be zero 
dict = {'saag':200,'Panir':250,'Lassi':50,'Noodles':100,'Dal makhani':150}
#The fetch the all keys from dictionary 
lst=list(dict.keys())  # We written list because we want keys in list form 
print(lst)
while True:
    print("saag (200 rs.)")
    print("Paneer (200 rs.)")
    print("Lassi (200 rs.)")
    print("Noodles (200 rs.)")
    print("Dal makhani (200 rs.)")
    print("press E for exist")
    order=input("Enter your order")
    #Then fetch the order by comparing with lst 
    if order in lst:
       sum=sum+dict[order]
    elif order=='E':
       break 
    else:
       print("Enter right item")
       
print("Your total bill is=",sum)
