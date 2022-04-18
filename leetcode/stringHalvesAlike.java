// https://leetcode.com/problems/determine-if-string-halves-are-alike/
// easy AF
class Solution {
    public static boolean isVowel(char ch){
        return ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u' || ch == 'A' || ch == 'E' || ch == 'I' || ch == 'O' || ch == 'U';
    }
    public boolean halvesAreAlike(String s) {
        int a = 0, b = 0, l = s.length();
        int z = l%2==0 ? l/2 : l/2+1;
        for(int i=0;i<l/2;i++){
            if(isVowel(s.charAt(i))){
                a++;
            }
            if(isVowel(s.charAt(z+i))){
                b++;
            }
            
        }
        return a==b;
    }
}
