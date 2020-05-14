def FLSM(defaultsubnet,subnet,b,d):
    while True:
        c=2**d
        if c>=b:
            break
        else:
            d+=1
    if c<255:
        l=defaultsubnet[2]
        print("The default subnetmask of class C is :",defaultsubnet[2])
    elif c<65025:
        l=defaultsubnet[1]
        print("The default subnetmask of class B is :",defaultsubnet[1])
    elif c<16581375:
        l=defaultsubnet[0]
        print("The default subnetmask of class A is :",defaultsubnet[0])
    e=(32-d)*"1"
    #print(e,"e")
    f=d*'0'
    #print(f,"o")
    g=e+f
    #print(g)
    i=str(g[0:8])+str(g[8:16])+str(g[16:24])+str(g[24::])
    #print(i)
    j=subnet[l]
    #print("The default subnetmask of class binary representation is :",j)
    print("The binary representation of new subnetmask is:",g[0:8]+"."+str(g[8:16])+"."+str(g[16:24])+"."+str(g[24::]))
    h=[(str(int(g[0:8],2))),(str(int(g[8:16],2))),(str(int(g[16:24],2))),(str(int(g[24::],2)))]
    print("The New SubNet Mask Generated is:",'.'.join(h))
    print("The Prefix Length of New Subnet Mask is:",i.count('1'))
    z=i.count('1')-j.count('1')
    print("No of networks :",int(2**(z)))
    print("No of hosts :",c)
#Main Program
print("Which type of subnetting method do you want to choose either FLSM or VLSM ?")
defaultsubnet=['255.0.0.0','255.255.0.0','255.255.255.0','255.255.255.255']
subnet={'255.0.0.0':'11111111.0.0.0','255.255.0.0':'11111111.11111111.0.0','255.255.255.0':'11111111.11111111.11111111.0','255.255.255.255':'11111111.11111111.11111111.1111111'}
a=input()
if a=='FLSM':
    print("How Many IP'S are Required?")
    b=int(input())
    d=1
    n=FLSM(defaultsubnet,subnet,b,d)
