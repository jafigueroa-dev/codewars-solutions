using System.Collections.Generic;
using System.Diagnostics;

public class LineNumbering 
{
    public static List<string> Number(List<string> lines) 
    {
        List<string> result = new List<string>();
        for(int i = 0; i < lines.Count; i++) {
          int j = i + 1;
          result.Add(j.ToString() + ": " + lines[i]);
        }
        return result;
    }
}