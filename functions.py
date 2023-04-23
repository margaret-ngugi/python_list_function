#Given two lists, write a function to find the common elements between them and return them in a new list.
def common_numbers(list1,list2):
    common = list(set(list1).intersection(set(list2)))
    return common
list1 = [7,2,4,6,7,8]
list2 = [3,6,2,1,9,7]

print (common_numbers(list1,list2))

#Write a function that takes in a list of numbers and returns a new list containing only the prime numbers.
def get_primes(numbers):
    new_list = []
    for num in numbers:
        if num>1:
            for i in range(2,num):
                if (num %i)==0:
                    break
            else:
                new_list.append(num)
    return new_list
numbers=[7,5,9,6,3,1,5,8,12,2,4,10]
prime_numbers=get_primes(numbers) 
print(prime_numbers)                       
   
#Given a list of integers, write a function that returns the smallest element in the list.
def find_smallest(lst):
    return min(lst)

my_list=[2,8,4,6,9,7] 
smallest =find_smallest(my_list) 
print(smallest) 



#Write a program that takes in a list of words and sorts them based on the number of vowels in each word.
def sort_words(words):
    def count_vowels(word):
        return sum(1 for letter in word if letter in'aeiou')
    return sorted(words,key=count_vowels)
words = ["apple","orange","mango","banana","kiwi"]
words_sorted = sort_words(words)
print(words_sorted)    
#Write a function that takes in a list of integers and returns the longest consecutive 
#subsequence of the list. For example, given [1, 2, 3, 5, 6, 7, 8], the function should return [5, 6, 7, 8].
def longest_consecutive_subsequence(nums):
    numsSet = set(nums)
    max_len = 0
    for num in nums:
        if num -1 not in nums:
            curr_num = num
            curr_len = 1
            while curr_num+1 in nums:
                curr_num +=1
                curr_len +=1
            max_len= max(max_len,curr_len)
    return max_len
nums = [1,3,3,4,7,8,2,11,5,6] 
print(longest_consecutive_subsequence(nums))   
