//Find the smallest integer in an array

public class SmallestIntegerFinder {
    public static int findSmallestInt(int[] args) {
        int minValue = args[0]; 
        for(int i = 1; i < args.length; i++){ 
            if(args[i] < minValue){ 
              minValue = args[i]; 
            } 
        } 
    return minValue; 
    } 
}
