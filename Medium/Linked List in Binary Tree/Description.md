## Challenge 1367. Linked List in Binary Tree


**Problem:** Given a binary tree root and a linked list with head as the first node. Return True if all the elements in the linked list 
starting from the head correspond to some downward path connected in the binary tree otherwise return False. In this context, a downward path
starts at some node and goes downwards.

 ## Examples

**Example 1:**

- **Input:** `head = [4,2,8]`, `root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]`
- **Output:** `true`
- **Explanation:** root = [1,4,**4**,null,2,**2**,null,1,null,6,**8**,null,null,null,null,1,3]
  - The numbers in **bold** represent the downward path 

**Example 2:**

- **Input:** `head = [1,4,2,6]`, `root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]`
- **Output:** `true`
  
**Example 3:**

- **Input:** `head = [1,4,2,6,8]`, `root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]`
- **Output:** `false`
- **Explanation:** No path in the binary tree contains all the linked list elements from head.

## Constraints:

- The number of nodes in the tree will be in the range [1, 2500].
- The number of nodes in the list will be in the range [1, 100].
- `1 <= Node.val <= 100` for each node in the linked list and binary tree.

## Approach 


1. **Recursive Depth-First Search (DFS):**
- The problem requires checking for any downward path in the tree, so a recursive DFS algorithm is used:
    - Start from any node in the binary tree, and for each node, check if the linked list's current node value matches the tree node's value.
    - If there is a match, move to the next node in the linked list and the left or right child of the current tree node.
    - If the end of the linked list is reached, return True.
    - If the values don't match or the tree node is null, return False and backtrack to try other paths.

2. **Tree Traversal:**
- Traverse the binary tree, checking for potential matches starting from every node.
- Each time a node's value matches the linked list's head, begin a recursive check to verify if the entire linked list can be matched by
  moving downward.

3. **Edge Cases:**
- If the tree is empty, return False.
- If the linked list is empty, return True (an empty list trivially exists in any tree).
- Ensure the recursion handles all possible subtrees to find potential starting points for the linked list.
- This approach ensures that the solution checks every possible starting point in the tree, and the recursive checking ensures that the linked list elements are consecutively matched.

### Complexity 

1. **Time Complexity:** O(N*M)
   - `N` is the number of nodes in the binary tree and `M` is the nodes in the linked list.
   - In the worst case, may need to visit every node in the binary tree to check if the linked list starts from that node. This takes O(N) time.
   - For each node in the binary tree, must then perform a comparison with the linked list, which might take up to M comparisons (if all elements match).
   - Therefore, in the worst case, the time complexity is O(N * M).
3. **Space Complexity:** O(N)
   - The space complexity is primarily determined by the recursion depth, which corresponds to the height of the binary tree.
   - In the worst case, the binary tree might be a skewed tree (like a linked list), where the recursion depth is N, the number of nodes in the tree.
   - The linked list comparison doesn't add to the space complexity since it's done inline during recursion, and no additional structures are stored.
   - Thus, the space complexity is O(N) due to the recursive stack from traversing the tree.
