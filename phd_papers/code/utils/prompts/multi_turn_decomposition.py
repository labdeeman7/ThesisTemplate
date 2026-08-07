from .types import MultiTurnDecompositionPrompt

PROMPT = MultiTurnDecompositionPrompt(
    name="multi_turn_decomposition",
    system="You are a surgical scene understanding assistant. Return valid JSON only.",
    instrument_user=(
        "For each labelled instrument instance in this image, identify the instrument type. "
        "Return JSON only."
    ),
    action_user=(
        "For each labelled instrument instance, identify the action being performed. "
        "Return JSON only."
    ),
    target_user=(
        "For each labelled instrument instance, identify the target being acted upon. "
        "Return JSON only."
    ),
    final_user=(
        "For each labelled instrument instance, predict the final instrument-action-target triplet. "
        "Return JSON only."
    ),
)
