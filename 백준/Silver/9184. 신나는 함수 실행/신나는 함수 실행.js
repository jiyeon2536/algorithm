// dp 테이블 3차원배열 초기화
let dp = [];

for (let i = 0; i < 21; i++) {
  dp[i] = [];
  for (let j = 0; j < 21; j++) {
    dp[i][j] = [];
    for (let k = 0; k < 21; k++) {
      dp[i][j][k] = 0;
    }
  }
}

function w(a, b, c) {
  if (a <= 0 || b <= 0 || c <= 0) {
    return 1;
  }
  if (a > 20 || b > 20 || c > 20) {
    return w(20, 20, 20);
  }

  if (dp[a][b][c]) {
    return dp[a][b][c];
  }

  if (a < b && b < c) {
    return (dp[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c));
  } else {
    return (dp[a][b][c] =
      w(a - 1, b, c) +
      w(a - 1, b - 1, c) +
      w(a - 1, b, c - 1) -
      w(a - 1, b - 1, c - 1));
  }
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
  const n = input.length;

  for (let i = 0; i < n; i++) {
    const [a, b, c] = input[i].split(" ").map(Number);

    if (a === -1 && b === -1 && c === -1) {
      process.exit();
    } else {
      const answer = w(a, b, c);
      console.log(`w(${a}, ${b}, ${c}) = ${answer}`);
    }
  }
  process.exit();
});
