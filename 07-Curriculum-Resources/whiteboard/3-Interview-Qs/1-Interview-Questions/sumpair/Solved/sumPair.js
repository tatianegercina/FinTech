function sumPair(input, sum) {
  for(let i = 0, e = input.length - 1; i < e; ) {
    if(i >= e) return null;
    let sumTest = input[i] + input[e];
    if(sumTest === sum) {
      return [input[i], input[e]];
      break;
    }
    if(sumTest < sum) i++;
    else if(sumTest > sum) e--;
  }
}

function sumPairs(input, sum) {
  let result = [];
  for(let i = 0, e = input.length; i < e; i++) {
    for(let j = i + 1; j < e ; j++) {
      if(input[i] + input[j] == sum) {
        result.push([input[i], input[j]]);
        e = j;
      }
    }
  }
  return result;
}

console.log('first match:', sumPair([1,2,3,4,5,6], 8));

console.log('all matches:', sumPairs([1,2,3,4,5,6], 8));
