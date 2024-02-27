function solution(n, v, graph) {
  // console.log(graph);
  let dfsAnswer = [v];
  let bfsAnswer = [];

  let dfsVisited = new Array(n + 1).fill(false);
  let bfsVisited = new Array(n + 1).fill(false);

  function dfs(n, v, graph) {
    dfsVisited[v] = true;
    // console.log(dfsAnswer);

    if (dfsAnswer.length === n) {
      return;
    } else {
      for (let j = 0; j < graph[v].length; j++) {
        if (!dfsVisited[graph[v][j]]) {
          // console.log(graph[v]);
          dfsVisited[graph[v][j]] = true;
          dfsAnswer.push(graph[v][j]);
          dfs(n, graph[v][j], graph);
        }
      }
    }
  }

  function bfs(n, v, graph) {
    let queue = [v];

    while (queue.length > 0) {
      const tmp = queue.shift();
      if (bfsVisited[tmp]) {
        continue;
      }
      bfsAnswer.push(tmp);
      bfsVisited[tmp] = true;

      for (let t = 0; t < graph[tmp][t]; t++) {
        if (!bfsVisited[graph[tmp][t]]) {
          queue.push(graph[tmp][t]);
        }
      }
    }

    return;
  }

  dfs(n, v, graph);
  bfs(n, v, graph);
  dfsAnswer = dfsAnswer.join(" ");
  console.log(dfsAnswer);
  bfsAnswer = bfsAnswer.join(" ");
  console.log(bfsAnswer);
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
  const [n, m, v] = input[0].split(" ").map(Number);
  let graph = new Array(n + 1);
  for (let i = 0; i < n + 1; i++) {
    graph[i] = new Array();
  }

  for (let i = 0; i < m; i++) {
    const [start, end] = input[i + 1].split(" ").map(Number);
    graph[start].push(end);
    graph[end].push(start);
  }

  graph.map((arr) => arr.sort((a, b) => a - b));

  solution(n, v, graph);

  process.exit();
});
