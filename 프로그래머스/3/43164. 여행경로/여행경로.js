function solution(tickets) {
    let visited = new Array(tickets.length).fill(false)
    let startAirport = 'ICN'
    const paths = []
    
    const dfs = (visited, stopover, paths) => {
        if (stopover.length === tickets.length + 1) {
            paths.push([...stopover])
        }
        for (let i = 0; i < tickets.length; i++) {
            const [from, to] = tickets[i]
            const located = stopover[stopover.length - 1] // 현재 위치
            
            if (visited[i] || located !== from) {
                continue
            }
            visited[i] = true
            stopover.push(to)
            dfs(visited, stopover, paths)
            visited[i] = false
            stopover.pop()
            
        }    
        
        return paths
    }
    
    
    dfs(visited, [startAirport], paths)
    return paths.sort((a, b) => a.toString().localeCompare(b.toString()))[0]
}