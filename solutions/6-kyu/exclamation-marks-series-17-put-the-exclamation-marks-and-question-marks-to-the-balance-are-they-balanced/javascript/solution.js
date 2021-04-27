function balance(left,right){
  const counters = [(left.split("?").length - 1) * 3, (left.split("!").length - 1) * 2, (right.split("?").length - 1) * 3, (right.split("!").length - 1) * 2];
  return (counters[0] + counters[1] < counters[2] + counters[3]) ? "Right" : (counters[0] + counters[1] > counters[2] + counters[3]) ? "Left" : "Balance";
}