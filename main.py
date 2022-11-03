"""
This is the main module responsible for solving the tasks.
To solve each task just run `python main.py`.
"""

import logging

import src.processing
import src.acquiring
import src.visualising
import src.storing


def solve_task1():
    # check if mongo already contains repos
    # if not, acquire and store
    if not src.storing.contains_repositories():
        repos = src.acquiring.acquire_repositories("google")
        src.storing.create_repositories(repos)

    # read repos from mongo
    repos = src.storing.read_repositories()

    # get stargazers count for each repo
    stars = {}
    for repo in repos:
        repo_name = repo.get("name", "unknown repo")
        stargazers = repo.get("stargazers_count", 0)
        stars[repo_name] = stargazers

    distribution = list(stars.values())

    # calculate the statistics of the distribution
    stats = src.processing.statistics(distribution)
    logging.info("Statistics are the following " + str(stats))

    # plot figures
    fig, _ = src.visualising.histogram(distribution)
    src.visualising.save_figure(fig, "stars_histogram.png")

    fig, _ = src.visualising.boxplot(
        stats["mean"],
        stats["min"],
        stats["max"],
        stats["percentile_5"],
        stats["percentile_95"],
    )
    src.visualising.save_figure(fig, "stars_boxplot_5-95.png")

    fig, _ = src.visualising.boxplot(
        stats["mean"],
        stats["min"],
        stats["max"],
        stats["percentile_10"],
        stats["percentile_90"],
    )
    src.visualising.save_figure(fig, "stars_boxplot_10-90.png")

    fig, _ = src.visualising.boxplot(
        stats["mean"],
        stats["min"],
        stats["max"],
        stats["percentile_25"],
        stats["percentile_75"],
    )
    src.visualising.save_figure(fig, "stars_boxplot_25-75.png")


def solve_task2():
    # read auth token
    with open("src/github.token", "r") as file:
        token = file.read().strip()

    # acquire data if not in mongo
    if not src.storing.contains_commits():
        commits = src.acquiring.acquire_commits(
            "google", "jax", auth=(src.acquiring.USERNAME, token)
        )
        src.storing.create_commits(commits)

    # read commits and group them by day
    commits = list(src.storing.read_groupped_commits())

    # plot the timeseries
    x = [d["date"] for d in commits]
    y = [d["count"] for d in commits]
    fig, _ = src.visualising.lineplot(x, y)
    src.visualising.save_figure(fig, "timeseries.png")
    return


def solve_task3():
    ...


def main():
    solve_task1()
    solve_task2()
    solve_task3()


if __name__ == "__main__":
    main()
