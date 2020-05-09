/**
 *@This is the DataModel class which is used to access data of books for the algorithms
 * 
 * @author Sodip Bikram Thapa, Aaryan Shrestha, Meru Sangroula
 * @date 2020-01-17
 */
public class DataModel {
    //variable initialization
    int bookID;
    String bookName,author,bookType,genre,publication;
    double price;
    
    DataModel(int bookID,String bookName,String author,String bookType,String genre,String publication, double price){
        //method to give value to the variables of this class
        this.bookID=bookID;
        this.bookName=bookName;
        this.author=author;
        this.bookType=bookType;
        this.genre=genre;
        this.publication=publication;
        this.price=price;
    }
    
    int getBookID(){    //method to return book id
        return bookID;
    }
    
    String getBookName(){   //method to return book name
        return bookName;
    }
    
    String getAuthor(){ //method to return author
        return author;
    }
    
    String getBookType(){   ////method to return book type
        return bookType;
    }
    
    String getGenre(){  //method to return genre
        return genre;
    }
    
    String getPublication(){    //method to return publication
        return publication;
    }
    
    double getPrice(){  //method to return price
        return price;
    }
}
