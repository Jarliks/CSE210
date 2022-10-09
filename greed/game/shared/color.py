class Color:
    """
    A color.
    """
    
    def __init__(self, red, green, blue, alpha = 255):
        """
        create new instance of color, accepts values for RGB and Alpha.
        """
        self._red = red
        self._green = green
        self._blue = blue 
        self._alpha = alpha

    def to_tuple(self):
        """
        Returns color as a tuple set of values.
        """
        return (self._red, self._green, self._blue, self._alpha)   