function solution(n) {
  // 바텀업 (반복문) 으로
  let dp = Array.from({ length: n + 1 }, () => {
    return new Array(2).fill(0);
  });
  for (let i = 0; i <= n; i++) {
    if (i === 0) {
      dp[i][0] = 1;
      dp[i][1] = 0;
    } else if (i === 1) {
      dp[i][0] = 0;
      dp[i][1] = 1;
    } else {
      dp[i][0] = dp[i - 1][0] + dp[i - 2][0];
      dp[i][1] = dp[i - 1][1] + dp[i - 2][1];
    }
  }
  console.log(dp[n].join(" "));
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
  const t = parseInt(input[0]);

  for (let i = 0; i < t; i++) {
    const n = parseInt(input[i + 1]);
    solution(n);
  }

  process.exit();
});
