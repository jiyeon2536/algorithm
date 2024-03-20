function solution(a, b, c) {
	if (a < b && b < c) {
		console.log(a, b, c)
	} else if (a < c && c < b) {
		console.log(a, c, b)
	} else if (b < c && c < a) {
		console.log(b, c, a)
	} else if (b < a && a < c) {
		console.log(b, a, c)
	} else if (c < a && a < b) {
		console.log(c, a, b)
	} else {
		console.log(c, b, a)
	}
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
	const [a, b, c] = input[0].split(' ').map(Number)
	solution(a, b, c)
	process.exit()
})
