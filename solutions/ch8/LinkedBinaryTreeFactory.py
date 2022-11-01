from TreeFactory import TreeFactory
from LinkedBinaryTree import LinkedBinaryTree

from lark import Discard, Transformer

class LinkedBinaryTreeFactory(TreeFactory):
    
    class _Transfomer(Transformer):
        def __default__(self, data, children, meta):
            if len(children) == 0:  # Empty node
                return Discard
            if len(children) == 1:  # Leaf
                return LinkedBinaryTree(children[0].value)
            else:
                t = LinkedBinaryTree(children[0].value)
                for child in children[1:]:
                    t.attach(child)
                return t

    @classmethod
    def create(cls, str):
        parse_tree = cls._PARSER.parse(str)
        tree = cls._Transfomer().transform(parse_tree)
        return tree