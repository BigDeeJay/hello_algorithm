import java.util.*;

class Solution {
    List<int[]> moved = new ArrayList<>();
    
    public List<?> solution(int n) {
        hanoi(n, 1, 2, 3);
        return moved;
    }
    
    void hanoi(int count, int from, int temp, int to) {
        if (count == 1) {
            moved.add(new int[] { from, to });
            return;
        }
        
        hanoi(count - 1, from, to, temp);
        moved.add(new int[] { from, to });
        hanoi(count - 1, temp, from, to);
    }
}