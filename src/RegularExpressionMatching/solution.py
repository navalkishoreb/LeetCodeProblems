class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        pattern_index = 0
        index = 0
        while index < len(s) and pattern_index < len(p):
            char = s[index]
            pattern_char = p[pattern_index]
            if pattern_char == ".":
                pattern_index = pattern_index + 1
                index = index + 1
            elif pattern_char == "*":
                matching_char = "." if pattern_index == 0 else p[pattern_index - 1]
                exit_loop = False
                while index < len(s) and not exit_loop:
                    if matching_char == ".":
                        index = index + 1
                    elif matching_char == char:
                        index = index + 1
                    else:
                        pattern_index = pattern_index + 1
                        index = index + 1
                        exit_loop = True
            elif pattern_char != char:
                return False
            else:
                pattern_index = pattern_index + 1
                index = index + 1
        
        return index == len(s)
