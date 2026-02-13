import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_inequality_type(self):
        node = TextNode("Common Text", TextType.TEXT)
        node2 = TextNode("Common Text", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_inequality_url(self):
        node = TextNode("Common Text", TextType.TEXT)
        node2 = TextNode("Common Text", TextType.TEXT, "http:/example.com")
        self.assertNotEqual(node, node2)

    def test_inequality_text(self):
        node = TextNode("Common Text", TextType.TEXT)
        node2 = TextNode("Text Common", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_equality(self):
        node = TextNode("Common Text", TextType.TEXT)
        node2 = TextNode("Common Text", TextType.TEXT)
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )

if __name__ == "__main__":
    unittest.main()
