from typing import List

from rich.prompt import Confirm, Prompt


def bool_input(prompt: str) -> bool:
    """Prompt user for yes/no boolean input.
    Returns True if user response is 'y'/'Y' and False if user reponse 'n'/'N'. Otherwise, reprompt.
    Args:
        prompt (str): Prompt to display.
    Returns:
        bool: User boolean response.
    """
    return Confirm.ask(prompt)


def choice_input(prompt: str, choices: List[str]):
    """Prompt user for to select one of the provided choices.
    Returns the selected choice. Otherwise, reprompt.
    Args:
        prompt (str): Prompt to display.
    Returns:
        str: User choice.
    """
    return Prompt.ask(prompt, choices=choices)
