function solution(n, words) {
  const vals = Object.values(words);
  vals.sort((a, b) => b - a);
  let answer = 0;
  let count = 9;
  vals.forEach((el) => {
    answer += count * el;
    count--;
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
  let words = {};
  for (let i = 0; i < n; i++) {
    const word = input[i + 1];
    const len = word.length;
    for (let j = 0; j < len; j++) {
      const el = word[j];
      if (!words[el]) {
        words[el] = 10 ** (len - j - 1);
      } else {
        words[el] += 10 ** (len - j - 1);
      }
    }
  }
  solution(n, words);
  process.exit();
});
