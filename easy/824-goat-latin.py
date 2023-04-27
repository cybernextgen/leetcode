import unittest

data = (
    ("I speak Goat Latin", "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"),
    (
        "The quick brown fox jumped over the lazy dog",
        "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa",
    ),
    (
        "Each word consists of lowercase and uppercase letters only",
        "Eachmaa ordwmaaa onsistscmaaaa ofmaaaaa owercaselmaaaaaa andmaaaaaaa uppercasemaaaaaaaa etterslmaaaaaaaaa onlymaaaaaaaaaa",
    ),
)


class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        new_words = []
        for index, word in enumerate(sentence.split()):
            if word[0] not in vowels:
                word = word[1:] + word[0]
            word = word + "ma" + ("a" * (index + 1))
            new_words.append(word)
        return " ".join(new_words)


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertEqual(s.toGoatLatin(input_data), expected)


if __name__ == "__main__":
    unittest.main()
