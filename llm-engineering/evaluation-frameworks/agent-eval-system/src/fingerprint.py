from typing import List, Dict
from .models import Episode, StepType

class AgentFingerprinter:
    def __init__(self):
        pass

    def generate_fingerprint(self, episodes: List[Episode]) -> Dict:
        if not episodes:
            return {}

        total_steps = 0
        total_thoughts = 0
        total_actions = 0
        total_tokens = 0

        for ep in episodes:
            total_steps += len(ep.steps)
            total_thoughts += sum(1 for s in ep.steps if s.type == StepType.THOUGHT)
            total_actions += sum(1 for s in ep.steps if s.type == StepType.ACTION)
            total_tokens += ep.tokens_used

        avg_steps = total_steps / len(episodes)
        thought_action_ratio = total_thoughts / max(1, total_actions)

        # Categorization
        bias = "balanced"
        if thought_action_ratio > 2.0:
            bias = "thought-heavy (deliberative)"
        elif thought_action_ratio < 0.5:
            bias = "action-heavy (impulsive)"

        return {
            "agent_id": episodes[0].agent_id,
            "avg_steps_per_task": round(avg_steps, 2),
            "thought_action_ratio": round(thought_action_ratio, 2),
            "behavioral_bias": bias,
            "total_tokens_consumed": total_tokens
        }
