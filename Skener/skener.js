let nums = readline().split(" ");
let r = parseInt(nums[0]);
let c = parseInt(nums[1]);
let zr = parseInt(nums[2]);
let zc = parseInt(nums[3]);
for (let i = 0; i < r; i++){
    row = readline();
    zrow = "";
    for (let j = 0; j < c; j++) {
        zrow += row[j].repeat(zc);
    }
    for (let k = 0; k < zr; k++) {
        console.log(zrow);
    }
}