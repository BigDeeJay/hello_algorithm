import java.util.*;

class Solution {
    int[][] a_land;
    
    public int solution(int[][] land) {
        int answer = 0;
        boolean[][] isVisited = new boolean[land.length][land[0].length];
        List<Place> finds = new ArrayList<>();
        
        for (int i = 0; i < land.length; i++) {
            for (int j = 0; j < land[0].length; j++) {
                if (land[i][j] > 0 && !isVisited[i][j]) {
                    Place place = process(i, j, land, isVisited, new Place(new HashSet<>(), 1));
                    if (place.amount > 0) {
                    	finds.add(place);
                	}
                }
            }
        }
        
        int maxAmount = Integer.MIN_VALUE;
        int[] result = new int[land[0].length];
        
        for (Place place : finds) {
        	for (int r : place.range) {
                result[r] += place.amount;
                maxAmount = Math.max(result[r], maxAmount);
            }    
        }
        
        
        //System.out.println("result = " + Arrays.toString(result));
        return maxAmount;
    }
    
    // 석유량 계산함수
    Place process(int init_y, int init_x, int[][] land, boolean[][] isVisited, Place place) {
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[] { init_y, init_x });
        Set<Integer> range = place.range;
        int amount = 0;
        
        while (!queue.isEmpty()) {
            int[] xy = queue.poll();
            int y = xy[0];
            int x = xy[1];
        
            if (land[y][x] == 0 || isVisited[y][x]) {
                continue;
            }

        	amount += 1;
            range.add(x);
            isVisited[y][x] = true;
            
            if (y - 1 > -1) {
                queue.add(new int[] { y - 1, x });
            }

            if (y + 1 < land.length) {
                queue.add(new int[] { y + 1, x });
            } 
            
            if (x - 1 > -1) {
                queue.add(new int[] { y, x - 1 });
            }     

            if (x + 1 < land[0].length) {
                queue.add(new int[] { y, x + 1 });            
            }
        }
                              
        return new Place(range, amount);
    }
    
    class Place {
        Set<Integer> range;
        int amount;
        
        public Place(Set<Integer> range, int amount) {
            this.range = range;
            this.amount = amount;
        }
    }
}