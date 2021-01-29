let name = readline().split('-');
let result = '';
for (let i = 0; i < name.length; i++) {
    result += name[i][0];
}
console.log(result);