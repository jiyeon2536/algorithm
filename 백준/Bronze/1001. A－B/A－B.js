function solution(list) {
    let answer = list[0] - list[1]
    console.log(answer)
    
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
    let list = input[0].split(' ').map((el) => parseInt(el))
    solution(list)
    process.exit()
})