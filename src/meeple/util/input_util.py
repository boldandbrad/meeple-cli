from rich.prompt import Confirm


def bool_input(prompt: str) -> bool:
    """Prompt user for yes/no boolean input.
    Returns True if user response is 'y'/'Y' and False if user reponse 'n'/'N'. Otherwise, reprompt.
    Args:
        prompt (str): Prompt to display.
    Returns:
        bool: User boolean response.
    """
    return Confirm.ask(prompt)
