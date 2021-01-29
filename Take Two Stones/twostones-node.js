const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.on('line', (line) => {
    var num = parseInt(line);
    console.log((num%2==1) ? "Alice" : "Bob");
});