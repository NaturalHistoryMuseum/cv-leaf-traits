import numpy as np
import alphashape
from shapely.geometry import LineString


def find_longest_line(contour_x, contour_y):
    # Aim: find the longest line i.e., furthest two points.
    points = np.array([contour_x, contour_y]).T
    max_dist = 0
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            dist = np.linalg.norm(points[i] - points[j])
            if dist > max_dist:
                max_dist = dist
                max_pair = (points[i], points[j])

    X = [max_pair[0][0], max_pair[1][0]]
    Y = [max_pair[0][1], max_pair[1][1]]

    return X, Y

def compute_gradient(line_x,line_y):
    # Aim: compute gradient of line.
    gradient = (line_y[1] - line_y[0]) / (line_x[1] - line_x[0])
    return gradient


def find_perpendicular_slope_and_intercept(line_x, line_y, midpoint_x, midpoint_y):
    # Aim: find gradient and intercept of line going through centroid.
    gradient = compute_gradient(line_x,line_y)
    perp_gradient = -1 / gradient
    intercept = midpoint_y - (perp_gradient * midpoint_x)
    return perp_gradient, intercept


def find_points_on_line(point, gradient, intercept, x_or_y="y"):
    # Aim: Find point on line.
    # x_or_y refers to the point you want, not have.
    if x_or_y == "y":
        # y = mx+c
        return (point * gradient) + intercept
    else:
        # x = (y-c)/m
        return (point - intercept) / gradient
    
def dist_two_points(x1, y1, x2, y2):
    # Aim: Compute distance between two points in R2.
    d = np.sqrt(((y2 - y1) ** 2) + ((x2 - x1) ** 2))
    return d


def find_approximate_perpendicular_line(contours, line, centroid):
    # Aim: Find line perpendicular with main line, and going through centroid.
    m, c = find_perpendicular_slope_and_intercept(
        line[0], line[1], centroid[0], centroid[1]
    )
    minx = min(contours[0])
    maxx = max(contours[0])
    y1 = find_points_on_line(minx, m, c)
    y2 = find_points_on_line(maxx, m, c)
    intersection = alphashape.alphashape(
        np.array([contours[0], contours[1]]).T, 0.0
    ).intersection(LineString([[minx, y1], [maxx, y2]]))
    if intersection.geom_type == "LineString":
        coords = np.asarray([intersection.coords.xy])
    elif intersection.geom_type == "MultiLineString":
        coords = np.asarray([l.coords.xy for l in intersection.geoms])

    return coords[:2][0][0], coords[:2][0][1]


def find_lamina_width_and_leaf_length(contours_x, contours_y, centroid):
    # Aim: Find the lamina width and approximate vein length (i.e. longest line).
    measurements = {}
    # 1) Find longest line:
    length_x, length_y = find_longest_line(contours_x, contours_y)
    measurements["length"] = [length_x, length_y]

    # 2) Find width:
    width_x, width_y = find_approximate_perpendicular_line(
        [contours_x, contours_y], [length_x, length_y], centroid
    )
    measurements["width"] = [width_x, width_y]
    
    return measurements
