# %%
import matplotlib.pyplot as plt

# ? Line graph
x_values = [0, 1, 2, 3, 4, 5]
squares = [0, 1, 4, 9, 16, 25]

fig, ax = plt.subplots()
ax.plot(x_values, squares)

plt.show()
# %%
import matplotlib.pyplot as plt

# ? Scatter plot
x_values = list(range(1000))
squares = [x**2 for x in x_values]

fig, ax = plt.subplots()
ax.scatter(x_values, squares, s=10)

plt.show()
# %%
import matplotlib.pyplot as plt

# ? Buing styles plots
x_values = list(range(1000))
squares = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, squares, s=10)

plt.show()
print(plt.style.available) #avaible styles
# %%
import matplotlib.pyplot as plt

# ? adding titles and labels, and scaling axes
x_values = list(range(1000))
squares = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, squares, s=10)

#set chart title and label axes
ax.set_title('Square Numbers', fontsize=24)
ax.set_xlabel('Value', fontsize=24)
ax.set_ylabel('Square of Value', fontsize=24)

#set scale axes, and size of tick labels
ax.axis([0, 1100, 0, 1_100_000])
ax.tick_params(axis='both', labelsize=14)
# colormap (color points line and shadow add)
ax.scatter(x_values, squares, c=squares, cmap=plt.cm.Blues, s=10)
plt.show()
# %%
import matplotlib.pyplot as plt

# ? Emphasizing points
x_values = list(range(1000))
squares = [x**2 for x in x_values]

fig, ax = plt.subplots()
ax.scatter(x_values, squares, c=squares, cmap=plt.cm.Blues, s=10)

ax.scatter(x_values[0], squares[0], c='green', s=100)
ax.scatter(x_values[-1], squares[-1], c='red', s=100)

ax.set_title('Square Numbers', fontsize=24)

plt.show()
# %%
import matplotlib.pyplot as plt

# ? Emphasizing points
x_values = list(range(1000))
squares = [x**2 for x in x_values]

#setting a custom figure size
fig, ax = plt.subplots(figsize=(10, 6), dpi=128)

ax.scatter(x_values, squares, c=squares, cmap=plt.cm.Blues, s=10)

ax.scatter(x_values[0], squares[0], c='green', s=100)
ax.scatter(x_values[-1], squares[-1], c='red', s=100)

ax.set_title('Square Numbers', fontsize=24)

# removing axes
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

#saving a plot
plt.savefig('squares.png', bbox_inches='tight')

plt.show()
# %%
import matplotlib.pyplot as plt

# ? Plots two sets of data
x_values =list(range(11))
squares = [x**2 for x in x_values]
cubes = [x**3 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()

ax.scatter(x_values, squares, c='blue', s=10)
ax.scatter(x_values, cubes, c='red', s=10)

# fill space between data sets
ax.fill_between(x_values, cubes, squares, facecolor='blue', alpha=0.25)
plt.show()
# %%
from datetime import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import dates as mdates

# ? Plots daily high temp
dates = [
    dt(2019, 6, 21), dt(2019, 6, 22),
    dt(2019, 6, 23), dt(2019, 6, 24),
]
highs = [56, 57, 57, 64]

fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')

ax.set_title('Daily high temp', fontsize=24)
ax.set_ylabel("Temp (F)", fontsize=16)
x_axis = ax.get_xaxis()
x_axis.set_major_formatter(mdates.DateFormatter('%B %d %Y'))

fig.autofmt_xdate()
plt.show()
# %%
import matplotlib.pyplot as plt

# ? Sharing an x axis
x_values = list(range(11))
squares = [x**2 for x in x_values]
cubes = [x**3 for x in x_values]

fig, axs = plt.subplots(2, 1, sharex=True)

axs[0].scatter(x_values, squares)
axs[0].set_title('Squares')

axs[1].scatter(x_values, cubes, c='red')
axs[1].set_title('Cubes')

plt.show()
# %%
import matplotlib.pyplot as plt

# ? Sharing an y axis
x_values = list(range(11))
squares = [x**2 for x in x_values]
cubes = [x**3 for x in x_values]

plt.style.use('seaborn')
fig, axs = plt.subplots(2, 1, sharey=True)

axs[0].scatter(x_values, squares)
axs[0].set_title('Squares')

axs[1].scatter(x_values, cubes, c='red')
axs[1].set_title('Cubes')

plt.show()
# %%
