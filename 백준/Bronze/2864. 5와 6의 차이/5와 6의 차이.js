function solution(a, b) {
	const aLen = a.length
	const bLen = b.length
	// 5, 6를 전부 5로 더하는 경우가 min
	// 5, 6를 전부 6로 더하는 경우가 max
	function findMin(a, b, aLen, bLen) {
		let newA = ''
		let newB = ''
		for (let i = 0; i < aLen; i++) {
			if (a[i] === '6') {
				newA += '5'
			} else {
				newA += a[i]
			}
		}

		for (let j = 0; j < bLen; j++) {
			if (b[j] === '6') {
				newB += '5'
			} else {
				newB += b[j]
			}
		}

		const minAnswer = Number(newA) + Number(newB)
		return minAnswer
	}

	function findMax(a, b, aLen, bLen) {
		let newA = ''
		let newB = ''
		for (let i = 0; i < aLen; i++) {
			if (a[i] === '5') {
				newA += '6'
			} else {
				newA += a[i]
			}
		}

		for (let j = 0; j < bLen; j++) {
			if (b[j] === '5') {
				newB += '6'
			} else {
				newB += b[j]
			}
		}

		const maxAnswer = Number(newA) + Number(newB)
		return maxAnswer
	}

	console.log(findMin(a, b, aLen, bLen), findMax(a, b, aLen, bLen))
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
	const [a, b] = input[0].split(' ')
	solution(a, b)
	process.exit()
})
