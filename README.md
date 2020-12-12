# SimplePythonProjects
I am attempting to write 12 Python projects in order to learn Python. 

Project 1: Madlibs.py Using string concatenation
In a traditional madlib you will have a bunch of blanks in a paragraph and you would have someone 
fill out those blanks and then read the paragraph out loud with the words that they chose in those blanks.
We are gonig to recreate this project in Python using string concatenation.
Concatenation means joining strings together end-to-end to create a new string. To concatenate strings, we use the + operator. 
Keep in mind that when we work with numbers, + will be an operator for addition, but when used with strings it is a joining operator.
String Concatenation
String concatenation means add strings together.
Use the + character to add a variable to another variable

  coder = "foday"
  a. writing the variable with a stored name and outputing it to the terminal along with a concatenated text ex: print("subscribe to " + coder)
  b. using {} to output a string ex print("subscribe to {}".format(coder))
  c. Using 'f' string to format the string in the {} ex" print(f"subscribe to {coder}")

2. Project 2: User Guess The Number
The computer has a secret number and the user has to guess what that number is 
  setp 1: the computer has to generate a secret number for the user to guess 
  and in order to do that "random" has to be imported into the program.
  
  ABOUT RANDOM 
  random — Generate pseudo-random numbers
Source code: Lib/random.py

This module implements pseudo-random number generators for various distributions.

For integers, there is uniform selection from a range. For sequences, there is uniform selection of a random element, a function to generate a random permutation of a list in-place, and a function for random sampling without replacement.

On the real line, there are functions to compute uniform, normal (Gaussian), lognormal, negative exponential, gamma, and beta distributions. For generating distributions of angles, the von Mises distribution is available.

Almost all module functions depend on the basic function random(), which generates a random float uniformly in the semi-open range [0.0, 1.0). Python uses the Mersenne Twister as the core generator. It produces 53-bit precision floats and has a period of 2**19937-1. The underlying implementation in C is both fast and threadsafe. The Mersenne Twister is one of the most extensively tested random number generators in existence. However, being completely deterministic, it is not suitable for all purposes, and is completely unsuitable for cryptographic purposes.

The functions supplied by this module are actually bound methods of a hidden instance of the random.Random class. You can instantiate your own instances of Random to get generators that don’t share state.

Class Random can also be subclassed if you want to use a different basic generator of your own devising: in that case, override the random(), seed(), getstate(), and setstate() methods. Optionally, a new generator can supply a getrandbits() method — this allows randrange() to produce selections over an arbitrarily large range.

The random module also provides the SystemRandom class which uses the system function os.urandom() to generate random numbers from sources provided by the operating system.

ABOUT RANDIT 
random.randint(a, b)¶
Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1).
