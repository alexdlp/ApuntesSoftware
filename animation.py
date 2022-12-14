

class Particle:
    def __init__(self, x, y, ang_vel):
        self.x = x
        self.y = y
        self.ang_vel = ang_vel


class ParticleSimulator:
    def __init__(self, particles) -> None:
        self.particles = particles
    
    def evolve(self,totalTime):
        dt = 0.00001
        nsteps = int(dt/totalTime)

        for i in range(nsteps):
            for p in self.particles:

                # 1. calculate de direction
                norm = (p.x**2 + p.y**2)**0.5
                Vx = (p.y*p.ang_vel)/norm
                Vy = -(p.x*p.ang_vel)/ norm
                
                # 2. calculate the displacement
                dx = dt * Vx; p.x += dx
                dy = dt * Vy; p.y += dy


import matplotlib.pyplot as plt
from matplotlib import animation

def visualize(simulator):
    X = [p.x for p in simulator.particles]
    Y = [p.y for p in simulator.particles]

    fig = plt.figure()
    ax = plt.subplot(111, aspect='equal')
    line, = ax.plot(X, Y, 'ro')

    # Axis limits
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)

    # It will be run when the animation starts
    def init():
        line.set_data([], [])
        return line, # The comma is important!
    
    def animate(i):
    # We let the particle evolve for 0.01 time units
        simulator.evolve(0.01)
        X = [p.x for p in simulator.particles]
        Y = [p.y for p in simulator.particles]
        line.set_data(X, Y)
        return line,
    
    # Call the animate function each 10 ms
    anim = animation.FuncAnimation(fig, animate, init_func=init, blit=True, interval=10)
    plt.show()


def test_visualize():
    particles = [
    Particle(0.3, 0.5, 1),
    Particle(0.0, -0.5, -1),
    Particle(-0.1, -0.4, 3)
    ]
    simulator = ParticleSimulator(particles)
    visualize(simulator)


if __name__ == '__main__':
    test_visualize()