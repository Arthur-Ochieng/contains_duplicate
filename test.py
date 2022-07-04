#Function to check if a duplicate element exists in a list
# The function returns a yes if the element exists or a no if it does not

def containsDuplicate(nums: list[int]) -> bool:

    new_set = set() #initiate an empty set or a hashmap

    for i in nums:  #map every element in the list to the set
        if i in new_set:   # check if the element already exists in the set before adding it
            print("YES")
            return True
          
        new_set.add(i)  # Add the element if it was previously non existent
    print("NO")
    return False

containsDuplicate([1,2,3,4])
        