const solution = (sizes) => {
    const [hor, ver] = sizes.reduce(([mw, mh], [w, h]) => [Math.max(mw, Math.max(w, h)), Math.max(mh, Math.min(w, h))], [0, 0] )
    return hor * ver
}