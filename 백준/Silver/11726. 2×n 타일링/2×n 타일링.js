function solution(n) {
  let dp = new Array(n + 1).fill(0);
  for (let i = 0; i <= n; i++) {
    if (i === 0) {
      dp[i] = 0;
    } else if (i === 1) {
      dp[i] = 1;
    } else if (i === 2) {
      dp[i] = 2;
    } else {
      dp[i] = (dp[i - 1] + dp[i - 2]) % 10007;
    }
  }

  console.log(dp[n]);
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

  solution(n);

  process.exit();
});
