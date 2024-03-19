function solution(n, l, leaks) {
	leaks.sort((a, b) => a - b)
	let answer = 1 // 사용한 테입 개수
	let start = leaks[0] - 0.5
	let end = start + l

	for (let i = 1; i < n; i++) {
		if (leaks[i] < end) {
			continue
		} else {
			answer++
			start = leaks[i] - 0.5
			end = start + l
		}
	}
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
	const [n, l] = input[0].split(' ').map(Number)
	const leaks = input[1].split(' ').map(Number)
	solution(n, l, leaks)
	process.exit()
})
