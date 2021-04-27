using System;
using System.Collections.Generic;

public static class Kata
{
  public static int DescendingOrder(int num)
  {
    string numToString = num.ToString();
    List<int> numList = new List<int>(); 
    for(int i = numToString.Length - 1; i >= 0; i--) {
      numList.Add((int)(numToString[i] - '0'));
    }
    numList.Sort();
    numList.Reverse();
    return Int32.Parse(String.Join("", numList));
  }
}
