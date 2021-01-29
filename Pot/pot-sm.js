var n = parseInt(readline());
let result = 0;
for (let i = 0; i < n; i++){
    let x = parseInt(readline());
    result += Math.pow(x/10 >> 0, x%10); // or Math.floor(x/10)
}
console.log(result);