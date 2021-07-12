import math

def paint_calculator(length:int, width:int) -> int:
    area = length * width
    paint = math.ceil(area/350)
    return f"""You will need to purchase {paint} gallons of
paint to cover {area} square feet."""

if __name__ == '__main__':
    length = int(input("Please enter the length of the room."))
    width = int(input("Please enter the width of the room."))
    print(paint_calculator(length, width))
