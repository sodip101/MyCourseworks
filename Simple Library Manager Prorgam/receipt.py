import read as r
import dime as dt
import read as rd
def borrow(name,sid,book_b,day,month,year):
    list2=r.readbooks()
    print("\t\t\tRECEIPT")
    print("\t\t\t-------")
    print("\t\tStudent Name: ",name)
    print("\t\tStudent ID: ",sid)
    print("\t\tBook Borrowed: ", list2[book_b][1])
    print("\t\tAuthor: ",list2[book_b][2])
    print("\t\tPrice: ","Rs.",list2[book_b][4])
    print("\t\tDate Borrowed: ",day,"/",month,"/",year)
    rdd=int(day)+10
    if rdd>30:
        rdd=rdd-30
        rdm=int(month)+1
        if rdm>12:
            month=1
            rdy=int(year)+1
    print("\t\tReturn Date: ",rdd,"/",month,"/",year)
def borrow2(name,sid,book_b,book_b2,day,month,year):
    list2=r.readbooks()
    print("\t\t\tRECEIPT")
    print("\t\t\t-------")
    print("\t\tName: ",name)
    print("\t\tStudent ID: ",sid)
    print("\t\tBook Borrowed: ", list2[book_b][1])
    print("\t\tAuthor: ",list2[book_b][2])
    print("\t\tPrice: ","Rs.",list2[book_b][4])
    print("\t\tBook Borrowed: ", list2[book_b2][1])
    print("\t\tAuthor: ",list2[book_b2][2])
    print("\t\tPrice: ","Rs.",list2[book_b2][4])
    print("\t\tTotal Price: ","Rs.",list2[book_b][4],"+","Rs.",list2[book_b2][4],"=",int(list2[book_b][4])+int(list2[book_b2][4]))
    print("\t\tDate Borrowed: ",day,"/",month,"/",year)
    rdd=int(day)+10
    if rdd>30:
        rdd=rdd-30
        rdm=int(month)+1
        if rdm>12:
            month=1
            rdy=int(year)+1
    print("\t\tReturn Date: ",rdd,"/",month,"/",year)    
def returns1(List):
    rd=int(List[5])+10
    rm=int(List[6])
    ry=int(List[7])
    dd=0
    if rd>30:
        rd=1
        rm+=1
        if rm>12:
            rm=1
            ry+=1    
    print("\t\t\tRECEIPT")
    print("\t\t\t-------")
    print("\t\tStudent Name: ",List[1])
    print("\t\tStudent ID: ",List[0])
    print("\t\tBook Returned: ", List[2])
    print("\t\tLast Date to Return Borrowed Book: ",rd,"/",rm,"/",ry)
    print("\t\tDate Returned: ",dt.day(),"/",dt.month(),"/",dt.year())
    if rd<=30 and rd<dt.day() and rm==dt.month() and ry==dt.year():
        dd=(dt.day()-rd)
        print("\t\tLate Fine: ","Rs.",dd*5)
    elif rd<=30 and rd>dt.day()and rd>(dt.day()+10) and rm<dt.month() and ry==dt.year():
        dd=10-(rd-(dt.day()+10))
        print("\t\tLate Fine: ","Rs.",dd*5)
    elif rd<=30 and rd<dt.day() and rm<dt.month() and ry==dt.year():
        dd=(dt.day()+30)-rd
        print("\t\tLate Fine: ","Rs.",dd*5)
    elif rd<=30 and rd>dt.day()and rd>(dt.day()+10) and rm>dt.month() and ry<dt.year():
        dd=10-(rd-(dt.day()+10))
        print("\t\tLate Fine: ","Rs.",dd*5)
    else:
        print("\t\tLate Fine: None")
def returns2(List):
    rd=int(List[8])+10
    rm=int(List[9])
    ry=int(List[10])
    dd=0
    if rd>30:
        rd=1
        rm+=1
        if rm>12:
            rm=1
            ry+=1    
    print("\t\t\tRECEIPT")
    print("\t\t\t-------")
    print("\t\tStudent Name: ",List[1])
    print("\t\tStudent ID: ",List[0])
    print("\t\tNo. of books borrowed: ",List[-1])
    print("\t\tBooks Returned: ", List[2],",",List[5])
    print("\t\tBooks Borrwed On: ",List[8],"/",List[9],"/",List[10])
    print("\t\tLast Date to Return Borrowed Books: ",rd,"/",rm,"/",ry)
    print("\t\tBooks Returned On: ",dt.day(),"/",dt.month(),"/",dt.year())
    if rd<=30 and rd<dt.day() and rm==dt.month() and ry==dt.year():
        dd=(dt.day()-rd)
        print("\t\tLate Fine: ","Rs.",dd*5)
    elif rd<=30 and rd>dt.day()and rd>(dt.day()+10) and rm<dt.month() and ry==dt.year():
        dd=10-(rd-dt.day()+10)
        print("\t\tLate Fine: ","Rs.",dd*5)
    elif rd<=30 and rd<dt.day() and rm<dt.month() and ry==dt.year():
        dd=(dt.day()+30)-rd
        print("\t\tLate Fine: ","Rs.",dd*5)
    elif rd<=30 and rd>dt.day()and rd>(dt.day()+10) and rm>dt.month() and ry<dt.year():
        dd=10-(rd-(dt.day()+10))
        print("\t\tLate Fine: ","Rs.",dd*5)
    else:
        print("\t\tLate Fine: None")
