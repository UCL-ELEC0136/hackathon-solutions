"""
A module to perform requests to the GitHub API.
It contains methods to construct, perform, and post-process requests.
"""


import logging
import os
import sys
import requests


GITHUB_API_ENTRYPOINT = "https://api.github.com"
USERNAME = "epignatelli"


def send_request(request, auth=None):
    """
    Performs a GET request and returns the response in json format.
    The function stops if any error is encountered during the request process.

    Args:
        request (str): the request to perform as a string
        auth (Tuple[str, str]): GitHub credentials to perform authenticated
            requests in the form `auth=(username, token)`.
            Authenticated requests increase API rate limit:
            https://docs.github.com/rest/overview/resources-in-the-rest-api#rate-limiting

    Returns:
        (List[Dict]): the response in json format as a list of dictionaries
    """
    # perform the request
    response = requests.get(request, auth=auth, timeout=10)

    # check for errors
    response.raise_for_status()
    if response.status_code != 200:
        msg = "Unexpected exception occurred with status code {}. " + str(
            response.status_code
        )
        msg += f"The suspected reason is {response.reason}"
        raise ValueError(msg)

    # read reponse as json and return it
    response_json = response.json()
    return response_json


def paginate(request, per_page=100, max_page=sys.maxsize, auth=None):
    """
    Resolves GitHub pagination for the `request` of interest,stopping
    when the response returns no result or when the maximum page is reached.

    Args:
        per_page (int): number of results to return per each page
        max_page (int): the latest page to iterate to; it can be useful
        to stop the iteration early, e.g., for debugging purposes

    Returns:
        (List[Dict]): the results for all pages of the requests,
        concatenated in one list
    """
    page = 1
    responses = []
    while True:
        # build request string and send
        page_request = f"{request}?per_page={per_page}&page={page}"
        response = send_request(page_request, auth=auth)
        responses += list(response)

        # provide feedback while looping
        logging.info(f"Succesfully performed request {page_request}")

        # check for termination and update state
        if len(response) == 0:
            break
        if page >= max_page:
            break

        page += 1

    return responses


def acquire_repositories(organisation):
    """
    Performs a GET request to GitHub to retrieve *all* repositories
    in an organisation. This function handles pagination.

    Args:
        organisation (str): the name of the GitHub organisation or
        username as it appears of GitHub

    Returns:
        (List[Dict]): the results for all pages of the requests,
        concatenated in one list
    """
    # see https://docs.github.com/en/rest/repos/repos
    request = os.path.join(GITHUB_API_ENTRYPOINT, "orgs", organisation, "repos")
    response = paginate(request)
    return response


def acquire_commits(organisation, repository, auth=None):
    """
    Performs a GET request to GitHub to retrieve *all*
    the commits of repository. This function handles pagination.

    Args:
        organisation (str): the name of the GitHub organisation
        or username as it appears of GitHub repository (str):
        the name of the repository than contains the commits of interest

    Returns:
        (List[Dict]): the results for all pages of the requests,
        concatenated in one list
    """
    # see https://docs.github.com/en/rest/commits/commits
    request = os.path.join(
        GITHUB_API_ENTRYPOINT, "repos", organisation, repository, "commits"
    )
    response = paginate(request, auth=auth)
    return response


def acquire_issue_comment(organisation, repository, issue):
    """
    See
    https://docs.github.com/en/rest/issues/comments#list-issue-comments
    """
    raise NotImplementedError()


def acquire_issue_reactions(organisation, repository, issue):
    """
    See
    https://docs.github.com/en/rest/reactions#list-reactions-for-an-issue
    """
    raise NotImplementedError()
