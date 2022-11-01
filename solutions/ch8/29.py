'''
8.29 Describe, in pseudo-code, an algorithm for computing the number of de-
scendants of each node of a binary tree. The algorithm should be based
on the Euler tour traversal
'''

from EulerTour import EulerTour
from LinkedBinaryTreeFactory import LinkedBinaryTreeFactory

class ComputeDescendants(EulerTour):
  def _hook_postvisit(self, p, d, path, results):
      if self.tree().is_leaf(p):
          print('{} has {} descendants'.format(p.element(), 0))
          return 1
      else:
          print('{} has {} descendants'.format(p.element(), sum(results)))
          return sum(results) + 1

if __name__ == "__main__":
    tree = LinkedBinaryTreeFactory.create("(1 (2 (3 (4)) (5)) ())")
    ComputeDescendants(tree).execute()
