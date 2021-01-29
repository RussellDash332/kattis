let nums = readline().split(" ");
let x1 = parseInt(nums[0]);
let y1 = parseInt(nums[1]);

let nums2 = readline().split(" ");
let x2 = parseInt(nums2[0]);
let y2 = parseInt(nums2[1]);

let t = parseInt(readline());
let check = Math.abs(x2-x1)+Math.abs(y2-y1)-t;
console.log((check > 0 || check % 2 == 1 || check % 2 == -1) ? "N" : "Y");