// https://leetcode.com/problems/global-and-local-inversions/
class Solution {
    public boolean isIdealPermutation(int[] A) {
        int l = A.length;
        // O(N^2) SOLUTION
        // basically all local inversions are global, so if we find 1 extra global just return false
        /*
        for(int i=0;i<l;i++){
            for(int j=i+2;j<l;j++){
                if(A[i]>A[j]){
                    return false;
                }
            }
        }
        return true;
        */
        // O(N) solution
        for(int i = 0;i<l-1;i++){
            // if at right place, go on
            if(i==A[i]){
                continue;
            } 
            // if neighbour elements swaped, go on and skip next(as we checked already)
            if(i+1==A[i] && A[i+1]==i){
                i++;
                continue;
            }
            // else just accept the fate
            return false;
        }
        return true;
    }
}
