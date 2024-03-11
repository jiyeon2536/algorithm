function solution(maps) {
    let answer = 0;
    
    const di = [0, 0, 1, -1]
    const dj = [1, -1, 0, 0]
    
    const n = maps.length
    const m = maps[0].length
    
    let visited = Array.from({length: n},() => {
        return new Array(m).fill(0)
    })
        
    function bfs(sti, stj) {
        let queue = [[sti, stj]]
        visited[sti][stj] = 1
        while (queue.length > 0) {
            const tmp = queue.shift()
            const r = tmp[0]
            const c = tmp[1]
            for (let i = 0; i < 4; i++) {
                const nr = r + di[i]
                const nc = c + dj[i]
                if (0 <= nr && nr < n && 0 <= nc && nc < m && maps[nr][nc] === 1 && visited[nr][nc] === 0) {
                    visited[nr][nc] = visited[r][c] + 1
                    queue.push([nr, nc])
                }
            }
        }            
    }
    
    bfs(0, 0)
    if (visited[n-1][m-1] === 0) return -1
    answer = visited[n-1][m-1]
    return answer;
}