public class Solution {
    public int lengthOfLastWord(String s) {
        String[] strs = s.split("\\s+");
        String word = strs[strs.length-1];
        return word.length();
    }
}
