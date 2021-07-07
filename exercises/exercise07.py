def rectangle_area(length, width):
    area_sqft = length * width
    sqft_sqmt_const = 0.09290304
    area_sqmt = round(area_sqft * sqft_sqmt_const, 3)
    return f"""You entered dimensions of {length} feet by {width} feet.
The area is
{area_sqft} square feet
{area_sqmt} square meters"""


if __name__ == '__main__':
    l = int(input("What is the length of the room in feet?"))
    w = int(input("What is the width of the room in feet?"))
    print(rectangle_area(l, w))
