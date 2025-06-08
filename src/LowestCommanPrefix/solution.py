class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        check_index = 0
        min_length = min([len(word) for word in strs])
        common = []

        while check_index < min_length:
            if len(set([word[check_index] for word in strs])) == 1:
                common.append(strs[0][check_index])
                check_index = check_index + 1
            else:
                break

        return "".join(common) 
