var w = parseInt(readline());
var n = parseInt(readline());
var area = 0;
for (let i = 0; i < n; i++) {
    let nums = readline().split(" ");
    area += parseInt(nums[0])*parseInt(nums[1]);
}
console.log(area/w >> 0);