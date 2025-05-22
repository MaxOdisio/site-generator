from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType


def text_node_to_html_node(text_node):
    match text_node:
        case TextType.TEXT:
            return LeafNode(text_node)
        case TextType.BOLD:
            return LeafNode("b", text_node)
        case TextType.ITALIC:
            return LeafNode("i", text_node)
        case TextType.CODE:
            return LeafNode("code", text_node)
        case TextType.LINK:
            return LeafNode("a", text_node, "href")
        case TextType.IMAGE:
            return LeafNode("img", None, ["src", "alt"])


def main():
    dummy = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(dummy)


main()
