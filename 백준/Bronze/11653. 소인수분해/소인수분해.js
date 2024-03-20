function solution(n) {
	let answer = []
	let cur = n
	let i = 2

	while (i <= n) {
		while (cur % i === 0) {
			if (cur === 1) {
				break
			}
			cur = cur / i
			answer.push(i)
		}
		i++
	}

	answer.forEach((el) => console.log(el))
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
	const n = parseInt(input[0])
	if (n === 1) {
		process.exit()
	}
	solution(n)
	process.exit()
})
