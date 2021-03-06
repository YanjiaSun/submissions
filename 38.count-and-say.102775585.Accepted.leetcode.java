public class Solution
{
    public String countAndSay(int n)
    {
        String str = "1";
        int count = 1;

        for (int i = 1; i < n; i++)
        {
            StringBuilder sb = new StringBuilder();

            for (int nav = 0; nav < str.length(); nav++)
            {
                if (nav + 1 < str.length() && str.charAt(nav) == str.charAt(nav + 1))
                {
                    count++;
                }
                else
                {
                    sb.append("" + count).append(str.charAt(nav));
                    count = 1;
                }
            }

            str = sb.toString();
        }

        return str;
    }
}   
