class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i=0
        j=0
        new=[]
        while i<m and j<n:
            if nums1[i]<=nums2[j]:
                new.append(nums1[i])
                i+=1
            else:
                new.append(nums2[j])
                j+=1
        while i<m:
            new.append(nums1[i])
            i+=1
        while j<n:
            new.append(nums2[j])
            j+=1
        for k in range(m+n):
            nums1[k]=new[k]
        return nums1

        
        