function expandedForm(num) {
  const len = num.toString().length;
  let pos = 0;
  let arr = [];
  for (i = len; i > 0; i--) {
    let digit = (num + '').charAt(pos);
    if (digit == 0) {
      pos++;
      continue;
    }
    pos++;
    arr.push(digit.padEnd(i, '0'));
  }
  return arr.join(' + ');
}