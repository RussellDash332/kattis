var w = parseInt(readline());
var n = parseInt(readline());
var area = 0;
for (let i = 0; i < n; i++) {
    let nums = readline().split(" ");
    let a = parseInt(nums[0]);
    let b = parseInt(nums[1]);
    area += a*b;
}
console.log(area/w >> 0);