class Solution(object):
    def separateSquares(self, squares):
        """
        :type squares: List[List[int]]
        :rtype: float
        """
        if not squares:
            return 0.0
        
        # Compute total area (with multiplicity — overlaps count multiple times)
        total_area = 0.0
        for _, _, side in squares:
            total_area += side * side
        
        target = total_area / 2.0
        
        # Binary search on the y-coordinate
        left = 0.0
        right = 2 * 10**9 + 10     # safe upper bound (y_i <= 1e9, side <= 1e9)
        
        # Run enough iterations for precision better than 1e-9
        for _ in range(80):
            mid = (left + right) / 2
            
            # Compute area strictly below y = mid
            area_below = 0.0
            for _, y, side in squares:
                if mid <= y:
                    # square completely above
                    continue
                top = y + side
                if mid >= top:
                    # square completely below
                    area_below += side * side
                else:
                    # partial — trapezoid below (but since uniform width, just height × side)
                    height_below = mid - y
                    area_below += height_below * side
            
            if area_below >= target:
                right = mid
            else:
                left = mid
        
        return left