const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let x = 0;
let y = 0;
  
rl.on("line", (line) => {
    if (x==0) {
        x = line;
    } else {
        y = line;
        if (x > 0 && y > 0) {
            console.log(1);
        } else if (y > 0) {
            console.log(2);
        } else if (x > 0) {
            console.log(4);
        } else {
            console.log(3);
        }
    }
});