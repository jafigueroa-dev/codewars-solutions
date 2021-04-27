function sortArray(arr) {
  const odd = [];
  const even = [];
  const zeroPos = [];
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] == 0) {
      zeroPos.push(i);
      even.push(arr[i]);
    } else if (arr[i] % 2 != 0) {
      odd.push(arr[i]);
      even.push(0);
    } else {
      even.push(arr[i]);
    }
  }
  odd.sort((a, b) => a - b);
  let count = 0;
  for (let i = 0; i < even.length; i++) {
    if (!zeroPos.includes(i) && even[i] == 0) {
      even[i] = odd[count]
      count++
    }
  }
  return even
}