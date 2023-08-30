class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        import itertools
        matrix = (list(itertools.chain.from_iterable(matrix)))
        if target in matrix:
            return True
        else:
            return False
