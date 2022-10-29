"""
This module contains methods to create, show and save usefuk plots to visualise and explore data.
"""


import os
import matplotlib.pyplot as plt


def histogram(data):
    fig, axes = plt.subplots()
    axes.hist(data)
    axes.set_title(
        "Number of commits per repo in the https://github.com/google organisation"
    )
    axes.set_xlabel("Repository index")
    axes.set_ylabel("Number of commits")
    return fig, axes


def boxplot(median, minimum, maximum, quantile_1, quantile_3):
    fig, axes = plt.subplots()
    boxes = [
        {
            "label": "Aggregated statistics for the commits in each google repository",
            "whislo": minimum,
            "q1": quantile_1,
            "med": median,
            "q3": quantile_3,
            "whishi": maximum,
            "fliers": [],
        }
    ]
    axes.bxp(boxes, showfliers=False)
    axes.set_ylabel("cm")
    return fig, axes


def lineplot(x_values, y_values):
    fig, axes = plt.subplots()
    axes.plot(x_values, y_values)
    return fig, axes


def save_figure(fig, path):
    folder = os.path.dirname(path)
    if folder != "":
        os.makedirs(folder, exist_ok=True)
    return fig.savefig(path, dpi=200)
