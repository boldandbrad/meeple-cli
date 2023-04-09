import click

from meeple.util.output_util import print_info

SHELLS = ["bash", "zsh", "fish"]


@click.command()
@click.argument("shell", type=click.Choice(SHELLS, case_sensitive=False))
@click.help_option("-h", "--help")
def completions(shell: str) -> None:
    """Setup meeple shell completions.

    - SHELL is the shell for which to setup completions.
    """
    match shell.lower():
        case "bash":
            print_info("Add this to ~/.bashrc:")
            print('\teval "$(_MEEPLE_COMPLETE=bash_source meeple)"')
        case "zsh":
            print_info("Add this to ~/.zshrc:")
            print('\teval "$(_MEEPLE_COMPLETE=zsh_source meeple)"')
        case "fish":
            print_info(
                "Save the following script to ~/.config/fish/completions/meeple.fish:"
            )
            print(
                "\t_MEEPLE_COMPLETE=fish_source meeple > ~/.config/fish/completions/meeple.fish"
            )
