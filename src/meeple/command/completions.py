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
            print_info(
                'To install, add this to ~/.bashrc: [green]eval "$(_MEEPLE_COMPLETE=bash_source meeple)"[/green]'
            )
        case "zsh":
            print_info(
                'To install, add this to ~/.zshrc: [green]eval "$(_MEEPLE_COMPLETE=zsh_source meeple)"[/green]'
            )
        case "fish":
            print_info(
                "To install, run: [green]_MEEPLE_COMPLETE=fish_source meeple > ~/.config/fish/completions/meeple.fish[/green]"
            )
