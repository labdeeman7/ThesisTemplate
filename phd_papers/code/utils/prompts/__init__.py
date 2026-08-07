from .baseline import PROMPT as BASELINE
from .constraint_100 import PROMPT as CONSTRAINT_100
from .reasoning import PROMPT as REASONING
from .cot_reasoning_target import PROMPT as COT_REASONING_TARGET
from .cot_reasoning_old import PROMPT as COT_REASONING_OLD
from .video_baseline import PROMPT as VIDEO_BASELINE
from .baseline_endovit_tip_prior import PROMPT as BASELINE_ENDOVIT_TIP_PRIOR
from .multi_turn_decomposition import PROMPT as MULTI_TURN_DECOMPOSITION

PROMPT_REGISTRY = {
    "baseline": BASELINE,
    "constraint_100": CONSTRAINT_100,
    "reasoning": REASONING,
    "cot_reasoning_target": COT_REASONING_TARGET,
    "cot_reasoning_old": COT_REASONING_OLD,
    "video_baseline": VIDEO_BASELINE,
    "baseline_endovit_tip_prior": BASELINE_ENDOVIT_TIP_PRIOR,
    "multi_turn_decomposition": MULTI_TURN_DECOMPOSITION,
}

def get_prompt(name: str):
    try:
        return PROMPT_REGISTRY[name]
    except KeyError as e:
        raise KeyError(
            f"Unknown prompt '{name}'. Available: {list(PROMPT_REGISTRY.keys())}"
        ) from e
