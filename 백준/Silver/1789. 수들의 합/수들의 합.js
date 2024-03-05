function solution(s) {
  // 1부터 자기자신까지를 더해놓은 배열이 있다고 생각해보자
  // 1, 3, 6, 10 ... 이런식으로 전개될 것이다.
  // 만약 입력값이 8이라면
  // 8은 6과 10사이의 어느 값이다.
  // 네번째니까 1부터 4까지를 더한 합이다.
  // 여기에서 2가 넘치기 때문에 2를 빼주면 된다.
  // 그러면 총 3개임.

  // 10, 15, 21, 28, ... 이렇게 간다면
  // 만약 입력값이 22 라면
  // 이는 28에서 6을 뺀 값이다
  let sfoCnt = 1;
  let sumFromOne = 1;
  // 같아지거나 커지면 빠져나와야함
  while (sumFromOne < s) {
    sfoCnt++;
    sumFromOne += sfoCnt;
  }

  let answer = 0;

  //   console.log(sfoCnt);
  //   console.log(sumFromOne);
  // 가장 인접한 크거나 같은 1부터 거기까지의 수
  if (sumFromOne === s) {
    answer = sfoCnt;
  } else {
    answer = sfoCnt - 1;
  }

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
  const s = parseInt(input[0]);

  solution(s);

  process.exit();
});
