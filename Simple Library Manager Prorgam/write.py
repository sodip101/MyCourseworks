import read as r
def userdata(sid,username,BN,SN,p,d,m,y):#function to store student data with 1 book borrowed
    file=open(str(sid)+".txt","w")
    file.write(str(sid))
    file.write(",")
    file.write(str(username))
    file.write(",")
    file.write(str(BN))
    file.write(",")
    file.write(str(SN))
    file.write(",")
    file.write(str(p))
    file.write(",")
    file.write(str(d))
    file.write(",")
    file.write(str(m))
    file.write(",")
    file.write(str(y))
    file.write(",")
    file.write("1")
    file.close()
def userdata2(sid,username,BN1,SN1,p1,BN2,SN2,p2,d,m,y):#function to store student data with 1 book borrowed
    file=open(str(sid)+".txt","w")
    file.write(str(sid))
    file.write(",")
    file.write(str(username))
    file.write(",")
    file.write(str(BN1))
    file.write(",")
    file.write(str(SN1))
    file.write(",")
    file.write(str(p1))
    file.write(",")
    file.write(str(BN2))
    file.write(",")
    file.write(str(SN2))
    file.write(",")
    file.write(str(p2))
    file.write(",")
    file.write(str(d))
    file.write(",")
    file.write(str(m))
    file.write(",")
    file.write(str(y))
    file.write(",")
    file.write("2")
    file.close()

def owrite(List,SN):#function to edit 2d list
    List[SN][3]=int(List[SN][3])-1
    return List
def owrite2(List,SN1,SN2):#function to edit 2d list
    List[SN1][3]=int(List[SN1][3])-1
    List[SN2][3]=int(List[SN2][3])-1
    return List
def owrite3(List):#function to overwrite database
    file=open("books.txt","w")
    for i in range(len(List)):
        j=0
        for k in range(len(List[i])):
            file.write(str(List[i][k]))
            if j<4:
                file.write(",")
            j+=1
        file.write("\n")
    file.close()
