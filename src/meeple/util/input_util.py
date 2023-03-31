def bool_input(prompt: str) -> bool:
    """Prompt user for yes/no boolean input.
    Returns True if user response is 'y'/'Y'/'yes'/'YES'. Otherwise, False.
    Args:
        prompt (str): Prompt to display.
    Returns:
        bool: User boolean response.
    """
    response = input(f"{prompt} (y/N) ")
    return response.lower() in ("y", "yes")
