"""
This module contains methods to create, show and save usefuk plots to visualise and explore data.
"""


import os
import matplotlib.pyplot as plt


def histogram(data):
    fig, ax = plt.subplots()
    ax.hist(data)
    ax.set_title(
        "Number of commits per repo in the https://github.com/google organisation"
    )
    ax.set_xlabel("Repository index")
    ax.set_ylabel("Number of commits")
    return fig, ax


def boxplot(median, minimum, maximum, q1, q3):
    fig, ax = plt.subplots()
    boxes = [
        {
            "label": "Aggregated statistics for the commits in each google repository",
            "whislo": minimum,
            "q1": q1,
            "med": median,
            "q3": q3,
            "whishi": maximum,
            "fliers": [],
        }
    ]
    ax.bxp(boxes, showfliers=False)
    ax.set_ylabel("cm")
    return fig, ax


def lineplot(x, y):
    fig, ax = plt.subplots()
    ax.plot(x, y)
    return fig, ax


def save_figure(fig, path):
    folder = os.path.dirname(path)
    if folder != '':
        os.makedirs(folder, exist_ok=True)
    return fig.savefig(path, dpi=200)
