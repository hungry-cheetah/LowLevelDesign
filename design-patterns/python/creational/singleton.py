"""
This script demonstrates various ways to implement the Singleton Design Pattern in Python.
Each method has its own advantages and trade-offs.
"""

import threading
import logging
import sqlite3
from enum import Enum

'''
Key Differences:

    Feature	        __new__	                        __init__
    Purpose	    Creates a new instance	       Initializes the instance 
    Called	    Before __init__	                After __new__
    Returns	    A new instance	                Nothing (None)
    Use Cases	Custom instance creation,      Setting up instance attributes
                singleton, immutable types	    

'''


# 1. Lazy Initialization (Not Thread-Safe)
class SingletonLazy:
    _instance = None  # Class variable to store single instance

    def __init__(self):
        print("Initializing SingletonLazy...")

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = SingletonLazy()
        return cls._instance

# 2. Thread-Safe Singleton (Using synchronized lock)
class SingletonThreadSafe:
    _instance = None
    _lock = threading.Lock()

    def __init__(self):
        print("Initializing SingletonThreadSafe...")

    @classmethod
    def get_instance(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = SingletonThreadSafe()
        return cls._instance

# 3. Double-Checked Locking Singleton
class SingletonDoubleChecked:
    _instance = None
    _lock = threading.Lock()

    def __init__(self):
        print("Initializing SingletonDoubleChecked...")

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = SingletonDoubleChecked()
        return cls._instance

# 4. Eager Initialization
class SingletonEager:
    _instance = object()

    def __init__(self):
        raise RuntimeError("Use get_instance() instead")

    @classmethod
    def get_instance(cls):
        return cls._instance

# 5. Bill Pugh Singleton (Lazy Loading)
class SingletonBillPugh:
    class _SingletonHelper:
        _instance = SingletonBillPugh()

    def __new__(cls):
        return cls._SingletonHelper._instance

# 6. Enum Singleton
class SingletonEnum(Enum):
    INSTANCE = object()

# 7. Static Block Initialization
class SingletonStaticBlock:
    _instance = None
    try:
        _instance = object()
    except Exception as e:
        raise RuntimeError("Error during singleton initialization")

    @classmethod
    def get_instance(cls):
        return cls._instance

# Real-world Example: Logger Singleton
class LoggerSingleton:
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = logging.getLogger("AppLogger")
            handler = logging.StreamHandler()
            cls._instance.addHandler(handler)
        return cls._instance

# Real-world Example: Database Connection Singleton
class Database:
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = sqlite3.connect(":memory:")
        return cls._instance

if __name__ == "__main__":
    print("Testing Singleton Implementations:")
    
    # Lazy Initialization
    s1 = SingletonLazy.get_instance()
    s2 = SingletonLazy.get_instance()
    print("Lazy Singleton:", s1 is s2)
    
    # Thread-Safe Singleton
    s1 = SingletonThreadSafe.get_instance()
    s2 = SingletonThreadSafe.get_instance()
    print("Thread-Safe Singleton:", s1 is s2)
    
    # Double-Checked Locking
    s1 = SingletonDoubleChecked.get_instance()
    s2 = SingletonDoubleChecked.get_instance()
    print("Double-Checked Locking Singleton:", s1 is s2)
    
    # Eager Initialization
    s1 = SingletonEager.get_instance()
    s2 = SingletonEager.get_instance()
    print("Eager Initialization Singleton:", s1 is s2)
    
    # Bill Pugh Singleton
    s1 = SingletonBillPugh()
    s2 = SingletonBillPugh()
    print("Bill Pugh Singleton:", s1 is s2)
    
    # Enum Singleton
    s1 = SingletonEnum.INSTANCE
    s2 = SingletonEnum.INSTANCE
    print("Enum Singleton:", s1 is s2)
    
    # Static Block Initialization
    s1 = SingletonStaticBlock.get_instance()
    s2 = SingletonStaticBlock.get_instance()
    print("Static Block Initialization Singleton:", s1 is s2)
    
    # Logger Singleton
    logger1 = LoggerSingleton.get_instance()
    logger2 = LoggerSingleton.get_instance()
    print("Logger Singleton:", logger1 is logger2)
    
    # Database Connection Singleton
    db1 = Database.get_instance()
    db2 = Database.get_instance()
    print("Database Connection Singleton:", db1 is db2)
