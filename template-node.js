const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
  
rl.on("line", (line) => {
    // code here to be executed on each read line
});

// optional part
rl.on("close", function() {
    // global variable display perhaps?
});