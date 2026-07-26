//import java.util.*;
class Solution {
    public boolean isAnagram(String s, String t) {
        char[] sChar = s.toCharArray();
        char[] tChar = t.toCharArray();
        Arrays.sort(sChar);
        Arrays.sort(tChar);

        String sNew = new String(sChar);
        String tNew = new String(tChar);

        if(sNew.equals(tNew))
        return true;

        return false;
    }
}
