import mysql.connector


class UseDatabase:
    """
    Usage: with UseDatabase(config: dict) as cursor:
                ...do stuff...
                
    If you create a class that defines __enter__ and __exit__, the class is
    automatically regarded as a context manager by the interpreter and can, as a
    consequence, hook into (and be used with) with. In other words, such a class conforms
    to the context management protocol, and implements a context manager.

    When an object is used with a with statement, the interpreter invokes the object’s
    __enter__ method before the with statement’s suite (block) starts.

    As soon as the with statement’s suite ends, the interpreter always invokes the object’s
    __exit__ method. When something goes wrong, the interpreter always notifies __exit__
    by passing three arguments into the method: exec_type, exc_value, and exc_
    trace. NO EXCEPTION HANDLING FOR NOW

    __init__ performs initialization (not necessary). Interpreter calls __init__ when it
    encounters a context manager (with MyContextManager(...)...)
    """
    def __init__(self, config: dict) -> None:
        self.configuration = config


    def __enter__(self) -> 'cursor':
        self.conn = mysql.connector.connect(**self.configuration)
        self.cursor = self.conn.cursor()
        return self.cursor


    def __exit__(self, exc_type, exc_value, exc_trace) -> None:
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
