function solution(x, sum) {
  if (x === sum) {
    console.log("Yes");
  } else {
    console.log("No");
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
  let x = parseInt(input[0]); // 총 금액
  let n = parseInt(input[1]); // 물건의 개수
  let list = new Array(n); // 가격, 개수 담을 배열
  let sum = 0; // 총 금액
  for (let i = 0; i < n; i++) {
    // 개수만큼의 입력
    list[i] = input[i + 2].split(" ").map((el) => parseInt(el));
    sum += list[i][0] * list[i][1]; // 가격 * 개수
  }

  solution(x, sum);
  process.exit();
});
