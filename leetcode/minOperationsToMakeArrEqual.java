// https://leetcode.com/problems/minimum-operations-to-make-array-equal/
class Solution {
    public int minOperations(int n) {
        /*
        odd n
        1 3 5 7 9
        1 5 5 5 9 (2)
        5 5 5 5 5 (4) 
        ans = 6 (2 + 4 ... (n-1)/2 times)
        

        even n
        1 3 5 7 9 11
        1 3 6 6 9 11 (1)
        1 6 6 6 6 11 (3)
        6 6 6 6 6 6  (5)
        ans = 9 (1+3+5 .. n/2 times)
        
        series sum Sn =  ½ n [ 2a + (n - 1)d ]
        */
        // even
        if(n%2==0){
            // n/(2*2) (2(1) + (n/2-1)2)
            // n/4(2+n-2)
            // n^2/4
            return n*n/4;
        } else {
            // odd
            // (n-1)/(2*2)*(2(2) + ((n-1)/2 - 1)*2)
            // (n-1)/4*(4+n-3) = (n^2-1)/4
            return (n*n-1)/4;
        }
    }
}
