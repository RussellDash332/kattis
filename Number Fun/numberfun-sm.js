var q = parseInt(readline());
for (let i = 0; i < q; i++) {
    let nums = readline().split(" ");
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
}