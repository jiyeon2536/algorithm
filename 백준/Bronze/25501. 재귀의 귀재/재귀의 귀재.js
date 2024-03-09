function solution(s) {
  const sLen = s.length;
  let cnt = 0;

  function recursion(s, l, r) {
    cnt++;
    if (l >= r) return 1;
    else if (s[l] != s[r]) return 0;
    else return recursion(s, l + 1, r - 1);
  }

  function isPalindrome() {
    return recursion(s, 0, sLen - 1);
  }

  console.log(isPalindrome(), cnt);
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
    const s = input[i + 1];
    solution(s);
  }

  process.exit();
});
