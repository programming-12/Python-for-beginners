def cal_compound_In(p,n,r):
    print("start Balance\t","\tInterest\t","\tEnding balance\t")
    total=0
    x=r/100
    tot=0
    for i in range(1,n+1):
        z_new=p*(1+x)**i-p
        z_old=p*(1+x)**(i-1)-p
        tot=tot +(z_new - z_old)
        if (i==1):
            print("{0:.2f}\t".format(p),end="")
            print("\t{0:.2f}\t".format(z_new-z_old),end="")
            print("\t\t{0:.2f}\t".format(z_new+p),end="")
        else:
            print("{0:.2f}\t".format(p+z_old),end="")
            print("\t{0:.2f}\t".format(z_new-z_old),end="")
            print("\t\t{0:.2f}\t".format(z_new+p),end="")
    print("total interest deposite: Rs:{0:.2f}".format(tot))
p=int(input("enter your principle value"))
r=int(input("enter your rate of interest"))
n=int(input("enter your number of year"))
cal_compound_In(p,n,r)
