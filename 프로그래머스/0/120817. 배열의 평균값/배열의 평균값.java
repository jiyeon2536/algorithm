class Solution {
    public double solution(int[] numbers) {
        double answer = 0;
        int len = numbers.length;
        int total = 0;
        
        for (int i = 0; i < len; i++) {
            total += numbers[i];
        }
        
        answer = (double) total / len;
        
        return answer;
    }
}