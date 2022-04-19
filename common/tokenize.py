from typing import List


def tokenize(document: str) -> List[str]:
    """Just split on whitespace"""
    return document.split()
