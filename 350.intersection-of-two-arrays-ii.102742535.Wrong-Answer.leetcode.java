public class Solution
{
    public int[] intersect(int[] nums1, int[] nums2)
    {
        Arrays.sort(nums1);
        Arrays.sort(nums2);
        ArrayList<Integer> list = new ArrayList<Integer>();
        int p1 = 0, p2 = 0;

        while (p1 < nums1.length && p2 < nums2.length)
        {
            if (nums1[p1] < nums2[p2])
            {
                p1++;
            }
            else
            {
                list.add(nums1[p1]);
                p1++;
                p2++;
            }
        }

        int[] result = new int[list.size()];
        return result;
    }
}
