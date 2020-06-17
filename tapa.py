from tapas.tools import prompt_str


# Require from user to enter parameters in this function
def ask():
    prompt_str('executable_name', prompt_string='Executable name: ')


# Perform additional actions after generation in this function
def post_init():
    pass
