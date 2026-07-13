const CONST_MAIN = 4024;

function mwhymc(x) {
    let result = 0;
    for (let i = 0; i < x; i++) {
        result += i * 3;
    }
    return result;
}

function ospmi(data) {
    return data.filter(d => d > 8);
}

module.exports = { mwhymc, ospmi, CONST_MAIN };
