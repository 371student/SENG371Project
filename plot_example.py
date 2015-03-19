# WARNING - this code was made using python 3.4

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# WARNING - this might not be needed in python 2.7
def bytedate2num(fmt):
    def converter(b):
        return mdates.strpdate2num(fmt)(b.decode('ascii'))
    return converter

# date_converter = bytedate2num("%Y-%m-%d")

def graph(proj_name, data_file):
	# Getting data from txt file
	date, coup_fact, grow_fact = np.loadtxt(data_file, 
											unpack = True,
											delimiter = ',',
											converters = {0: bytedate2num("%Y-%m-%d")}
											)

	# Plot both factors against date
	plt.plot_date(x=date, y=grow_fact, fmt='r-')
	plt.plot_date(x=date, y=coup_fact, fmt='b-')

	# Trendlines
	z1 = np.polyfit(date, grow_fact, 20)
	p1 = np.poly1d(z1)
	z2 = np.polyfit(date, coup_fact, 20)
	p2 = np.poly1d(z2)

	plt.plot_date(x=date, y=p1(date), fmt='r-')
	plt.plot_date(x=date, y=p2(date), fmt='b-')

	# Trendline correlation - oddly linear - probably wrong
	# z3 = np.polyfit(coup_fact, grow_fact, 30)
	# p3 = np.poly1d(z3)
	# plt.plot_date(x=date, y=p3(date), fmt='r-')

	# Graph labelling
	plt.title(proj_name + ' - Growth VS Coupling over Time')
	plt.xlabel('Time')
	plt.ylabel('Factors')
	plt.legend(['Growth Factor', 'Coupling Factor', 'Growth Trend', 'Coupling Trend'], loc="center right")
	plt.show()

graph("Django","django_data.csv")