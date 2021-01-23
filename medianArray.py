class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        merged = []
        count1 = 0
        count2 = 0
        while count1 < len(nums1) or count2 < len(nums2):
            if count1 < len(nums1) and count2 < len(nums2):
                if nums1[count1] < nums2[count2]:
                    merged.append(nums1[count1])
                    count1 += 1
                elif nums1[count1] > nums2[count2]:
                    merged.append(nums2[count2])
                    count2 += 1
                else:
                    merged.append(nums1[count1])
                    count1 += 1
                    merged.append(nums2[count2])
                    count2 += 1
            elif count1 < len(nums1):
                merged.append(nums1[count1])
                count1 += 1
            elif count2 < len(nums2):
                merged.append(nums2[count2])
                count2 += 1
        #print(merged)
        if len(merged) % 2 == 0:
            midValues = [len(merged)//2-1,len(merged)//2]
        else:
            midValues = [len(merged)//2]
        #print(midValues)
        median = 0
        for i in range(len(midValues)):
            median += merged[midValues[i]]
        if len(midValues) > 0:
            median = median / len(midValues)
        return median