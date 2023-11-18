import java.util.*;
import java.util.stream.*;

class Solution {    
    public int[] solution(int[] progresses, int[] speeds) {
        List<Integer> answer = new ArrayList<>();
        
        Queue<Integer> queue = new LinkedList<>();
        for (int num : progresses) {
            queue.offer(num);
        }
        
        int day = 0;
        int index = 0;

        while (queue.size() > 0) {
            day++;
            int removed = 0;
            
            while (true) {
                if (index >= speeds.length) {
                    break;
                }
                
                int inc = day * speeds[index];
                int progress = queue.peek() + inc;

                if (progress >= 100) {
                    queue.remove();
                    index++;
                    removed++;
                    continue;
                }

                break;
            }
            
            if (removed > 0) {
                answer.add(removed);
            }
        }
        
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}