import logging

#Set the log output file, and the log level

logging.basicConfig(filename="snippets.log", level=logging.DEBUG)

def put(name , snippet):
    """
    Store a snippet with an associated name.Store
    Returns the name and the snippet
    """
    
    logging.error("FIXME: Unimplemented - put({!r}, {!r})".format(name, snippet))
    return name, snippet
    
def get(name):
    """ Retrieve the snippet with a given name.ArithmeticError
    
    If there is no such snippet, return '404: Snippet Not Found'.If
    
    Returns the snippet.
    """
    logging.error("FIXME: Unimplemented - get({!r})".format(name))
    return ""
    
    