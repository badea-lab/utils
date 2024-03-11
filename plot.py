'''
Author: Anthony Badea
Date: 03/11/24
Purpose: Plotting utils
'''

import numpy as np

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager

import mplhep as hep
hep.style.use("CMS")


def plot(
	x,
	y, 
	xerr=None, 
	yerr=None,
	xlabel="xlabel", 
	ylabel="ylabel", 
	xlim=[0,1],
	xlog=False,
	ylim=[0,1],
	ylog=False,
	outFileName=None
	):
	
	# make plot
	fig = plt.figure(figsize=(6, 5))
	ax = plt.axes([0.1, 0.1, 0.85, 0.85])

	plt.errorbar(x, y, xerr=xerr, yerr=yerr, fmt='-o', color="red")

	# set labels
	ax.set_xlabel(xlabel, fontsize=18, labelpad=9, horizontalalignment='right', x=1.0)
	ax.set_ylabel(ylabel, fontsize=18, labelpad=9, horizontalalignment='right', y=1.0)

	# tick params
	tick_params_major = {"which"     : "major",
	                     "length"    : 10,
	                     "width"     : 1.25,
	                     "direction" : "in",
	                     "right"     : True,
	                     "top"       : True,
	                     "labelsize" : 18,
	                     "pad"       : 8}
	tick_params_minor = {"which"     : "minor",
	                     "length"    : 4,
	                     "width"     : 1,
	                     "direction" : "in",
	                     "right"     : True,
	                     "top"       : True,
	                     "labelsize" : 15}

	# ax.xaxis.set_minor_locator(AutoMinorLocator(5))
	# ax.yaxis.set_minor_locator(AutoMinorLocator(5))
	ax.tick_params(**tick_params_major)
	ax.tick_params(**tick_params_minor)
	plt.locator_params(axis='y', nbins=8)
	plt.locator_params(axis='x', nbins=8)

	# ax.ticklabel_format(axis='y', style='sci')
	plt.ticklabel_format(axis='y', style='sci', scilimits=(1,2), useMathText=True)

	# set limits and scale
	ax.set_xlim(xlim[0], xlim[1])
	ax.set_ylim(ylim[0], ylim[1])
	plt.xscale("log" if xlog else "linear")
	plt.yscale("log" if ylog else "linear")

	if outFileName:
		plt.savefig(outFileName, bbox_inches="tight")

	return fig, ax

def text(x, y, text="text", fontsize=13, color="black"):
	plt.text(x, y, text, fontsize=fontsize, color=color, ha='left', va='top', transform=plt.gca().transAxes)


# plot
x = [20,  20, 10,  4, 1.3, 1.2, 1.1, 0.35, 0.12, 0.04, 0.025]
y = [300, 30, 35, 13,   2,  11, 1.8, 1,  3.5,    20,   70]
fig, ax = plot(x,y,xlim=[10**-2,3*10**1], ylim=[0.8*10**0, 4*10**2])
plt.savefig("hi.pdf", bbox_inches="tight")