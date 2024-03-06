function solution(n, heights) {
  let answer = 0;
  let stack = [];
  // list를 순회하면서,
  // 첫번쨰 원소를 스택에 넣는다.
  // 그다음 원소 차례.
  // 스택에서 원소보다 큰 아이가 나올때까지 팝한다.
  // 나를 볼수 있는 소들의 숫자를 더해주는 거임.

  // peek이 해당 건물보다 높이가 작으면 스택에서 pop 하고
  // 더 크면 해당 건물을 스택에 push
  // 그래서 stack 길이에서 -1 해서 result 변수에 더해준다.

  heights.forEach((el) => {
    while (stack.length > 0 && stack[stack.length - 1] <= el) {
      stack.pop();
    }
    answer += stack.length;
    stack.push(el);
  });

  console.log(answer);
}

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];
rl.on("line", function (line) {
  input.push(line);
}).on("close", function () {
  const n = parseInt(input[0]);
  const heights = new Array(n).fill(0);
  for (let i = 0; i < n; i++) {
    heights[i] = parseInt(input[i + 1]);
  }
  solution(n, heights);

  process.exit();
});
