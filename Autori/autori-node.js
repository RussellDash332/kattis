const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.on('line', (line) => {
    var name = line.split('-');
    let result = '';
    for (let i = 0; i < name.length; i++) {
        result += name[i][0];
    }
    console.log(result);
});