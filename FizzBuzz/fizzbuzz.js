nums = readline().split(" ")
fizz = parseInt(nums[0]);
buzz = parseInt(nums[1]);
end = parseInt(nums[2]);
for (let i = 1; i <= end; i++) {
    if (i % fizz == 0 && i % buzz == 0) {
console.log("FizzBuzz");
    } else if (i % fizz == 0) {
console.log("Fizz");
    } else if (i % buzz == 0) {
console.log("Buzz");
    } else {
console.log(i);
    }
}