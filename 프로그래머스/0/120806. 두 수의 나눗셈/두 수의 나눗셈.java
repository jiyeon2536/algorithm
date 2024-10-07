class Solution {
    public int solution(int num1, int num2) {
        double divided = num1 / (double)num2;
        double tmp = divided * 1000.0;
        int answer = (int) tmp;
        return answer;
    }
}