const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let previousLine = "";
let result = 0;
  
rl.on("line", (line) => {
    if (!previousLine) {
        let n = line;
        previousLine = line;
    } else {
        let x = parseInt(line);
        result += Math.pow(x/10 >> 0, x%10);
        previousLine = line;
    }
});

rl.on("close", function() {
    console.log(result);
});