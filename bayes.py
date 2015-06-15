__author__ = 'Slawek'

import matplotlib.pyplot as plt
import random as rand

with open("data1.csv", "r") as f1:
    data1 = [tuple(d.replace("\n", "").replace(",", ".").split("|")) for d in f1.readlines()]
    f1.close()
with open("data2.csv", "r") as f2:
    data2 = [tuple(d.replace("\n", "").replace(",", ".").split("|")) for d in f2.readlines()]
    f2.close()

d1 = [(float(x[0]), float(x[1])) for x in data1]
d2 = [(float(x[0]), float(x[1])) for x in data2]

# ======================== plot
plt.plot([x[0] for x in d1], [x[1] for x in d1], 'go')
plt.plot([x[0] for x in d2], [x[1] for x in d2], 'ro')
plt.xlim(-0.5, 3)
plt.ylim(0.5, 6.5)
# ======================== plot END

print("\n*** Naive Bayes classifier ***")
while True:
    try:
        new_points = int(input("Number of points to add: "))
    except ValueError:
        print("\nInput has to be an integer!\nTry Again...")
        continue
    else:
        break

for i in range(new_points):
    # ======================== random points
    r = 0
    g_points = 0
    r_points = 0
    x = rand.uniform(0, 2.5)
    y = rand.uniform(0, 6)

    while g_points + r_points < 3:
        for p in d1:
            if (p[0] - x)**2 + (p[1] - y)**2 <= r**2:
                g_points += 1
        for p in d2:
            if (p[0] - x)**2 + (p[1] - y)**2 <= r**2:
                r_points += 1
        if g_points + r_points <= 3:
            g_points = 0
            r_points = 0
            r += 0.01
    # ======================== random points END

    # ======================== probabilities
    g_apriori = len(d1) / (len(d1)+len(d2))
    r_apriori = len(d2) / (len(d1)+len(d2))
    g_chance = g_points / len(d1)
    r_chance = r_points / len(d2)
    g_posteriori = g_apriori * g_chance
    r_posteriori = r_apriori * r_chance

    print("\n\n")
    print("******************** Point nr {}".format(i))
    print("Coords of new points: (x, y) = ({0}, {1})".format(x, y))
    print("Number of green points (r={0}): {1}".format(r, g_points))
    print("Number of red points (r={0}): {1}".format(r, r_points))
    print("A priori of green: {}".format(g_apriori))
    print("A priori of red: {}".format(r_apriori))
    print("Chance of choosing green: {}".format(g_chance))
    print("Chance of choosing red: {}".format(r_chance))
    print("A posteriori of green: {}".format(g_posteriori))
    print("A posteriori of red: {}".format(r_posteriori))

    if r_posteriori > g_posteriori:
        s = 'ro'
        d2.append((x, y))
        print("*** Point has been choosen to be RED ***")
    else:
        s = 'go'
        d1.append((x, y))
        print("*** Point has been choosen to be GREEN ***")

    fig = plt.figure(1)
    fig.canvas.set_window_title("Naive Bayes classifier")
    ax = fig.add_subplot(1, 1, 1)
    plt.plot(x, y, s)
    circ = plt.Circle((x, y), radius=r, color='y', fill=False)
    ax.add_patch(circ)
    # ======================== probabilities END

plt.show()