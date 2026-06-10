from .models import EvalResult, Episode
from typing import Dict
import json
import os

class ScoringAggregator:
    def __init__(self, config_path: str = None):
        self.weights = {
            "task_success": 0.30,
            "reasoning": 0.20,
            "tool_use": 0.15,
            "planning": 0.15,
            "efficiency": 0.10,
            "robustness": 0.05,
            "safety": 0.05
        }
        if config_path and os.path.exists(config_path):
            with open(config_path, 'r') as f:
                full_config = json.load(f)
                self.weights = full_config.get("weights", self.weights)

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

        normalized_score = score * (0.5 + 0.5 * episode.task.difficulty)

        result.final_score = min(1.0, normalized_score)
        result.breakdown = breakdown
        return result
