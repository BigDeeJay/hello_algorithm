import java.util.*;

class Solution {
    List<String> list = new ArrayList<>();
    List<String> keywords = List.of("A", "E", "I", "O", "U");
    boolean isFind = false;
    int count = 0;

    public int solution(String word) {
        int answer = 0;
        getCombi("", 0, word);
        // System.out.println("list = " + list);
        // return list.indexOf(word);
        return count - 1;
    }
    
    void getCombi(String output, int depth, String target) {
        if (isFind) {
            return;
        }
        
        // System.out.println(output);
        count++;
        if (output.equals(target)) {
            isFind = true;
            return;
        }
        
        if (depth == 5) {
            return;
        }
        
        for (int i = 0; i < keywords.size(); i++) {
            getCombi(output + keywords.get(i), depth + 1, target);
        }
    }
}