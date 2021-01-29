var n = parseInt(readline());
for (let i = 1; i <= n; i++) {
    let nums = readline().split(" ");
    let k = nums[0];
    let p = parseInt(nums[1]);
    console.log(k+" "+((p*(p+1))/2 >> 0)+" "+(p*p)+" "+(p*(p+1)));
}