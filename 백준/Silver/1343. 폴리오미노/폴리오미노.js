// 폴리오미노

// 짝수가 아니면 덮지 못함
// .으로 나누어진 것이 짝수가 아니면 덮지 못함.
// 4의 배수까지는 최대한 A로 덮음
// 남은 2의 배수는 B로 덮음
function solution(list) {
  const n = list.length;
  let answer = new Array();
  let numX = 0;

  for (let i = 0; i < n; i++) {
    if (numX === 4) {
      answer.push("AAAA");
      numX = 0;
    }

    if (list[i] === "X") {
      numX++;
      continue;
    } else if (list[i] === ".") {
      if (numX === 0) {
        answer.push(".");
      } else if (numX % 2 !== 0) {
        console.log(-1);
        return;
      } else if (numX === 4) {
        answer.push("AAAA.");
        numX = 0;
      } else if (numX === 2) {
        answer.push("BB.");
        numX = 0;
      } else {
        answer.push(".");
      }
    }
  }
  if (numX === 4) {
    answer.push("AAAA");
    numX = 0;
  } else if (numX === 2) {
    answer.push("BB");
    numX = 0;
  } else if (numX !== 0) {
    console.log(-1);
    return;
  }

  console.log(answer.join(""));
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
  const list = input[0];

  solution(list);

  process.exit();
});
