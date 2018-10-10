from matplotlib import pyplot

# data
machine_counts = [18,4,2]

#labels
machine_names = ["PC", "Mac", "Linux"]

#draw
pyplot.pie(machine_counts, labels = machine_names, autopct = "%.1f%%", explode=[0,0.1,0])
pyplot.title("PC v Mac v Linux")
pyplot.axis("equal")


#show
pyplot.show()