import unittest
from src.string_decoder import decode_string

class TestStringDecoder(unittest.TestCase):
    def test_given_examples(self):
        self.assertEqual(decode_string("3[a]2[bc]"), "aaabcbc")
        self.assertEqual(decode_string("3[a2[c]]"), "accaccacc")
        self.assertEqual(decode_string("2[abc]3[cd]ef"), "abcabccdcdcdef")
        self.assertEqual(decode_string("abc3[cd]xyz"), "abccdcdcdxyz")

    def test_edge_cases(self):
        self.assertEqual(decode_string(""), "")
        self.assertEqual(decode_string("abc"), "abc")
        self.assertEqual(decode_string("10[a]"), "aaaaaaaaaa")
        self.assertEqual(decode_string("2[3[a]b]"), "aaabaaab")
        self.assertEqual(decode_string("3[a]2[b4[c]]"), "aaabccccbcccc")
        self.assertEqual(decode_string("100[leetcode]"), "leetcode" * 100)
        self.assertEqual(decode_string("3[a]2[b]1[c]"), "aaabbc")
        self.assertEqual(decode_string("1[a]"), "a")
        self.assertEqual(decode_string("2[]"), "")
        self.assertEqual(decode_string("0[abc]"), "")
if __name__ == '__main__':
    unittest.main()
