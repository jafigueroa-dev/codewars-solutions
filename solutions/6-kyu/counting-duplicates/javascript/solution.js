function duplicateCount(text){
  arr = text.toLowerCase().split('');
  countMap = {};
  count = 0
  for ( i = 0; i < text.length; i++ ) {
    countMap[arr[i]] = ++countMap[arr[i]] || 1;
  }
  for ( var key in countMap ){
    if (countMap[key] > 1) {
      count++
    }
  }
  return count
}