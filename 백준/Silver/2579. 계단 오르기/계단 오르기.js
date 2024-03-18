function solution(n, scores) {
	let dp = new Array(n + 1).fill(0)
	for (let i = 0; i <= n; i++) {
		if (i === 1) {
			dp[i] = scores[1]
		} else if (i === 2) {
			dp[i] = scores[1] + scores[2]
		} else if (i === 3) {
			dp[i] = Math.max(scores[1], scores[2]) + scores[3]
		} else {
			dp[i] = Math.max(dp[i - 3] + scores[i - 1] + scores[i], dp[i - 2] + scores[i])
		}
	}
	console.log(dp[n])
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
	const stairLen = parseInt(input[0])
	let scores = [0]
	for (let i = 0; i < stairLen; i++) {
		scores.push(parseInt(input[i + 1]))
	}
	solution(stairLen, scores)
	process.exit()
})
