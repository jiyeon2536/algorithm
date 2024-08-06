const solution = (t, p) => {
    let st = 0;
    let end = p.length;
    let result = 0;
    
    while (end <= t.length) {
        if (parseInt(t.slice(st, end)) <= parseInt(p)) result ++;
        st ++;
        end ++;
    }
    return result
}