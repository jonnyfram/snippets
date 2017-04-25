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
    get_parser.add_argument("name", help="Get name of snippet")
   
    update_parser = subparsers.add_parser("update", help="Replace/update name of snippet and text")
    update_parser.add_argument("name", help="Name of the snippet")
    update_parser.add_argument("snippet", help="Snippet text")
    
    catalog_parser = subparsers.add_parser("catalog", help="Show all snippet keywords")
    
    search_parser = subparsers.add_parser("search", help="Search for strings like the input")
    search_parser.add_argument("searchtext", help="search for this text string")
    
    arguments = parser.parse_args()
    #convert parsed arguments from namespace to dictionary
    arguments = vars(arguments)
    command = arguments.pop("command") # removes part of arguments

    if command == "put":
        name, snippet = put(**arguments)
        print("Stored {!r} as {!r}".format(snippet, name))
        
    elif command == "get":
        snippet = get(**arguments)
        print("Retrieved snippet: {!r}".format(snippet))
        
    elif command == "update":
        name, snippet = update(**arguments)
        print("Updated snippet: {!r} with {!r}".format(snippet, name))
        
    elif command == "catalog":
        catalog()
        
    elif command == "search":
        search_text = search(**arguments)

def catalog():
    """Print the whole database"""
    cursor = connection.cursor()
    cursor.execute("select * from snippets")
    cat = cursor.fetchall()

    print (cat)
    
def search(search_text):
    """"""
    logging.info("searching for snippet text {!r}".format(search_text))
    
    cursor = connection.cursor()
    cursor.execute("select * from snippets")
    cursor.fetchall()
    
    results = cursor.execute("select * from table where prescription like '%search_text%'", (search_text))
    print(results)

def put(name, snippet):
    """Store a snippet with an associated name."""
    logging.info ("Storing snippet {!r}: {!r}".format(name, snippet))
    cursor = connection.cursor()
    
    with connection, connection.cursor() as cursor:
        cursor.execute("insert into snippets values (%s, %s)", (name, snippet))
        return name, snippet
    """try:
        command = "insert into snippets values (%s, %s)"
        cursor.execute(command, (name,snippet))
    except psycopg2.IntegrityError as e:
        connection.rollback()
        command = "update snippets set message=%s where keyword %s"
        cursor.execute(command, (snippet,name))

    connection.commit()"""
    logging.debug("Snippet stored successfully")

    
def get(name):
    """ Retrieve the snippet with a given name.
    If there is no such snippet, return '404: Snippet Not Found'.
    Returns the snippet."""
    logging.info("Retrieving snippet {!r}".format(name))
    cursor = connection.cursor()
    command = "select keyword from snippets where keyword=%s"
    
    with connection, connection.cursor() as cursor:
        cursor.execute("select message from snippets where keyword=%s", (name,))
        row = cursor.fetchone()
        return cursor.fetchone()
       #returns tuple from database
        
    #return_value = cursor.fetchone() 
    if not return_value:
        return "404: snippet not found"
    
def update(name, snippet):
    """replaces/updates a snippet with a new one"""
    logging.info ("Overwriting snippet {!r}: {!r}".format(name, snippet))
    cursor = connection.cursor()

    command = "insert into snippets values (%s, %s)"
    cursor.execute(command, (name,snippet))

    
if __name__ == "__main__":
    main()