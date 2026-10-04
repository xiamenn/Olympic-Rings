# print_me_first.py
def print_me_first(name, program_name=""):
    """
    Function name: print_me_first
    Function description: Prints the programmer's name and program information
    @param name: The programmer's name
    @param program_name: The name of the program
    @return: A string with the programmer's name and program information
    """
    info = f"Programmer: {name}\n"
    if program_name:
        info += f"Program: {program_name}\n"
    info += "CNET-142 - Introduction to Python"
    return info