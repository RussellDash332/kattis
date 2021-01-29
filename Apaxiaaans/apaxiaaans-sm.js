let line = readline();
let result = line[0];
for (let i = 1; i < line.length; i++) {
    if (result[result.length-1] !== line[i]) {
        result += line[i]
    }
}
console.log(result);