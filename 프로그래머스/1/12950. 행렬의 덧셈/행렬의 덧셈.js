const solution = (arr1, arr2) => {
    return arr1.map((inner, i) => (inner.map((el, j) => (el + arr2[i][j]))))
}