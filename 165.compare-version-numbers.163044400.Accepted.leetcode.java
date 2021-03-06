public class Solution
{
    public int compareVersion(String version1, String version2)
    {
        String[] ver1 = version1.split("\\.");
        String[] ver2 = version2.split("\\.");

        for (int index = 0; index < ver1.length || index < ver2.length; index++)
        {
            int num1 = index < ver1.length ? Integer.parseInt(ver1[index]) : 0;
            int num2 = index < ver2.length ? Integer.parseInt(ver2[index]) : 0;

            if (num1 < num2)
            {
                return -1;
            }
            else if (num1 > num2)
            {
                return 1;
            }
        }

        return 0;
    }
}

