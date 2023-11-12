import java.util.*;

class Solution {
    public int[] solution(int[] fees, String[] records) {
        int[] answer = {};
        Map<String, Car> carMap = new HashMap<>();
    
        for (int i = 0; i < records.length; i++) {
            String[] record = records[i].split(" ");
            
            String time = record[0];
            String name = record[1];
            String type = record[2];
            
            if (!carMap.containsKey(name)) {
                carMap.put(name, new Car());
            }
            
            Car parkedCar = carMap.get(name);
            
            if (type.equals("IN")) {
                // IN이면 값 넣기
                parkedCar.setTime(transformToMinute(time));
                continue;
            }
            
            // OUT이면 값 초기화 후 minute 더해주기
            parkedCar.addMinute(transformToMinute(time) - parkedCar.getTime());
        }
        
        List<String> keySet = new ArrayList<>(carMap.keySet());
        Collections.sort(keySet);
        answer = new int[keySet.size()];
        int index = 0;
        
        for (String key : keySet) {
            Car parkedCar = carMap.get(key);
            parkedCar.flush();            
            answer[index] = getTotalFee(fees, parkedCar);
            index++;
        }
        
        return answer;
    }
    
    int getTotalFee(int[] fees, Car car) {
        int def_time = fees[0];
        int def_fee = fees[1];
        int unit_time = fees[2];
        int unit_fee = fees[3];
        
        // System.out.println("total = " + car.getTotal());
        // System.out.println(Math.ceil((car.getTotal() - def_time) / unit_time));
        
        if (car.getTotal() - def_time  <= 0) {
            return def_fee;
        }
        
        return def_fee + (int) (Math.ceil((double) (car.getTotal() - def_time) / (double) unit_time)
            * unit_fee);
    }
    
    int transformToMinute(String time) {
        String[] times = time.split(":");
        return (Integer.parseInt(times[0]) * 60) + Integer.parseInt(times[1]);
    }
    
    class Car {
        public int latestInTime;
        public int parkedMinute;
        
        public void addMinute(int minute) {
            this.parkedMinute += minute;
            latestInTime = -1;
        }
        
        public int getTotal() {
            return parkedMinute;
        }
        
        public int getTime() {
            return latestInTime;
        }
        
        public void setTime(int time) {
            this.latestInTime = time;
        }
        
        public void flush() {
            if (latestInTime == -1) {
                return;
            }
            
            addMinute(transformToMinute("23:59") - latestInTime);
        }
        
        @Override
        public String toString() {
            return "p_min = " + parkedMinute;
        }
    }
}