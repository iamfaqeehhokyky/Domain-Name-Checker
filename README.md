# Domain Name Checker

A command-line tool to check the availability of domain names

In this implementation, we define a `DomainChecker` class that takes a domain name as input and has a `is_available` method that uses the `whois` library to check if the domain name is available or not.

The `main` function prompts the user to enter a domain name, creates a `DomainChecker` instance with the user's input, and prints whether the domain name is available or not.

To run the program, simply save the code to a file (e.g. `domain_checker.py`) and run it in the command-line using the python command:

```py
python domain_checker.py
```
