const solution = (arr1, arr2) => {
    return Array.from(arr1, (inner, i) => {
        return Array.from(inner, (el, j) => (el + arr2[i][j])
        )
    })
}