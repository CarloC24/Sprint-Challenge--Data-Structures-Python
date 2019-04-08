Add your answers to the questions below.

1. What is the runtime complexity of your ring buffer's `append` method?
   0(1) it just checks if we are going over our capacity and appends on the proper position.

2. What is the space complexity of your ring buffer's `append` function?

0(1) I am using memory that is explicitly defined for my operations. So the Space Complexity of my Append Method is Constant

3. What is the runtime complexity of your ring buffer's `get` method?
   0(n) Because I am making a list comprehension that loops on the self.storage to not include None's

4. What is the space complexity of your ring buffer's `get` method?

0(1) Because im only using one space in memory and that is to store my List Comprehension that im returning.

5. What is the runtime complexity of the provided code in `names.py`?
   0(n^2) because we have a for loop inside of a for loop so n \* n is n^2 hence the big O of 0(n^2)

6. What is the space complexity of the provided code in `names.py`?
   0(1) because we only have the duplicates array
   So the Space Complexity is Constant

7. What is the runtime complexity of your optimized code in `names.py`?
   0(n) Because we are checking with our LRU Cache (Least Recently Used) if the following value exist. If not add it if it does Append it.

8. What is the space complexity of your optimized code in `names.py`?

0(2). Linear Time I removed duplicates in names_1 and names_2 and added both and stored in the variable namesset. Then the duplicates array.
1 + 1 = 0(2)
