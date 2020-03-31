def computepay(hour,rate):
    h = hour
    r = rate
    pay = h*r
    if h> 40.0:
        reghr=40.0
        overtmhr=h-40.0
        regrt=rate
        overtmrate=regrt*1.5
        return (reghr*regrt)+(overtmhr*overtmrate)
    return (pay)
    
hrs = input("Enter Hours worked:")
rt = input("Enter hourly rate:")
try:
    hour = float(hrs)
except:
    print("Not a number, Please try again")
    quit()
try:
    rate = float(rt)
except:
    print("Not a number, Please try again")
    quit()

p = computepay(hour,rate)
print("Pay",p)

