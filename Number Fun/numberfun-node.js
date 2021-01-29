const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let previousLine = "";
rl.on("line", (line) => {
    if (!previousLine) {
        let n = line;
        previousLine = line;
    } else {
        let nums = line.split(" ");
        let a = parseInt(nums[0]);
        let b = parseInt(nums[1]);
        let c = parseInt(nums[2]);
        if (a+b==c) {
            console.log("Possible");
        } else if (a-b ==c) {
            console.log("Possible");
        } else if (b-a ==c) {
            console.log("Possible");
        } else if (a*b == c) {
            console.log("Possible");
        } else if (b*c == a) {
            console.log("Possible");
        } else if (a*c == b) {
            console.log("Possible");
        } else {
            console.log("Impossible");
        }
        previousLine = line;
    }
});