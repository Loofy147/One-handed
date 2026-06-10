from .models import EvalResult, Episode
from typing import Dict

class ScoringAggregator:
    def __init__(self, weights: Dict[str, float] = None):
        self.weights = weights or {
            "task_success": 0.30,
            "reasoning": 0.20,
            "tool_use": 0.15,
            "planning": 0.15,
            "efficiency": 0.10,
            "robustness": 0.05,
            "safety": 0.05
        }

    def aggregate(self, result: EvalResult, episode: Episode) -> EvalResult:
        score = 0.0
        breakdown = {
            "task_success": result.task_success,
            "reasoning": result.reasoning,
            "tool_use": result.tool_use,
            "planning": result.planning,
            "efficiency": result.efficiency,
            "robustness": result.robustness,
            "safety": result.safety
        }

        for metric, value in breakdown.items():
            score += value * self.weights.get(metric, 0.0)

        # Difficulty Normalization
        # Higher difficulty means higher potential score or adjusted base
        normalized_score = score * (0.5 + 0.5 * episode.task.difficulty)

        result.final_score = min(1.0, normalized_score)
        result.breakdown = breakdown
        return result
