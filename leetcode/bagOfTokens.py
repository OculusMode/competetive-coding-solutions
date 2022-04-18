# https://leetcode.com/problems/bag-of-tokens/
class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        score = 0
        # trade
        while True:
            if len(tokens) == 0 or P < min(tokens):
                break
            while len(tokens) > 0 and P >= min(tokens):
                score += 1
                P -= min(tokens)
                # print('trading ', min(tokens))
                tokens.remove(min(tokens))
            if len(tokens) > 1 and score > 0:
                maxToken = max(tokens)
                P += maxToken
                score -= 1
                tokens.remove(maxToken)
            if len(tokens) == 0:
                break
        return score
