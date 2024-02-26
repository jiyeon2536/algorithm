function solution(word) {
    console.log(`${word}??!`)
}

const readline = require('readline')
const rl = readline.createInterface({
    input : process.stdin,
    output : process.stdout
})

let input = []
rl.on('line', function(line){
    input.push(line)
}).on('close', function() {
    let word = input[0]
    // let list = input[0].split(' ').map((el) => parseInt(el))
    solution(word)
    process.exit()
})