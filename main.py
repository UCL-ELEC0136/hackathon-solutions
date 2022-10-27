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
    if src.storing.contains_repositories():
        repos = src.storing.pull_repositories()
    else:
        repos = src.acquiring.acquire_repositories("google")
        src.storing.push_repositories(repos)

    stars = {}
    for repo in repos:
        repo_name = repo.get("name", "unknown repo")
        stargazers = repo.get("stargazers_count", 0)
        stars[repo_name] = stargazers

    distribution = list(stars.values())

    stats = src.processing.statistics(distribution)
    logging.info("Statistics are the following", stats)

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
        stats["percentile_74"],
    )
    src.visualising.save_figure(fig, "stars_boxplot_25-75.png")

    return


def solve_task2():
    ...


def solve_task3():
    ...


def main():
    solve_task1()
    solve_task2()
    solve_task3()


if __name__ == "__main__":
    main()
