
from lark import Lark


class TreeFactory:

    _GRAMMAR = """
    start: "(" NODE subtree* ")"
    subtree: "(" NODE subtree* ")" | "()"
    NODE: NUMBER
    %ignore " "
    %import common.NUMBER
    """
    _PARSER = Lark(_GRAMMAR, debug=True)

    @classmethod
    def create(cls, str):
        """Return a Tree implementation based on the provided string represenstation.
            e.g. 
                     1
                    / \
                   2   None
                  / \         === ' (1 (2 (3 (4)) (5)) ()) '
                 3   5
                /
               4
        """
        raise NotImplementedError('must be implemented by subclass')