# Hackathon #1

Hello and welcome to your first hackathon in the UCL-ELEC0136, Data Acquisition and Processing Systems course at UCL.

The goal of this laboratory is to provide you with a practical and effective understanding of how to interact with RESTful web APIs, acquire data, store and processes it, and submit it for review.
At completion, you will have acquired the following skills and knowledge:
- What an HTTP request is, and how to perform it
- What a RESTful web API is, and how to interface with it
- How to perform basic storage and retrieval operations with mongodb in Python
- How to set up a pipeline to acquire, process, store and analyse data, and send your work for review.

If you plan to work in the data industry, you will very likely encounter all of these.
Unlike our usual labs, part of this exercise is designed to test your ability to solve a problem _ex tempore_.
Your starting point is a text brief, detailing the tasks to solve with no initial code, and some instructions for submission.
This assignment will not be graded.

---

## Prerequisites
- [Miniforge](https://github.com/conda-forge/miniforge) (advised) or equivalents (e.g., Anaconda)
- An account in Mongo Atlas: https://www.mongodb.com/atlas/database
- A GitHub account
- A Fine-grained Personal Access Token, 30 days expiration date, public repositories access, no permissions

## Constraints
For each task, you must:
- Provide an `environment.yml` file that combines a conda recipe wiht pip requirements (example here: https://stackoverflow.com/a/35245610/6655465)
- Follow the [PEP8](https://peps.python.org/pep-0008/) guidelines to write good compliant code
- Use only the [GitHub API](https://docs.github.com/en/rest) to acquire any data
- Use only the `requests` library to perform HTTP requests to the GitHub API through Python, and not any wrapper around that that specifically targets the GitHub API
- Store the result of each request in MongoDB Atlas using the `pymongo` library
- For numerical calculations, use either `numpy`, `pandas`, `jax` or `pytorch`
- For data visualisation, use `matplotlib`
- Solve, at least, task 1 in class, and not at home

## Advices
- You can follow [these instructions](https://dba.stackexchange.com/questions/192507/how-to-add-useradmin-user-in-mongodb-atlas) to create a user in MongoDB Atlas
- You can follow these [guidelines](https://pip.pypa.io/en/stable/user_guide/#requirements-files) to create the requirements file. Do NOT create the file automatically with `pip freeze` or similar, as this is NOT recommended by us (in contrast to the documentation)
- Install a code formatter extension in VScode, such as [`black`](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter) or [`autopep8`](https://marketplace.visualstudio.com/items?itemName=himanoa.Python-autopep8) to auto-format your code according to PEP8.
- Take a brief scan to the [GitHub API](https://docs.github.com/en/rest) documentation to be able to orient yourself during the lab.



# Tasks
Now that we have our stage set up, let's dive into the tasks briefs.
Task 1 is designed as a primer, and to be solved in 3 hours in class.
The task is split into 4 subtasks. We will stop for 15 minutes every 30 minutes (a total of 4 times) to checkpoint on the completion of each subtask.
At each checkpoint, we review your progresses, answer questions, and provide the solution to the subtask.
We will solve the rest of the tasks in the next hackathon session.


## Task 1: Aggregated statistics
Consider the empirical distribution represented by the number of stargazers (stars) in each repository in the organisation, https://github.com/google.
We seek the answers to the following questions:
1. Retrieve all the repositories from the organisation and store the results in a MongoDB Atlas database.
2. Which is the repository with the highest number of stargazers? What the one with the lowest? What is the average number of stargazers per repo, what its standard deviation?
3. What are the `5`, `10`, `25`, `75`, `90`, and `95` percentiles of the distribution?
4. Draw a histogram of the distribution, and save it on disk. Draw one boxplot for each of these percentile pairs: `5` and `95`; `10` and `90`; `25` and `75`, and save it on disk. Check [this](https://stackoverflow.com/questions/27214537/is-it-possible-to-draw-a-matplotlib-boxplot-given-the-percentile-values-instead) on how to personalise boxplots.


### Submitting task 1
We will consider the task to be completed if the following conditions are met
- In your MongoDB Atlas there exists a user with *read-only permissions* to access all databases
- The credentials of this user are published in the [`Feedback`](#1) pull request of the assignment
- In your mongodb there is a database named `hackathon` and a collection named `answer`
- The collection contains the following document:
```json
{
  "task-1-submission": {
    "mean": <mean number of stargazers count as double>,
    "std": <standard deviation of stargazers count as double>,
    "min": <minimum number of stargazers count as integer>,
    "max": <maximum number of stargazers count as integer>,
    "percentile_5": <5-percentile of stargazers count as integer>,
    "percentile_10": <10-percentile of stargazers count as integer>,
    "percentile_25": <25-percentile of stargazers count as integer>,
    "percentile_75": <75-percentile of stargazers count as integer>,
    "percentile_90": <90-percentile of stargazers count as integer>,
    "percentile_95": <95-percentile of stargazers coun as integert"
  }
}
```
- The values of each object are mathematically correct.

Please, [create a user](https://dba.stackexchange.com/questions/192507/how-to-add-useradmin-user-in-mongodb-atlas) with **read-only permissions** to access the database, and
send publish the credentials in the `feedback` pull request of the assignment.

## Task 2: Time series
Now consider the https://github.com/google/jax repository.
We ask you to complete the following:
1. Retrieve all the commits from this repository, and store the data in a MongoDB Atlas database
2. Read all the commits from the database (do not perform a new HTTP request), grouping them by date using the mongo [`aggregate` interfce](https://www.mongodb.com/developer/languages/python/python-quickstart-aggregation/). No other grouping methods are allowed.
3. Create a timeseries that shows the number of commits per day, draw a line plot representing the timeseries and save it to disk.

#### Submitting task 2
We will consider the task to be completed under the following conditions:
- In your mongodb there is a database named `hackathon` and a collection named `answer`
- The collection contains the following document:
```json
{
  "task-2-submission": {
    "timeseries": <the number of commits per each day as an array of integers>
  }
}
```
- The values of each object are mathematically correct.

## Task 3: Classification with hand-designed features
Now consider the following issue https://github.com/google/jax/issues/5501
We seek answers to the following questions:
1. Acquire the commit object in question, and store it in a MongoDB Atlas database. Is it an open or close issue?
2. We seek to acquire the text corpus of the comment that most likely is the answer to the question in the issue title.
3. As a discriminant, hand-designed feature, we consider the comment with the highest count of `heart` + `rocket` + `horray` reactions as the correct answer to the issue.

#### Submitting task 3
We will consider the task to be completed under the following conditions:
- In your mongodb there is a database named `hackathon` and a collection named `answer`
- The collection contains the following document:
```json
{
  "task-3-submission": {
    "question": <the title of the issue>,
    "answer": <the comment with the highest number of (`heart` + `rocket` + `horray`) reactions>,
  }
}
```
- The values of each object are mathematically correct.

## FAQs
-

## References
- HTTP requests
  - What is an HTTP request
  - Python's `requests` library
- What is a RESTful web API?
  - https://en.wikipedia.org/wiki/Representational_state_transfer
  - https://www.redhat.com/en/topics/api/what-is-a-rest-api
- The GitHub API
  - Documentation: https://docs.github.com/en/rest
- Mongodb
  - How mongo implements the CRUD interface: https://www.mongodb.com/docs/manual/crud/
  - How to process data during retrieval in mongo with the aggregation API: https://www.mongodb.com/docs/atlas/app-services/mongodb/crud-and-aggregation-apis/
- Plotting in python with `matplotlib`


## Have fun! :rocket: