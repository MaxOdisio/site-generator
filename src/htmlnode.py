class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        props_str = ""
        if self.props:
            for prop in self.props:
                props_str += f' {prop}="{self.props[prop]}"'
            return props_str[1:]
        return ""

    def __eq__(self, other):
        if isinstance(other, HTMLNode):
            return (
                self.tag == other.tag
                and self.value == other.value
                and self.children == other.children
                and self.props == other.props
            )
        return NotImplemented

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props_to_html()})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not self.value:
            raise ValueError("invalid HTML: no value")
        if not self.tag:
            return self.value
        return f"<{self.tag}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("invalid HTML: no tag")
        if not self.children:
            raise ValueError("invalid HTML: no children")
        children_str = ""
        for child in self.children:
            children_str += child.to_html()
        return f"<{self.tag}>{children_str}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"
