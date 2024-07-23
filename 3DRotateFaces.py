import turtle
from math import sin, cos

window = turtle.Screen()
window.setup(600, 600)
window.tracer(0) # Disable animations of turtle
window.bgcolor("black") # window colour

def rotate(x, y, r):
    s, c = sin(r), cos(r)
    return x * c - y * s, x * s + y * c

class Shape:
    def __init__(self, x=True, y=True, z=True, colour="lightblue",border="black",size = 800):
        self.counter = 0
        self.t = turtle.Turtle()
        self.t.ht()
        self.t.color(border)
        self.t.fillcolor(colour)
        self.Rx = x
        self.Ry = y
        self.Rz = z
        self.Size = size

    def draw(self):
        faces_with_depth = []
        
        for edge in self.Faces:
            points = []
            center_z = 0

            for vertex in edge:
                x, y, z = self.VERTICES[vertex]

                if self.Ry:
                    x, z = rotate(x, z, self.counter)  # Only this one to rotate around y
                if self.Rx:
                    y, z = rotate(y, z, self.counter)  # Only this for x
                if self.Rz:
                    x, y = rotate(x, y, self.counter)  # This for z

                z += 5
                center_z += z / len(edge)  # Average z-coordinate for this face

                f = self.Size / z  # f gives size/distance
                sx, sy = x * f, y * f
                points.append((sx, sy))

            faces_with_depth.append((center_z, points))

        # Sort faces based on average z-coordinate
        faces_with_depth.sort(reverse=True)

        for _, points in faces_with_depth:
            self.t.up()
            self.t.begin_fill()
            self.t.goto(points[0])
            self.t.down()
            for point in points[1:]:
                self.t.goto(point)
            self.t.goto(points[0])
            self.t.end_fill()

class Pyramid(Shape):
    Faces = ((0, 1, 2), (2, 3, 0), (0, 1, 4), (1, 2, 4), (2, 3, 4), (3, 0, 4))
    VERTICES = [(-1, -1, -1), (-1, -1, 1), (1, -1, 1), (1, -1, -1), (0, 1, 0)]
class Cube(Shape):
    Faces = (0,1,2),(0,2,3),(0,4,5),(0,1,5),(1,5,6),(1,2,6),(2,3,7),(2,6,7),(0,3,7),(0,4,7),(4,5,6),(4,6,7)
    VERTICES = [(-1, -1, -1), (1, -1, -1), (1, 1, -1), (-1, 1, -1), (-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1)]
class IcoSphere(Shape):
    Faces = (0,1,2),(0,2,3),(0,3,4),(0,4,5),(0,5,1),(1,6,7),(2,7,10),(3,10,9),(4,9,11),(5,11,6),(1,2,7),(2,3,10),(3,4,9),(4,5,8),(5,1,6),(6,7,12),(7,10,12),(10,9,12),(9,11,12),(11,6,12)
    VERTICES = [(0, 1, 0),
                (-0.7236, 0.447215, 0.52572),
                (0.276385, 0.447215, 0.85064),
                (0.894425, 0.447215, 0),
                (0.276385, 0.447215, -0.85064),
                (-0.7236, 0.447215, -0.52572),
                (-0.894425, -0.447215, 0),
                (-0.276385, -0.447215, 0.85064),
                (-0.276385, -0.447215, -0.85064),
                (0.7236, -0.447215, -0.52572),
                (0.7236, -0.447215, 0.52572),
                (-0.276385, -0.447215, -0.85064),
                (0, -1, 0)
                ]

shapes=[]
###################################################
```
Shape properties:
X   \
Y   |  Bool foe rotation axis ( default is true)
Z   /

colour : the colour of the Faces of the shape ( default is lightblue)
border : the colour if the edges of the faces (default is black)
size   : size of Shape (default is 800)

```
shapes.append(IcoSphere(border="black",colour="red"))
window.bgcolor("black") # background window colour
rotateSpeed = 1/1000
######################################################
while True:
    for i in shapes:
        i.t.clear()
        i.draw()
        window.update()
        i.counter += rotateSpeed