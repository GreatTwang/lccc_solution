class Solution {
  public List<String> fizzBuzz(int n) {
    List<String> ans = new ArrayList<String>();
      
    for (int num = 1; num <= n; num++) {
      String numAnsStr = "";
      if (num % 3 == 0) {
        numAnsStr += "Fizz";
      }
      if (num % 5 == 0) {
        numAnsStr += "Buzz";
      }
      if (numAnsStr.equals("")) {
        // Not divisible by 3 or 5, add the number
        numAnsStr += Integer.toString(num);
      }
      ans.add(numAnsStr);
    }
    return ans;
  }
}