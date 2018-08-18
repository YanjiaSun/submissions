public class Solution
{
    public String addStrings(String num1, String num2)
    {
        int i = num1.length() - 1, j = num2.length() - 1, carry = 0;
        String result = "";

        while (i >= 0 || j >= 0)
        {
            if (i >= 0)
            {
                carry += num1.charAt(i) - '0';
            }

            if (j >= 0)
            {
                carry += num2.charAt(j) - '0';
            }

            result = Integer.toString(carry % 10) + result;
            carry /= 10;
            i--;
            j--;
        }

        return carry != 0 ? "1" + result : result;
    }
}
