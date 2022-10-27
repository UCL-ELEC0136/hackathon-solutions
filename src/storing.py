import pymongo


MONGODB_SERVER_ADDRESS = "mongodb+srv://{username}:{password}@cluster0.0ryuw.mongodb.net/test"
DATABASE_NAME = "hackathon"
REPOSITORIES_COLLECTION_NAME = "repositories"
COMMITS_COLLECTION_NAME = "commits"
COMMENTS_COLLECTION_NAME = "comments"
REACTIONS_COLLECTION_NAME = "reactions"


def get_server():
    # connect to your local mongo instance
    address = MONGODB_SERVER_ADDRESS.format(username="student", password="student")
    server = pymongo.MongoClient(address)
    return server


def push(data, database_name, collection_name):
    # connect to your local mongo instance
    server = get_server()
    # grab the collection you want to push the data into
    database = server[database_name]
    collection = database[collection_name]
    # push the data
    return collection.insert_many(data)


def pull(database_name, collection_name, query={}):
    # connect to your local mongo instance
    server = get_server()

    # retrieve the data in `collection_name` that matches `query`
    data = server[database_name][collection_name].find(query)

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


def push_repositories(repos):
    return push(repos, DATABASE_NAME, REPOSITORIES_COLLECTION_NAME)


def pull_repositories():
    return pull(DATABASE_NAME, REPOSITORIES_COLLECTION_NAME)

