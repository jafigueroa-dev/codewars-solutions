function towerBuilder(nFloors) {
  let tower = [];
  let descend = nFloors * 2 - 1;
  for (i = 0; i < nFloors; i++) {
    tower.push(" ".repeat(i) + "*".repeat(descend) + " ".repeat(i));
    descend = descend - 2;
  }
  return tower.reverse();
}