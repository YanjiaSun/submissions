public class Solution
{
    public int numDistinct(String S, String T)
    {
        int[][] dp = new int[S.length() + 1][T.length() + 1];

        for (int i = 1; i <= S.length(); i++)
        {
            for (int j = 1; j <= T.length(); j++)
            {
                if (j == 0)
                {
                    dp[i][j] = 1;
                    continue;
                }

                dp[i][j] = dp[i - 1][j];

                if (S.charAt(i - 1) == T.charAt(j - 1))
                {
                    dp[i][j] += dp[i - 1][j - 1];
                }
            }
        }

        return dp[S.length()][T.length()];
    }
}
