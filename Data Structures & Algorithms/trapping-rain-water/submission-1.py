class Solution:
    def trap(self, height: List[int]) -> int:
        # maior elemento a esquerda
        # Maior elemento a direita
        # left
        # right
        # se left > maior a esquerda, altera
        # se right > maior a direita, altera

        # Para cada índice, tirar o min entre os maiores
        # Fazer o cálculo y - heigh[i]

        left = 0
        right = len(height) -1
        max_left = left
        max_right = right

        result = 0
        while left < right:
            if height[left] > height[max_left]:
                max_left = left
            if height[right] > height[max_right]:
                max_right = right

            if height[max_left] < height[max_right]:
                result += max(height[max_left] - height[left], 0)
                left += 1
            else:
                result += max(height[max_right] - height[right], 0)
                right -= 1

        return result
