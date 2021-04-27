function solution(s, e){
  return e == '' ? true : s.slice(-e.length) == e ? true : false;
}