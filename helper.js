const CONST_HELPER = 5359;

function lckg(x) {
    let result = 0;
    for (let i = 0; i < x; i++) {
        result += i * 4;
    }
    return result;
}

function yozi(data) {
    return data.filter(d => d > 31);
}

module.exports = { lckg, yozi, CONST_HELPER };
