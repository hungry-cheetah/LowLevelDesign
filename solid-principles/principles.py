# YAGNI - Always implement things when you actually need them, never when you just foresee that you might need them.
# DRY - Every piece of knowledge must have a single, unambiguous, authoritative representation within a system.
# KISS - It suggests that software should be designed to be easy to understand, modify, and extend, rather than complex and convoluted.

# S Single responsibility
# O classes should be open for extension, but closed for modification.
# L objects of superclass should be replaced with the objects of its subclass without affecting the correctness of the program.
# I clients should not be forced to depend upon methods they do not use....
# D high-level modules should not depend on low-level modules, both should depend on abstraction.

# SOLID principles help in designing maintainable, scalable, and flexible software. They improve code
#  readability, reduce coupling.



# coding across time - its not about you meeting the requirements of the clients now, its about the future engineers to 
# meet the future requirements.

# 3 major factors - 

# 1. Readability - easier to debug, change and write test cases for it. If its not readable,
# it becomes a black box and its the first thing that gets refacatored. Increases the cost of engineering.

# 2. Extensible

# 3. Reliable - Cost of fixing bugs at production is more. If you write code and it should just work.

# Important considerations and tradeoffs for data denormalization
# For normalizing data, one important consideration is if the data will be "read heavy" or "write heavy." 
# In a denormalized database, data is duplicated. So, every time data needs to be added or modified, several tables will need to be changed. This results in slower write operations.
# Therefore, the fundamental tradeoff is fast writes and slow reads with normalization versus slow writes and fast reads with denormalization.
