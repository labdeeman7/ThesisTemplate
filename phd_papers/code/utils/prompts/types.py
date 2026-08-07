from dataclasses import dataclass

@dataclass
class Prompt:
    name: str
    system: str
    user: str


@dataclass
class MultiTurnDecompositionPrompt:
    """Prompt text for decomposing triplet prediction across multiple turns."""

    name: str
    system: str
    instrument_user: str
    action_user: str
    target_user: str
    final_user: str
