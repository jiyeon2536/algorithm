function solution(sizes) {
    var answer = 0;
    let bigOfBig = 0;
    let bigOfSmall = 0;
    for (item of sizes) {
        let w = item[0];
        let h = item[1];
        if (w > h) {
            if (w > bigOfBig) {
                bigOfBig = w;
            }
            if (h > bigOfSmall) {
                bigOfSmall = h;
            } 
        } else {
            if (h > bigOfBig) {
                bigOfBig = h;
            }
            if (w > bigOfSmall) {
                bigOfSmall = w; 
            }
        }
    }
    answer = bigOfBig * bigOfSmall
    return answer;
}