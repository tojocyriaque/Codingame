import java.util.*;
import java.io.*;
import java.math.*;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
class Solution {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        String b = in.nextLine();
        char[] B = b.toCharArray();
        
        int maxL = 0;
        for(int i=0; i<B.length; i++){
            if(B[i]=='0'){
                B[i] = '1';
                if(getMaxLen1(B)>maxL){
                    maxL=getMaxLen1(B);
                }
                B[i] = '0';
            }
        }

        System.out.println(maxL);

    }

    static int getMaxLen1(char[] arr){
        int maxLen1 = 0;
        int len = 0;
        for(char c: arr){
            if (c=='1'){
                len++;  
            }
            else{
                if(len>maxLen1){
                    maxLen1=len;
                }
                len=0;
            }
        }       
        if (len>maxLen1) maxLen1=len;

        return maxLen1;
    }

}
