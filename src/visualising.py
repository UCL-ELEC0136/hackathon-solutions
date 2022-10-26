"""
This module contains methods to create, show and save usefuk plots to visualise and explore data.
"""


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


def boxplot(median, minimum, maximum, q1, q2):
    fig, ax = plt.subplots()
    boxes = [
        {
            "label": "Aggregated statistics for the commits in each google repository",
            "whislo": minimum,
            "q1": q1,
            "med": median,
            "q3": q2,
            "whishi": maximum,
            "fliers": [],
        }
    ]
    ax.bxp(boxes, showfliers=False)
    ax.set_ylabel("cm")
    return fig, ax


def lineplot(timeseries):
    ...


def save_figure(fig, path):
    fig.savefig(path, dpi=200)
