import perceptrons_data as data
import matplotlib.pyplot as plt

#plot1
point = [x[0] for x in data.mystery1]
plt.scatter(*zip(*point))
plt.show()

#plot2
point = [x[0] for x in data.mystery2]
xyz = zip(*point)

# Use matplotlib to create a 3D scatter plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(*xyz)

# Show the plot
plt.show()


