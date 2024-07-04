int* twoSum(int* nums, int numsSize, int target, int* returnSize) 
{
    int key=0;
    int* index = (int*)malloc(2 * sizeof(int));
    for(int i =0;i<numsSize-1;i++)
    {
        key=0;
        for(int j=i+1;j<numsSize;j++)
        {   key=0;
            if(nums[i]+nums[j]==target)
            {
                index[0]=i;
                index[1]=j;
                *returnSize=2;
                return index;
            }
        }
    }
    *returnSize=0;
    return NULL;
}