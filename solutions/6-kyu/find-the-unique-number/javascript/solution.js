function findUniq(arr) {
  countMap = {};

  for ( i = 0; i < arr.length; i++ ) {
    countMap[arr[i]] = ++countMap[arr[i]] || 1;
  }
  for ( var key in countMap ){
    if (countMap[key] == 1) {
      return parseFloat(key);
    }
  }
}
