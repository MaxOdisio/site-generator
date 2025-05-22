import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(
            "p",
            "This is a paragraph",
            None,
            {"class": "txt-custom", "id": "myParagraph"},
        )
        node2 = HTMLNode(
            "p",
            "This is a paragraph",
            None,
            {"class": "txt-custom", "id": "myParagraph"},
        )
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = HTMLNode(
            "p",
            "This is a paragraph",
            None,
            {"class": "txt-custom", "id": "myParagraph"},
        )
        node2 = HTMLNode(
            "a",
            "This is an anchor",
            None,
            {"href": "https://www.google.com", "target": "_blank"},
        )
        self.assertNotEqual(node, node2)

    def test_props_is_none(self):
        node = HTMLNode("p", "This is a paragraph", None)
        node2 = HTMLNode("p", "This is a paragraph", None, None)
        self.assertEqual(node, node2)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Hello, world!")
        self.assertEqual(node.to_html(), "<a>Hello, world!</a>")

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )


if __name__ == "__main__":
    unittest.main()
