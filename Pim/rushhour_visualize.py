# Problem Set 6:
# Visualization code for simulated robots.
#
# See the problem set for instructions on how to use this code.

import math
import time

from Tkinter import *

class RushhourVisualisation:
    # We moeten het aantal autos weten met de richting en de posities. De originele positie van de
    # auto is altijd het meest richting de basis (dat wil zeggen, rechts boven). De richting is
    # y/v of x/h voor respectievelijk verticaal of horizontaal.
    def __init__(self, width, height, cars, delay = 0.2):
        "Initializes a visualization with the specified parameters."
        # Number of seconds to pause after each frame
        self.delay = delay
        self.max_dim = max(width, height)
        self.width = width
        self.height = height
        self.carsData = cars
        self.carsImage = None

        # Initialize a drawing surface
        self.master = Tk()
        self.w = Canvas(self.master, width=500, height=500)
        self.w.pack()
        self.master.update()

        # Draw a backing and lines
        x1, y1 = self._map_coords(0, 0)
        x2, y2 = self._map_coords(width, height)
        self.w.create_rectangle(x1, y1, x2, y2, fill = "white")

        # Draw gridlines
        for i in range(width + 1):
            x1, y1 = self._map_coords(i, 0)
            x2, y2 = self._map_coords(i, height)
            self.w.create_line(x1, y1, x2, y2)
        for i in range(height + 1):
            x1, y1 = self._map_coords(0, i)
            x2, y2 = self._map_coords(width, i)
            self.w.create_line(x1, y1, x2, y2)

        # Draw some status text
        self.cars = None
        self.text = self.w.create_text(25, 0, anchor=NW,
                                       text=self._status_string(0))
        self.time = 0
        self.master.update()

    def _status_string(self, time):
        "Returns an appropriate status string to print."
        return "Time: %d" % time

    def _map_coords(self, x, y):
        "Maps grid positions to window positions (in pixels)."
        return (250 + 450 * ((x - self.width / 2.0) / self.max_dim),
                250 + 450 * ((self.height / 2.0 - y) / self.max_dim))

    def _draw_car(self, x, y, direction, length, color):
        "Returns a rectangle representing a robot with the specified parameters."
        tmpDirection = []
        if 'y' in direction or 'v' in direction:
            tmpDirection = [1, length]
        elif 'x' in direction or 'h' in direction:
            tmpDirection = [length, 1]

        x1, y1 = self._map_coords(x, y)
        x2, y2 = self._map_coords(x + tmpDirection[0], y + tmpDirection[1])
        return self.w.create_rectangle([x1, y1, x2, y2], fill= color)

    def update(self):
        "Redraws the visualization with the specified room and robot state."
        if self.carsImage:
            for cars in self.carsImage:
                self.w.delete(car)
                self.master.update_idletasks()
        # Draw new cars
        self.carsImage = []
        for cars in self.carsData:
            self.carsImage.append(self._draw_car(cars[0], cars[1], cars[2], cars[3], cars[4]))

        # Update text
        self.w.delete(self.text)
        self.time += 1
        self.text = self.w.create_text(
            25, 0, anchor=NW,
            text=self._status_string(self.time))
        self.master.update()
        time.sleep(self.delay)

    def done(self):
        "Indicate that the animation is done so that we allow the user to close the window."
        mainloop()

class Room(object):
    def __init__(self, width, height):
		self.width = int(max([1, width]))
		self.height = int(max([1, height]))

    def isPositionInRoom(self, x, y):
		if 0.0 <= x < self.width and 0.0 <= y < self.height:
			return True
		return False

def runSimulation(carList, width, height):
    room = Room(width, height)
    cars = carList
    anim = RushhourVisualisation(room.width, room.height, cars)
    anim.update()
    anim.done()

    return

if __name__ == '__main__':
    car1 = [1, 4, 'v', 2, 'green']
    car2 = [2, 5, 'h', 3, 'yellow']
    car3 = [5, 4, 'v', 2, 'light sky blue']
    car4 = [0, 3, 'h', 2, 'red']
    car5 = [3, 3, 'v', 2, 'orange']
    car6 = [4, 2, 'v', 3, 'violet']
    car7 = [2, 0, 'v', 2, 'pink']
    car8 = [3, 0, 'h', 2, 'cyan']
    car9 = [5, 0, 'v', 2, 'magenta']
    car10 = [1, 2, 'h', 3, 'blue']
    carList = [car1, car2, car3, car4, car5, car6, car7, car8, car9, car10]
    runSimulation(carList, 6, 6)
