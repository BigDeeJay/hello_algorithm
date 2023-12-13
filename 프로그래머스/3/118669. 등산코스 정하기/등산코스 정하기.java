import java.util.*;

class Solution {
    class Node implements Comparable<Node> {
        int index;
        int cost;
        
        Node(int index, int cost) {
            this.index = index;
            this.cost = cost;
        }
        
        @Override
        public int compareTo(Node o) {
            return Integer.compare(this.cost, o.cost);
        }
    }
    
    List<Node>[] graph;
    
    public int[] solution(int n, int[][] paths, int[] gates, int[] summits) {
        graph = new ArrayList[n + 1];
        
        for (int i = 0; i < n + 1; i++) {
            graph[i] = new ArrayList<>();
        }
        
        for (int[] path : paths) {
            graph[path[0]].add(new Node(path[1], path[2]));
            graph[path[1]].add(new Node(path[0], path[2]));
        }
        
        int[] intensities = new int[n + 1];
        Arrays.fill(intensities, Integer.MAX_VALUE);
                    
        PriorityQueue<Node> pq = new PriorityQueue<>();
        for (int gate : gates) {
            pq.offer(new Node(gate, 0));
            intensities[gate] = 0;
        }
        
        while (!pq.isEmpty()) {
            Node node = pq.poll();
            boolean sValid = true;
            for (int s : summits) {    
                if (node.index == s) {
                    sValid = false;
                }
            }
            
            // 현재 위치가 산봉우리면 패스 -> 올라가는 경로 = 내려가는 경로
            if (!sValid) {
                continue;
            }
        
            // 현재 위치에 도달한 비용이 기존 비용보다 크면 패스
            if (node.cost > intensities[node.index]) {
                continue;
            }
            
            for (Node next : graph[node.index]) {
                // System.out.println("next = " + next.index);
                int maxCost = (next.cost == Integer.MAX_VALUE) ?
                    node.cost : Math.max(node.cost, next.cost);
                
                // 결정된 intensity끼리 비교해서 최소값을 최종 intensities에 저장
                if (maxCost < intensities[next.index]) {
                    intensities[next.index] = maxCost;
                    
                    // 현 노드 위치의 최소 intensity 값을 유지한 상태로 pq 추가
                    pq.add(new Node(next.index, maxCost));
                }
            }
        }
        
        int idx = -1;
        int minCost = Integer.MAX_VALUE;

        Arrays.sort(summits);
        for (int i = 0; i < summits.length; i++) {
            // 각 봉우리의 intensity를 확인하고 최소 intensity를 갱신한다
            if (intensities[summits[i]] < minCost) {
                minCost = intensities[summits[i]];
                idx = summits[i];
            }
        }
        
        // System.out.println("inten = " + Arrays.toString(intensities));
        
        return new int[] { idx, minCost };
    }
}