function solution(list) {
    const a = list[0]
    const b = list[1]
    if (a > b) {
        console.log('>')
    } else if (a < b) {
        console.log('<')
    } else {
        console.log('==')
    }
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