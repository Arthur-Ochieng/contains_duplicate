/**
 * @param {number[]} nums
 * @return {boolean}
 */
 var containsDuplicate = function(nums) {
    const newSet = new Set(nums) 
    // Created a new set and assigned all the elements in the nums array to this set

    val = newSet.size !== nums.length;   // Compared the two objects to see if they are equal
    // Sets do not map duplicate elements, so if the two objects are not of the same length it means that there is a duplicate element
    console.log(val);

};
nums = [1,5,4,3]
containsDuplicate(nums)