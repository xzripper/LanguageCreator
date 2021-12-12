import subprocess
import sys
import os


subprocess = subprocess
sys = sys
os = os

def output(command: str, remlstc: bool) -> str:
    """
    Get output from console command.
    If remlstc is True, it's return an output without a useless newline.

    :param command: The command.
    :param remlstc: Remove last character from output.
    """
    return subprocess.check_output(command, shell=True, encoding='cp866')[:-1] if remlstc else subprocess.check_output(command, shell=True, encoding='cp866')
