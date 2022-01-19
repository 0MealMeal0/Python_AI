nums1, nums2, nums3 = map(int, input("세 정수를 입력하세요.: ").split())

print(nums1, nums2, nums3)

if(nums1 > nums2):

    if(nums1 > nums3):

        if(nums2 > nums3):
            print(nums1, nums2, nums3)
        
        else:
            print(nums1, nums3, nums2)

    else:
        print(nums3, nums1, nums2)

else:

    if(nums2 > nums3):

        if(nums1 > nums3):
            print(nums2, nums1, nums3)
        
        else:
            print(nums2, nums3, nums1)

    else:
        print(nums3, nums2, nums1)