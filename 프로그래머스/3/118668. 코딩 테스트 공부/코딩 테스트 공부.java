import java.util.*;

class Solution {
    public int solution(int alp, int cop, int[][] problems) {
        int answer = 0;
        int al_max = Arrays.stream(problems)
            .map(problem -> problem[0])
            .max(Comparator.naturalOrder()).orElseThrow();
        int co_max = Arrays.stream(problems)
            .map(problem -> problem[1])
            .max(Comparator.naturalOrder()).orElseThrow();
        
        // 이미 모든 문제를 풀 수 있는 경우 0 반환
        if (alp >= al_max && cop >= co_max) {
            return 0;
        }
        
        if (alp >= al_max) {
            alp = al_max;
        }
        
        if (cop >= co_max) {
            cop = co_max;
        }
        
        // System.out.println("al_max = " + al_max);
        // System.out.println("co_max = " + co_max);
        int[][] dp = new int[al_max + 2][co_max + 2];
        for (int i = alp; i <= al_max; i++) {
            for (int j = cop; j <= co_max; j++) {
                dp[i][j] = Integer.MAX_VALUE;
            }
        }
        
        int[][] new_ps = Arrays.copyOf(problems, problems.length + 2);
        new_ps[problems.length] = new int[] { 0,0,0,1,1 };
        new_ps[problems.length + 1] = new int[] { 0,0,1,0,1 };
        
        // 초기화
        dp[alp][cop] = 0;
        
        for (int i = alp; i <= al_max; i++) {
            for (int j = cop; j <= co_max; j++) {	
                for (int[] problem : new_ps) {
                    dp[i+1][j]=Math.min(dp[i+1][j],dp[i][j]+1);
                    dp[i][j+1]=Math.min(dp[i][j+1],dp[i][j]+1);
                    // 문제를 못푸는 실력일 경우, 스킵
                    if (i >= problem[0] && j >= problem[1]) {
                        if (i + problem[2] > al_max && j + problem[3] > co_max) {
                            dp[al_max][co_max] = Math.min(dp[al_max][co_max], dp[i][j] + problem[4]);
                        } else if (i + problem[2] > al_max) {
                            dp[al_max][j + problem[3]] = Math.min(dp[al_max][j + problem[3]], dp[i][j] + problem[4]);
                        } else if (j + problem[3] > co_max) {
                            dp[i + problem[2]][co_max] = Math.min(dp[i + problem[2]][co_max], dp[i][j] + problem[4]);
                        } else if (i + problem[2] <= al_max && j + problem[3] <= co_max) {
                            dp[i + problem[2]][j + problem[3]] = Math.min(dp[i + problem[2]][j + problem[3]], dp[i][j] + problem[4]);
                        }
                    }
                }
            }
        }
        
        return dp[al_max][co_max];
    }
}