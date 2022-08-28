print("""
Welcome to Imaghur!

This project is exploring the importance of color from the perspective of
evolution. By revealing the underlying maths of color, we may be able to
better understand what color is truly useful for, and maybe do some silly
things using color maths.

Usage notes:
more to come in the future!

Working notes:
Choose canvas size as image when processed in illustrator

Input values in square millimeters or pixels, depending on which is easier to work with (data-wise)
- for each of the RGB colors
- for each of the CMYK colors
- around 15 different color inputs

Randomly output shapes for each color that take up exact same area as original color input
- decide shape based on surrounding shapes
- based on volume of color, decide ordering of placed shapes
- make random shapes using color ordering (to the pixel)
- no one shape can overlap another shape
- do this until there are not enough pixels to place one whole color in an area
- then, pick next open area randomly to fill, until color is depleted
- do this for all remaining colors
- QED.
""")
