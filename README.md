# Leaf Trait Extraction

We employ [Leaf Machine 2](https://github.com/NaturalHistoryMuseum/LeafMachine2) to extract outlines of leaves and leaflets from Herbarium sheets.

We note that we are using an older version of [Leaf Machine 2](https://github.com/NaturalHistoryMuseum/LeafMachine2), with slightly modified and additional files, compared to the [original](https://github.com/Gene-Weaver/LeafMachine2). This version is uses Python 3.95 and Pytorch 1.11. Please follow the instructions in the repository to install Leafmachine correctly.

Our aim is to use LeafMachine to extract measurements and outlines of leaves and leaflets from herbarium sheets. The maasurements include:
- Length (Longest line on leaf/leaflet outline).
- Width (This can be described with shortest paths with additional criteria such as perpendicular to the Length, or intersection with centroid, as described by our functions).
- Area (The area of the leaf/leaflet, assumed by the area within the boundary created by the outline contour).
- Perimeter (Computed as the total length of the contour around leaf/leaflet).
