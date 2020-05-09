def readlist(book):# function to read database and return list
    booklist=open(book,"r")
    booklistd=booklist.readlines()
    return booklistd
    booklist.close() 
def readlist2(sid):# function to read file with same student id
    ulist=open(str(sid)+".txt","r")
    ulist1=ulist.read().split(',')
    return ulist1
def readbooks():# function to get 2D-list of the database
    booklist2d=[]
    booklist2=readlist("books.txt")
    for i in booklist2:
        booklist2d.append(i.replace("\n","").split(","))
    return booklist2d
