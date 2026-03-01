Dear Dr. Parag & Krithika, 

I wrote my code by trying to build out everything myself, and then comparing what I wrote to the examples we did in class. For whatever worked, I kept it the same, and adjusted parts that were broken based on the model. Therefore what I created strays a little bit from how we wrote the BST and DLL in our examples. I had the most difficulty with the BST, especially with the delete and successor methods. 

The explanation of how I wrote my code is included throughout the code as comments. Regarding time complexity, the DLL appears less complex. There are a handful of while loops used to iterate through the DLL, but they aren't nested, so these methods have a linear time complexity -- O(n). While there are several nested conditionals that were needed in the BST, none of them are nested loops. The time complexity of a BST would presumably be less than that of a DLL, since if you are inserting, searching etc an element in the BST, it isn't always the case you have to iterate through every single tree node except in the worst case scenarios. 


~KD