"""This module implements a CRUD (Create, Read, Update, Delete) interface to our noSQL database."""


import os
import pymongo


MONGODB_SERVER_ADDRESS = (
    "mongodb+srv://{username}:{password}@cluster0.0ryuw.mongodb.net/test"
)
DATABASE_NAME = "hackathon"
REPOSITORIES_COLLECTION_NAME = "repositories"
COMMITS_COLLECTION_NAME = "commits"
COMMENTS_COLLECTION_NAME = "comments"
REACTIONS_COLLECTION_NAME = "reactions"


def get_server():
    # load password from disk
    current_folder = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(current_folder, "mongodb.pwd")
    with open(filepath, "r") as file:
        password = file.read()

    # connect to your local mongo instance
    address = MONGODB_SERVER_ADDRESS.format(username="student", password=password)
    server = pymongo.MongoClient(address)
    return server


def create(data, database_name, collection_name):
    # connect to your local mongo instance
    server = get_server()
    # grab the collection you want to push the data into
    database = server[database_name]
    collection = database[collection_name]
    # push the data
    return collection.insert_many(data)


def read(database_name, collection_name, query):
    # handle null inputs
    query = query or []

    # connect to your local mongo instance
    server = get_server()

    # retrieve the data in `collection_name` that matches `query`
    data = server[database_name][collection_name].aggregate(query)

    return data


def contains_data(database_name, collection_name):
    server = get_server()

    # check if database exists
    databases = server.list_database_names()
    if database_name not in databases:
        return False

    # check if collection exists
    collections = server[database_name].list_collection_names()
    if collection_name not in collections:
        return False

    # check if collection contains elements
    collection = server[database_name][collection_name]
    if collection.count_documents({}) <= 0:
        return False

    return True


def contains_repositories():
    return contains_data(DATABASE_NAME, REPOSITORIES_COLLECTION_NAME)


def create_repositories(repos):
    return create(repos, DATABASE_NAME, REPOSITORIES_COLLECTION_NAME)


def read_repositories(query=None):
    return read(DATABASE_NAME, REPOSITORIES_COLLECTION_NAME, query)


def contains_commits():
    return contains_data(DATABASE_NAME, COMMITS_COLLECTION_NAME)


def create_commits(repos):
    return create(repos, DATABASE_NAME, COMMITS_COLLECTION_NAME)


def read_commits(query=None):
    return read(DATABASE_NAME, COMMITS_COLLECTION_NAME, query)


def read_groupped_commits():
    query = [
        {"$addFields": {"date": "$commit.author.date"}},
        {"$project": {"date": {"$arrayElemAt": [{"$split": ["$date", "T"]}, 0]}}},
        {"$project": {"date": {"$toDate": "$date"}}},
        {"$group": {"_id": "$date", "count": {"$sum": 1}}},
        {"$sort": {"_id": 1}},
        {"$project": {"date": "$_id", "count": "$count"}},
    ]
    return read(DATABASE_NAME, COMMITS_COLLECTION_NAME, query)
