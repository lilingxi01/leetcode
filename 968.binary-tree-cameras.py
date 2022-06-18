#
# @lc app=leetcode id=968 lang=python3
#
# [968] Binary Tree Cameras
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math


class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        def solve_subtree(node: Optional[TreeNode]):
            if not node:
                return 0, math.inf, 0
            left_results = solve_subtree(node.left)
            right_results = solve_subtree(node.right)
            # There are three different states for one node:
            # 0. The node will be covered by the camera of the next level.
            # 1. The node has a camera in place.
            # 2. The node is not covered but all subtrees.
            # In (0), it requires a camera, (1), in the next level.
            # But we do not know which branch has a camera,
            # so we need to take the minimum of the two.
            # In (2), a camera will be needed to place in its parent.
            # So it may be used in (1) of the parent.
            case_0 = min(
                left_results[1] + min(right_results[0:2]),
                right_results[1] + min(left_results[0:2]),
            )
            case_1 = min(left_results) + min(right_results) + 1
            case_2 = left_results[0] + right_results[0]
            return case_0, case_1, case_2
        # In the end, (2) cannot be used because the root is not covered.
        return min(solve_subtree(root)[0:2])
# @lc code=end

