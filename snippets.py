import logging

#Set the log output file, and the log level

logging.basicConfig(filename="snippets.log", level=logging.DEBUG)

def main():
    """Main function"""
    logging.info("Constructing parse")
    parser = argparse.ArgumentParser(description="Store and retrieve snippets of text")
    arguments parser.parse_args()

def put(name , snippet):
    """
    Store a snippet with an associated name.Store
    Returns the name and the snippet
    """
    
    logging.error("FIXME: Unimplemented - put({!r}, {!r})".format(name, snippet))
    return name, snippet
    
def get(name):
    """ Retrieve the snippet with a given name.
    
    If there is no such snippet, return '404: Snippet Not Found'.
    
    Returns the snippet.
    """
    logging.error("FIXME: Unimplemented - get({!r})".format(name))
    return ""
    
def time(time, name):
    """
    Retrieve the time the snippet was created.
    
    If there is no such snippet, return '404: Snippet Not Found'.
    
    Returns the time and name of snippet.
    """
    logging.error("FIXME: Unimplemented - get({!r}), {!r})".format(time, name))
    return time, name
    
if __name__ == "__main__":
    main()