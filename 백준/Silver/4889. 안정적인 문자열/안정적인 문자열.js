function solution(s, turn) {
  // 스트링을 순회하면서
  // 스택에 넣을 건데
  // stack[-1]이 {인데 }가 오면
  // 스택에서 꺼낸다
  // 요소가 {} 가 아니면 그냥 넘어간다.
  // 나머지는 그냥 스택에 넣는다
  // {이면 open에 +1
  // }이면 close 에 +1
  // 순회를 마쳤는데 스택에 남아있으면
  // opening closing 차이를 op에 더한다.
  let stack = [];
  let opening = 0;
  let closing = 0;
  const n = s.length;

  for (let i = 0; i < n; i++) {
    if (s[i] === "{" || s[i] === "}") {
      const m = stack.length;
      if (m !== 0) {
        const peek = stack[m - 1];
        if (peek === "{" && s[i] === "}") {
          stack.pop();
          opening -= 1;
          continue;
        }
      }
      if (s[i] === "{") opening++;
      else if (s[i] === "}") closing++;
      stack.push(s[i]);
    }
  }
  let operation = 0;
  operation += Math.floor(opening / 2) + Math.floor(closing / 2);
  operation += (opening % 2) + (closing % 2);

  console.log(`${turn}. ${operation}`);
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
  const inputLen = input.length;
  for (let j = 0; j < inputLen - 1; j++) {
    solution(input[j], j + 1);
  }
  process.exit();
});
