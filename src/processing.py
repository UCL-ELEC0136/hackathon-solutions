"""
This module contains methods to perform numerical processing of the acquired data.
"""


import jax.numpy as jnp


def statistics(distribution):
    """
    Returns useful statistics on the number of commits for each repository.

    Args:
        distribution (List[int]): a List or Sequence of counts, e.g. the count of commits for each repository.

    Returns:
        (Dict): A dictionary containing the following keys and their respective values
            - "mean": The mean of the distribution
            - "std": The standard deviation of the distribution
            - "percentile_5": The 5-percentile of the distribution
            - "percentile_10": The 10-percentile of the distribution
            - "percentile_25": The 25-percentile of the distribution
            - "percentile_75": The 75-percentile of the distribution
            - "percentile_90": The 90-percentile of the distribution
            - "percentile_95": The 95-percentile of the distribution
    """
    array = jnp.array(distribution)
    mean = jnp.mean(array)
    std = jnp.std(array)
    percentile_5 = jnp.percentile(array, 5)
    percentile_10 = jnp.percentile(array, 10)
    percentile_25 = jnp.percentile(array, 25)
    percentile_75 = jnp.percentile(array, 75)
    percentile_90 = jnp.percentile(array, 90)
    percentile_95 = jnp.percentile(array, 95)

    return {
        "mean": mean,
        "std": std,
        "percentile_5": percentile_5,
        "percentile_10": percentile_10,
        "percentile_25": percentile_25,
        "percentile_75": percentile_75,
        "percentile_90": percentile_90,
        "percentile_95": percentile_95,
    }


def group_commits(commits):
    ...


def sort_comments_by_reactions(comments, reactions):
    ...


def get_issue_answer(issue):
    """
    Returns:
        (Dict):{
            "Question": <issue-title>,
            "Answer: <comment-with-most--heart-reactions?>,
            }
    """
