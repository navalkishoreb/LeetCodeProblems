class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        cache = {}
        def match(string_index, pattern_index):

            # print(f"{string_index} {pattern_index}")

            if (string_index, pattern_index) in cache:
                # print(f"Found in cache {string_index} {pattern_index}")
                return  cache[(string_index,pattern_index)]

            if pattern_index >= len(p) and string_index >= len(s):
                return True
            
            if pattern_index >= len(p):
                return False


            result = False

            first_match = string_index < len(s) and (p[pattern_index] == '.' or s[string_index] == p[pattern_index])

            if pattern_index + 1 < len(p) and p[pattern_index + 1] == "*":
                result =  match(string_index , pattern_index + 2) or (first_match and match(string_index + 1 , pattern_index))
            elif first_match:
                result = match(string_index+1 , pattern_index+1)

            cache[(string_index,pattern_index )] = result
            return result
            
        return match(0,0)

