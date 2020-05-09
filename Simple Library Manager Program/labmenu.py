import display as d
import dime as dt
import read as r
import receipt as R
import write as ww
def labmenu():
    List=r.readbooks()
    year=dt.year()
    month=dt.month()
    day=dt.day()
    ui=1
    ui2=2
    ui3=3
    print("\t\t\tLIBRARY MENU\n\t\t\t------------\n\t\tNOTE: STUDENT MUST BE FIRST ADDED AS MEMBER OF THE LIBRARY\n\n\t\tEnter 1 to display book list\n\t\tEnter 2 to borrow\n\t\tEnter 3 to return")
    user_input=int(input("\t\tEnter 4 to Add a new member\n\t\tEnter 5 to exit: "))
    try:
        if user_input==1:
            d.displaybooklist(List)
            labmenu()
        elif user_input==2:
            d.displaybooklist(List)
            name=input("Enter full name of the Student: ")
            sid=input("Enter their Student ID: ")
            if len(sid)>14 or len(sid)<14:
                print("Invalid Student ID!")
                labmenu()
            else:
                listy=r.readlist2(sid)
                if sid==listy[0]:
                    print("Student hasn't returned the books they've borrowed previously.")
                    labmenu()
                else:
                    book_b=int(input("Enter the S.N. of the book that you want to borrow: ")) 
                    op=input("Do you want to borrow one more book(y/n)? ")
                    while ui==1:
                        if op=="y":
                            book_b2=int(input("Enter the S.N. of the other book: "))
                            if book_b2==book_b:
                                print("You can't borrow multiple copies of the same book!")
                            else: 
                                R.borrow2(name,sid,book_b,book_b2,day,month,year)
                                List2=ww.owrite2(List,book_b,book_b2)
                                ww.owrite3(List2)
                                ww.userdata2(sid,name,List[book_b][1],book_b,List[book_b][4],List[book_b2][1],book_b2,List[book_b2][4],day,month,year)
                                ui=2
                                labmenu()
                        elif op=="n":    
                            R.borrow(name,sid,book_b,day,month,year)
                            ww.userdata(sid,name,List[book_b][1],book_b,List[book_b][4],day,month,year)
                            List2=ww.owrite(List,book_b)
                            ww.owrite3(List2)
                            ui=2
                            lanmenu()
                        else:
                            print("Invalid Input!")
                            labmenu()
        elif user_input==3:
            d.displaybooklist(List)
            sid=input("Enter your Student ID: ")
            while ui3==3:
                if len(sid)>14 or len(sid)<14:
                    print("Invalid Student ID!")
                else:
                    ui3=4
            try:
                rlist=r.readlist2(sid)
                try:    
                    q=int(rlist[-1])
                    SN1=int(rlist[3])
                    SN2=int(rlist[6])
                    if q==2:
                        R.returns2(rlist)
                        file3=open(sid+".txt","w").close
                        List[SN1][3]=int(List[SN1][3])+1
                        List[SN2][3]=int(List[SN2][3])+1
                        ww.owrite3(List)
                        labmenu()
                    elif q==1:
                        R.returns1(rlist)
                        file3=open(sid+".txt","w").close
                        List[SN1][3]=int(List[SN1][3])+1
                        ww.owrite3(List)
                        labmenu()
                except:
                    print("The Student Hasn't Borrowed Any Books!")
                    labmenu()
            except:
                print("Invalid Member!")
                labmenu()
                
        elif user_input==4:
            sid=input("Enter the Student ID of the student you want to add as a member: ")    
            if len(sid)>14 or len(sid)<14:
                print("Invalid Student ID!")
                labmenu()
            else: 
                file=open(sid+".txt","w").close()
                print("Member successfully added!")
                labmenu()
        elif user_input==5:
            print("Thank You!")
    except:
        print("Invalid!")
        labmenu()
labmenu()

