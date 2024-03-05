import tkinter as tk
import math
canva_width = 800
canva_height = 800
colour0 = '#CD5334'
colour1 = '#4B7A84'
colour2 = '#E8C547'

class DraggablePoint:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.circle = canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill=colour0, tags='draggable')
        self.canvas.tag_bind(self.circle, '<ButtonPress-1>', self.on_press)
        self.canvas.tag_bind(self.circle, '<B1-Motion>', self.on_drag)
        self.canvas.tag_bind(self.circle, '<ButtonRelease-1>', self.on_release)
        self.x = x
        self.y = y

    def on_press(self, event):
        self.start_x = event.x
        self.start_y = event.y

    def on_drag(self, event):
        dx = event.x - self.start_x
        dy = event.y - self.start_y
        self.canvas.move(self.circle, dx, dy)
        self.x += dx
        self.y += dy
        self.start_x = event.x
        self.start_y = event.y
        self.update_points()
        self.canvas.tag_raise('draggable')

    def on_release(self, event):
        self.update_points()
        self.canvas.tag_raise('draggable')

    def update_points(self):
        quad31_x_diff = point3.x - point1.x
        quad24_x_diff = point2.x - point4.x

        quad31_y_diff = point3.y - point1.y
        quad24_y_diff = point2.y - point4.y

        quad_size_x = min(map(abs, [quad31_x_diff, quad24_x_diff])) + 5
        quad_size_y = min(map(abs, [quad31_y_diff, quad24_y_diff])) + 5

        # make sure the dots span the whole canvas
        diagonal = math.sqrt(canva_width ** 2 + canva_height ** 2) / 2
        max_dots_x = math.ceil(diagonal / quad_size_x) + 1
        max_dots_y = math.ceil(diagonal / quad_size_y) + 1

        self.canvas.delete('fixed')

        for i in range(- max_dots_x, max_dots_x):
            for j in range(- max_dots_y, max_dots_y):
                PointA = Point1(canvas, point1.x - i * quad31_x_diff + j * quad24_x_diff,
                                point1.y - i * quad31_y_diff + j * quad24_y_diff)
                Quad1(canvas, PointA, point1, point2, point3, point4)
                PointB = Point2(canvas, point2.x - i * quad31_x_diff + j * quad24_x_diff,
                                point2.y - i * quad31_y_diff + j * quad24_y_diff)
                Quad2(canvas, PointB, point1, point2, point3, point4)


class Point1:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        # self.circle = canvas.create_oval(x - 3, y - 3, x + 3, y + 3, fill=colour1, tags='fixed')
        self.x = x
        self.y = y

class Quad1:
    def __init__(self, canvas, Point, p1, p2, p3, p4):
        self.canvas = canvas
        quad12_y_diff = p2.y - p1.y
        quad13_y_diff = p3.y - p1.y
        quad14_y_diff = p4.y - p1.y

        quad12_x_diff = p2.x - p1.x
        quad13_x_diff = p3.x - p1.x
        quad14_x_diff = p4.x - p1.x
        self.quad = canvas.create_polygon(Point.x, Point.y,
                                            Point.x + quad12_x_diff, Point.y + quad12_y_diff,
                                            Point.x + quad13_x_diff, Point.y + quad13_y_diff,
                                            Point.x + quad14_x_diff, Point.y + quad14_y_diff,
                                            fill=colour1, tags='fixed')
class Point2:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        # self.circle = canvas.create_oval(x - 3, y - 3, x + 3, y + 3, fill=colour2, tags='fixed')
        self.x = x
        self.y = y

class Quad2:
    def __init__(self, canvas, Point, p1, p2, p3, p4):
        self.canvas = canvas
        quad12_y_diff = p2.y - p1.y
        quad13_y_diff = p3.y - p1.y
        quad14_y_diff = p4.y - p1.y

        quad12_x_diff = p2.x - p1.x
        quad13_x_diff = p3.x - p1.x
        quad14_x_diff = p4.x - p1.x
        self.quad = canvas.create_polygon(Point.x, Point.y,
                                            Point.x - quad12_x_diff, Point.y - quad12_y_diff,
                                            Point.x - quad13_x_diff, Point.y - quad13_y_diff,
                                            Point.x - quad14_x_diff, Point.y - quad14_y_diff,
                                            fill=colour2, tags='fixed')

root = tk.Tk()
root.title("Draggable Points")

# Create a canvas to draw on
canvas = tk.Canvas(root, width=canva_width, height=canva_height)
canvas.pack()

# Create four draggable points
point1 = DraggablePoint(canvas, 480, 525)
point2 = DraggablePoint(canvas, 400, 420)
point3 = DraggablePoint(canvas, 420, 350)
point4 = DraggablePoint(canvas, 520, 315)

quad12_y_diff = point2.y - point1.y
quad31_y_diff = point3.y - point1.y
quad14_y_diff = point4.y - point1.y
quad24_y_diff = point2.y - point4.y

quad12_x_diff = point2.x - point1.x
quad31_x_diff = point3.x - point1.x
quad14_x_diff = point4.x - point1.x
quad24_x_diff = point2.x - point4.x

# make sure all the dots span the canvas
quad_size_x = min(map(abs, [quad31_x_diff, quad24_x_diff])) + 5
quad_size_y = min(map(abs, [quad31_y_diff, quad24_y_diff])) + 5

# make sure the dots span the whole canvas
diagonal = math.sqrt(canva_width ** 2 + canva_height ** 2) / 2
max_dots_x = math.ceil(diagonal / quad_size_x)
max_dots_y = math.ceil(diagonal / quad_size_y)


#initial dots
for i in range(- max_dots_x, max_dots_x):
    for j in range(- max_dots_y, max_dots_y):
        PointA = Point1(canvas, point1.x - i * quad31_x_diff + j * quad24_x_diff,
                        point1.y - i * quad31_y_diff + j * quad24_y_diff)
        Quad1(canvas, PointA, point1, point2, point3, point4)
        PointB = Point2(canvas, point2.x - i * quad31_x_diff + j * quad24_x_diff,
                        point2.y - i * quad31_y_diff + j * quad24_y_diff)
        Quad2(canvas, PointB, point1, point2, point3, point4)


# initial quad



'''
# Create initial polygon
points = [
    (point1.x, point1.y),
    (point2.x, point2.y),
    (point3.x, point3.y),
    (point4.x, point4.y)
]
'''

# canvas.create_polygon(points, fill='blue', outline='blue', width=2, tags='quadrilateral')


#Raise the dots to the first layer
canvas.tag_raise('draggable')


# Start the Tkinter event loop
root.mainloop()