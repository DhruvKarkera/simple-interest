def simpleInterest(p,t,r):
    print("The principal is", p)
    print("The time is",t)
    print("The rate of interest is", r)
    
    si = (p*t*r)/100
    
    print("The simple interest is",si)
    return si

print("ENTER THE VALUES :-")
principal = int(input("Enter the principle:"))
time = int(input("Enter the time :"))
rate = int(input("Enter the rate:"))

simpleInterest(principal,time,rate)