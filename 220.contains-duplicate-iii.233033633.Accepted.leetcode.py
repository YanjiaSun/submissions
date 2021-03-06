from collections import OrderedDict


class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        buckets = {}
        for i, v in enumerate(nums):
            bucketNum, offset = (v // t, 1) if t else (v, 0)
            for idx in xrange(bucketNum - offset, bucketNum + offset + 1):
                if idx in buckets and abs(buckets[idx] - nums[i]) <= t:
                    return True
            buckets[bucketNum] = nums[i]
            if len(buckets) > k:
                del buckets[nums[i - k] // t if t else nums[i - k]]
        return False
