import unittest

from main import text_node_to_html_node
from textnode import TextNode, TextType


def test_text_not_eq(self):
    node = TextNode("This is a text node", TextType.BOLD)
    node2 = TextNode("This is a different text node", TextType.LINK)
    self.assertNotEqual(node, node2)



if __name__ == "__main__":
    unittest.main()
