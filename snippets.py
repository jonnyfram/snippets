import psycopg2
import logging
import argparse


#Set the log output file, and the log level

logging.basicConfig(filename="snippets.log", level=logging.DEBUG)
logging.debug("Connecting to PostgreSQL")
connection = psycopg2.connect(database="snippets")
logging.debug("Database connection established.")

def main():
    """Main function"""
    logging.info("Constructing parser")

    
    parser = argparse.ArgumentParser(description="Store and retrieve snippets of text")
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Subparser for the put command
    logging.debug("Constructing put subparser")
    put_parser = subparsers.add_parser("put", help="Store a snippet")
    put_parser.add_argument("name", help="Name of the snippet")
    put_parser.add_argument("snippet", help="Snippet text")
    
    get_parser = subparsers.add_parser("get", help="Get the name of a snippet")
    get_parser.add_argument("get", help="Get name of snippet")
    
    arguments = parser.parse_args()
    #convert parsed arguments from namespace to dictionary
    arguments = vars(arguments)
    command = arguments.pop("command")
    
    if command == "put":
        name, snippet = put(**arguments)
        print("Stored {!r} as {!r}".format(snippet, name))
    elif command == "get":
        snippet = get(arguments)
        print("Retrieved snippet: {!r}".format(snippet))

def put(name, snippet):
    """Store a snippet with an associated name."""
    
    logging.info ("Storing snippet {!r}: {!r}".format(name, snippet))
    cursor = connection.cursor()
    command = "insert into snippets values (%s, %s)"
    cursor.execute(command, (name,snippet))
    connection.commit()
    logging.debug("Snippet stored successfully")
    return name, snippet
    
def get(name):
    """ Retrieve the snippet with a given name.
    If there is no such snippet, return '404: Snippet Not Found'.
    Returns the snippet."""
    logging.info("Retrieving snippet {!r}".format(name))
    cursor = connection.cursor()
    command = "select keyword from snippets where keyword='(%s,)'"
    retrieved_snippet = cursor.execute(command, (name))
    
    return retrieved_snippet
    
def time(time, name):
    """
    Retrieve the time the snippet was created.
    
    If there is no such snippet, return '404: Snippet Not Found'.
    
    Returns the time and name of snippet.
    """
    logging.error("FIXME: Unimplemented - time({!r}), {!r})".format(time, name))
    return time, name
    
if __name__ == "__main__":
    main()