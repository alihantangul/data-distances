pass  # YOUR CODE HERE

def manhattan(point1, point2):
    """
    Calculate the Manhattan distance between two points.

    Parameters:
    point1 (tuple): The first point as a tuple of coordinates (x1, y1).
    point2 (tuple): The second point as a tuple of coordinates (x2, y2).

    Returns:
    int: The Manhattan distance between the two points.
    """
    d_x = abs(point2[0] - point1[0])
    d_y = abs(point2[1] - point1[1])
    distance = d_x + d_y

    return distance

def euclidean(a, b):
        d_x = b[0] - a[0]
        d_y = b[1] - a[1]

        distance = (d_x ** 2 + d_y ** 2) ** 0.5
        return distance
