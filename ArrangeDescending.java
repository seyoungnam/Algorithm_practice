package algoPractice;

import java.util.Arrays;
import java.util.Collections;

public class ArrangeDescending {
	//My Answer
     public String solution(String s) {
         String answer = "";
         
         String[] array = s.split("");
         Arrays.sort(array, Collections.reverseOrder());
         
         StringBuilder builder = new StringBuilder();
         for( String v : array ) { builder.append(v); }
         answer = builder.toString();

         return answer;
     }
     
     //Best Answer
     public String reverseStr(String str){
    	 char[] sol = str.toCharArray();
    	 Arrays.sort(sol);
    	 return new StringBuilder(new String(sol)).reverse().toString();
    }
   

   public static void main(String[] args) {
      ArrangeDescending instance = new ArrangeDescending();
      String s = "Zbcdefg";
      
      System.out.println(instance.solution(s));
      

   }

}