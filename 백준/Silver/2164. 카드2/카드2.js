class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
    this.prev = null;
  }
}

class LinkedList {
  constructor() {
    this.head = null;
    this.tail = null;
    this.length = 0;
  }

  push(value) {
    const newNode = new Node(value);

    if (!this.head) {
      this.head = newNode; // 헤드가 널(초기)면 이번에 넣은 값이 헤드임
    } else {
      this.tail.next = newNode; // 이미 있으면 꼬리 뒤에 넣어주고
      newNode.prev = this.tail; // 그 아이의 이전값을 꼬리로 엮어줌
    }
    this.tail = newNode; // 여기도 마지막을 뉴노드로 갱신해줌
    this.length++; // 길이도 하나 추가해줌
    return newNode;
  }

  getHead() {
    return this.head.value; // 맨 앞 값
  }

  removeHead() {
    this.head = this.head.next; // 뒤에 값으로 바꿔주고
    this.head.prev = null; // 앞의 값을 널로 바꿔줌
    this.length--; // 길이도 줄인다
  }

  getSize() {
    return this.length;
  }
}

function solution(n) {
  const list = new LinkedList();

  for (let i = 0; i < n; i++) {
    list.push(i + 1);
  }

  while (list.getSize() > 1) {
    list.removeHead();
    list.push(list.getHead());
    list.removeHead();
  }
  console.log(list.getHead());
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
  solution(n);
  process.exit();
});
