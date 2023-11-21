import java.util.*;

class Solution {
    public int[] solution(String[] gems) {
        int[] answer = new int[2];
        
        // 보석 종류 정리
        Set<String> cleared_gems = new HashSet<String>(Arrays.asList(gems));        
        Map<String, Integer> picked = new HashMap<>();
        
        int start = 0;
        int distance = Integer.MAX_VALUE;
        
        // 보석 탐색
        for (int i = 0; i < gems.length; i++) {
            String endGem = gems[i];
            picked.put(endGem, picked.getOrDefault(endGem, 0) + 1);
            
            while (picked.get(gems[start]) > 1) {
                picked.put(gems[start], picked.get(gems[start]) - 1);
                start++;
            }
            
            if (picked.size() == cleared_gems.size() && distance > (i - start)) {
                distance = i - start;
                // answer = new int[] { start + 1, i + 1 };
                answer[0] = start + 1;
                answer[1] = i + 1;
            }
        }
        
        return answer;
    }
}