function list(names){
  const a = [];
  names.forEach(function(obj){
    a.push(obj.name);
  })
  const last = a.pop()
  if (names.length == 0) {
    return ''
  } else if (names.length == 1) {
    return last
  } else {
    return a.join(', ') + ' & ' + last
  }
}