function solution(n, list) {
  const max = Math.max(...list);
  let sum = 0;
  list.map((el) => {
    el = (el / max) * 100;
    sum += el;
  });
  console.log(sum / n);
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
  let n = parseInt(input[0]);
  let list = input[1].split(" ").map((el) => parseInt(el));
  solution(n, list);
  process.exit();
});
