function solution(n, list) {
  // 1. 초기의 배열을 내림차순 정렬한다.
  list.sort((b, a) => a - b);
  // console.log(list);

  // 2. 초기의 배열을 돌면서, 인덱스 + 1 을 숫자에 곱해서 넣어준다.
  const multipled = list.map((el, idx) => {
    return el * (idx + 1);
  });

  // console.log(multipled);
  // 3. 그중에서 가장 큰 값을 찾는다.
  const answer = Math.max(...multipled);
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
  // 로프의 개수
  const n = parseInt(input[0]);

  // 로프중량 배열
  let list = new Array(n);
  for (let i = 0; i < n; i++) {
    list[i] = parseInt(input[i + 1]);
  }

  solution(n, list);

  process.exit();
});
