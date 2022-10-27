# Hackathon #1

Welcome to the first hackathon of UCL-ELEC0136, Data Acquisition and Processing Systems.

### Objectives
The goal of this laboratory is to provide you with an understanding of how to practically interact with RESTful web APIs, how to extract data, store it, and processes it.
At completion, we expect you to have acquired the following skills:
- Know what a RESTful web API is, and how to interface with it
- Know how to perform basic storage and retrieval operations with mongodb from Python
- Being able to setup a pipeline to acquire, process, store and analyse data

Unlike our usual labs, this exercise is designed to test your ability to solve a problem _ex tempore_.
Your starting point is a brief, detailing the tasks to solve with no initial code.
Let's dive into it.

---

### Task 1: Aggregated statistics
Consider the empirical distribution represented by the number of stargazers (stars) of each repository in the https://github.com/google organisation.
We seek the answers to the following questions:
- Retrieve all the repositories from the organisation
- Store the results into a local mongo database
- Which is the repository with the highest number of stargazers? What the one with the lowest?
- What is the average number of stargazers per repo, what its variance?
- What are the 5, 10, 25, 75, 90, and 95 percentile of the distribution?
- Draw a histogram of the distribution, and save it on disk
- Draw one boxplot for each of these percentile pairs: 5 and 95; 10 and 90; 25 and 75, and save it on disk. Check [this](https://stackoverflow.com/questions/27214537/is-it-possible-to-draw-a-matplotlib-boxplot-given-the-percentile-values-instead) on how to personalise boxplots.

### Task 2: Time series
Now consider the https://github.com/google/jax repository.
We ask you to complete the following:
- Retrieve all the commits from this repository
- Store the results into a local mongo database
- Create a timeseries that shows the number of commits per day
- Draw a line plot representing the timeseries and save it to disk


### Task 3: Classification with hand-designed features
Now consider the following issue https://github.com/google/jax/issues/5501
We seek answers to the following questions:
- Is it an open or close issue?
- Retrieve all the comments in the issue
- Store these into a local mongo database
- What's the comment with most `reactions`? Can you select the correct answer to the issue by using `reactions` count and type?
- Provide a python dictionary containing two keys:
  - `Question` whose dictionary `value` is the `title` of the issue
  - `Answer` whose dictionary `value` is the answer to the issue question

---

### Constraints
For each subtask, you must:
- Provide a `requirements.txt` file with the required packages
- Follow the [PEP8](https://peps.python.org/pep-0008/) guidelines for writing code
- Use the [GitHub API](https://docs.github.com/en/rest) to acquire any data
- Use only the `requests` library for performing HTTP requests to the GitHub API through Python, and not any wrapper around that, specifically targeting the GitHub API
- Store The result of each request must be stored in mongodb using the `pymongo` library
- For numerical calculations, use either `numpy`, `pandas`, `jax` or `pytorch`
- For data visualisation, use `matplotlib`
- Do not solve this at home, this is meant to be solved during class


### Advices
- Follow the [guidelines](https://pip.pypa.io/en/stable/user_guide/#requirements-files) for the requirements file. Do NOT create the file automatically with `pip freeze` or similar, this is NOT recommended
- Install a code formatter extension in VScode, such as [`black`](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter) or [`autopep8`](https://marketplace.visualstudio.com/items?itemName=himanoa.Python-autopep8). This will allow you to auto-format your code according to PEP8.
- Take a brief scan to the [GitHub API](https://docs.github.com/en/rest) documentation to be able to orient yourself during the lab


### Prerequisites
- [Miniforge](https://github.com/conda-forge/miniforge) (advised) or equivalents (e.g., Anaconda)
- Downlaoded and installed mongodb: https://www.mongodb.com/docs/manual/installation/
- A working GitHub account

---

### FAQs

### References
- What is a RESTful web API?
  - https://en.wikipedia.org/wiki/Representational_state_transfer
  - https://www.redhat.com/en/topics/api/what-is-a-rest-api
