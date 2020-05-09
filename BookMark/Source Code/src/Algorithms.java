/**
 *
 * @author Sodip Bikram Thapa, Aaryan Shrestha, Meru Sangroula
 * 
 */

import java.util.LinkedList;

public class Algorithms {
    
    LinkedList<DataModel> SelectionSort(LinkedList<DataModel> LL){
         int n = LL.size(); 
        // One by one move boundary of unsorted subarray
        for (int i = 0; i < n-1; i++)
        {
            // Find the minimum element in unsorted array
            int min_idx = i;
            for (int j = i+1; j < n; j++)
                if ((Double)LL.get(j).getPrice() < (Double)LL.get(min_idx).getPrice()){
                    min_idx = j;
                }
            // Swap the found minimum element with the first
            // element
            DataModel temp = LL.get(min_idx);
            LL.set(min_idx, LL.get(i));
            LL.set(i,temp);
        }
        return LL;
    }
    
    DataModel BinarySearch (LinkedList<DataModel> LL,int low,int high,double price){
        if (high>0) 
        { 
            int mid = low+((high-low)/2); 
   
            // If the element is present at the  
            // middle itself 
            if (LL.get(mid).getPrice() == price) {
               return LL.get(mid); 
            // If element is smaller than mid, then  
            // it can only be present in left subarray 
            }else if (LL.get(mid).getPrice() > price){
               return BinarySearch(LL, low, mid-1, price); 
            }else{
                return BinarySearch(LL, mid+1, high, price);
            }
            // Else the element can only be present 
            // in right subarray 
                 
        } else{
            return null;
        }
    }
    
    LinkedList<DataModel> LinearSearch(LinkedList<DataModel> LL,String genre){
        LinkedList<DataModel> LL2=new LinkedList<>();
        for (int i=0;i<=LL.size()-1;i++){
            if (LL.get(i).getGenre().equals(genre)){
                LL2.add(LL.get(i));
            }
        }
        return LL2;
    }
}
