from collections import Counter


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        ransom_note_hash = Counter(ransomNote)
        magazine_hash = Counter(magazine)

        for char, needed in ransom_note_hash.items():
            if magazine_hash[char] < needed:
                return False

        return True