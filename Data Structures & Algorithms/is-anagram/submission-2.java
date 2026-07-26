//import java.util.*;
class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character,Integer> map1 = new HashMap<>();
        HashMap<Character,Integer> map2 = new HashMap<>();

        for(char c : s.toCharArray())
        map1.put(c,0);

        for(char c : t.toCharArray())
        map2.put(c,0);

        for(char c : s.toCharArray()) {
            int x = map1.get(c);
            x++;
            map1.put(c,x);
        }

        for(char c : t.toCharArray()) {
            int x = map2.get(c);
            x++;
            map2.put(c,x);
        }

        return map1.equals(map2) ? true : false;
    }
}
