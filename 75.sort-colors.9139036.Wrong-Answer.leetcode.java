public class Solution
{
    public void sortColors(int[] A)
    {
        if (A == null)
        {
            return;
        }

        int redIndex = 0; // points to the first one that may be not red
        int blueIndex = A.length - 1; // points to the first one that may be not
        // blue
        int index = 0;

        while (index <= blueIndex)
        {
            if (A[index] == 0)
            {
                swap(A, index, redIndex);
                redIndex++;
                index++; // cannot be less than redIndex
            }
            else if (A[index] == 2)
            {
                swap(A, index, blueIndex);
                blueIndex--;
            }
            else
            {
                index++;
            }
        }
    }

    private void swap(int[] a, int index, int blueIndex)
    {
        a[index] ^= a[blueIndex];
        a[blueIndex] ^= a[index];
        a[index] ^= a[blueIndex];
    }
}
