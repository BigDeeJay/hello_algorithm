class Solution {
    public int solution(int n, int[][] results) {
        int answer = 0;
        boolean[][] graph = new boolean[n][n];
        
        for (int[] result : results) {
            int win = result[0] - 1;
            int lose = result[1] - 1;
            
        	graph[win][lose] = true;
        }
        
        int count = 0;
        for (int p = 0; p < n; p++) {
        	int lose = countBehind(p, graph, new boolean[n]) - 1;
        	int win = countFront(p, graph, new boolean[n]) - 1;
            
            if (lose + win + 1 == n) {
                count += 1;
            }
        }
        
        return count;
    }
    
    public int countBehind(int node, boolean[][] graph, boolean[] visited) {
        int count = 1;
        
        for (int i = 0; i < graph.length; i++) {
            if (!graph[i][node] || visited[i]) {
                continue;
            }
            visited[i] = true;
            count += countBehind(i, graph, visited);
        }
        
        return count;
    }
    
    public int countFront(int node, boolean[][] graph, boolean[] visited) {
        int count = 1;
        
        for (int i = 0; i < graph[node].length; i++) {
            if (!graph[node][i] || visited[i]) {
                continue;
            }
            visited[i] = true;
            count += countFront(i, graph, visited);
        }
        
        return count;
    }
}