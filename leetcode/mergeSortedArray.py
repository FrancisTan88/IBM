class Solution:
    
    # Method1: Naive, append first m elements of nums1 to the new list
    # Time complexity: O(m+n)
    # Space complexity: O(m+n)
    
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        clone_nums1 = []
        for i in range(m):
            clone_nums1.append(nums1[i])
        
        new_list = []
        ind1, ind2 = 0, 0
        while ind1 < m and ind2 < n:
            if clone_nums1[ind1] < nums2[ind2]:
                new_list.append(clone_nums1[ind1])
                ind1 += 1
            else:
                new_list.append(nums2[ind2])
                ind2 += 1
        while ind1 < m:
            new_list.append(clone_nums1[ind1])
            ind1 += 1
        while ind2 < n:
            new_list.append(nums2[ind2])
            ind2 += 1
        
        for i in range(m+n):
            nums1[i] = new_list[i]

    # method2: 
    # Time complexity: O(m+n)
    # Space complexity: O(1)
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ind1, ind2 = m-1, n-1
        total_ind = len(nums1)-1
        while ind1 >= 0 and ind2 >= 0:
            if nums1[ind1] > nums2[ind2]:
                nums1[total_ind] = nums1[ind1]
                ind1 -= 1
            else:
                nums1[total_ind] = nums2[ind2]
                ind2 -= 1
            total_ind -= 1
            
        while ind2 >= 0:
            nums1[total_ind] = nums2[ind2]
            ind2 -= 1
            total_ind -= 1