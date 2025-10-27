display = []
guessed = {}
wrong_guesses = 0

def init_state(secret: str, max_tries: int) -> dict:
    return {
        "secret": secret,
        "display": ["_ " * len(secret)],
        "guessed": set[str],
        "wrong_guesses": int,
        "max_tries": max_tries
    }
    
def validate_guess(ch: str, guessed: set[str]) -> tuple[bool, str]:    
    if len(ch) == 1 and ch.isalpha:
        if ch in guessed:
            return False, "You already guessed this letter."
        else:
            return True, "Correct guess!"
    return False, "Incorrect input, please enter only one letter without spaces or numbers."
        
def apply_guess(state: dict, ch: str) -> bool:
    if ch in state:
        return True
    return False

def is_won(state: dict) -> bool:
    pass

def is_lost(state: dict) -> bool:
    pass

def render_display(state: dict) -> str:
    pass

def render_summary(state: dict) -> str:
    pass
    