#include <iostream>
#include <cmath>

long int findNextSquare(long int sq) {
  int num = sqrt(sq) + 1;
  float a = sqrt(sq);
  if (int(a) != a) {
    return -1;
  }
  return pow(num, 2);
}