class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        # Escolher entre:
        # Deletar letra 
        # Seguir com ela
        # Max entre eles
        # Caso base, quando acabar a string
        # Para cada char igual, incrementamos em 1
        # Guardar os estados de índices i e j para cada string

        cache = {}
        def dp(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            if i == len(text1) or j == len(text2):
                return 0
            
            if text1[i] == text2[j]:
                res = 1 + dp(i + 1, j + 1)
            else:
                res = max(
                    dp(i + 1, j),
                    dp(i, j + 1)
                )
            cache[(i, j)] = res
            return res
        return dp(0, 0)