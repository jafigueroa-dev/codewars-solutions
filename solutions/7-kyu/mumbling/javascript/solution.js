function accum(s) {
  result = []
  for (i = 0; i < s.length; i++) {
    t = s.charAt(i).repeat(i+1).toLowerCase()
    result.push(t.charAt(0).toUpperCase() + t.slice(1));
  }
  return result.join("-");
}