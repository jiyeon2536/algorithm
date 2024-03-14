function solution(w, h, seaMap) {
	const di = [0, 0, 1, -1, -1, 1, -1, 1]
	const dj = [1, -1, 0, 0, -1, 1, 1, -1]

	// console.log(seaMap)

	let answer = 0
	let visited = Array.from({ length: h }, () => {
		return new Array(w).fill(0)
	})

	function bfs(stI, stJ) {
		let queue = new Array()
		queue.push([stI, stJ])
		visited[stI][stJ] = 1
		while (queue.length > 0) {
			const tmp = queue.shift()
			const nowR = tmp[0]
			const nowC = tmp[1]
			for (let k = 0; k < 8; k++) {
				const ni = nowR + di[k]
				const nj = nowC + dj[k]
				if (0 <= ni && ni < h && 0 <= nj && nj < w && seaMap[ni][nj] === '1' && visited[ni][nj] === 0) {
					visited[ni][nj] = 1
					queue.push([ni, nj])
				}
			}
		}
	}

	for (let r = 0; r < h; r++) {
		for (let c = 0; c < w; c++) {
			if (seaMap[r][c] === '1' && visited[r][c] === 0) {
				bfs(r, c)
				answer += 1
			}
		}
	}

	// console.log(visited)

	console.log(answer)
}

const readline = require('readline')
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout,
})

let input = []
rl.on('line', function (line) {
	input.push(line)
}).on('close', function () {
	let st = 0
	while (st < input.length) {
		const [w, h] = input[st].split(' ').map(Number)

		if (w === 0 && h === 0) process.exit()

		let seaMap = new Array()

		for (let i = st; i < st + h; i++) {
			const inner = Array.from(input[i + 1])
			const filtered = inner.filter((value) => {
				return value !== ' '
			})
			seaMap.push(filtered)
		}

		solution(w, h, seaMap)
		st += h + 1
	}
})
