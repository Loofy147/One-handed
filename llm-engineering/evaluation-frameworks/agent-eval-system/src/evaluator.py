from .models import Episode, EvalResult, StepType
import re
import json
import os

class EvaluationEngine:
    def __init__(self, config_path: str = None):
        self.config = {
            "baselines": {
                "ideal_steps": 5,
                "token_limit": 1000,
                "time_limit_seconds": 30
            }
        }
        if config_path and os.path.exists(config_path):
            with open(config_path, 'r') as f:
                full_config = json.load(f)
                self.config["baselines"] = full_config.get("baselines", self.config["baselines"])

    def evaluate_episode(self, episode: Episode) -> EvalResult:
        result = EvalResult()

        # 1. Task Success
        result.task_success = self._evaluate_success(episode)

        # 2. Reasoning Quality
        result.reasoning = self._evaluate_reasoning(episode)

        # 3. Tool Use Efficiency
        result.tool_use = self._evaluate_tool_use(episode)

        # 4. Planning Quality
        result.planning = self._evaluate_planning(episode)

        # 5. Efficiency (Steps, Tokens, Time)
        result.efficiency = self._evaluate_efficiency(episode)

        # 6. Robustness (Error Recovery)
        result.robustness = self._evaluate_robustness(episode)

        # 7. Safety
        result.safety = 1.0 # Default

        return result

    def _evaluate_success(self, episode: Episode) -> float:
        if not episode.final_output:
            return 0.0
        if episode.task.expected_outcome.lower() in episode.final_output.lower():
            return 1.0
        return 0.0

    def _evaluate_reasoning(self, episode: Episode) -> float:
        thought_steps = [s for s in episode.steps if s.type == StepType.THOUGHT]
        if not thought_steps:
            return 0.0
        return min(1.0, len(thought_steps) / 3.0)

    def _evaluate_tool_use(self, episode: Episode) -> float:
        action_steps = [s for s in episode.steps if s.type == StepType.ACTION]
        if not action_steps:
            return 1.0

        successful_calls = sum(1 for s in action_steps if s.tool_output is not None and str(s.tool_output).lower() != "error")
        return successful_calls / len(action_steps)

    def _evaluate_planning(self, episode: Episode) -> float:
        thoughts = " ".join([s.content for s in episode.steps if s.type == StepType.THOUGHT])
        if re.search(r'\b(step|first|next|then|finally)\b', thoughts, re.I):
            return 1.0
        return 0.5

    def _evaluate_efficiency(self, episode: Episode) -> float:
        baselines = self.config["baselines"]

        # Step Efficiency
        num_steps = len(episode.steps)
        step_eff = min(1.0, baselines["ideal_steps"] / num_steps) if num_steps > 0 else 0.0

        # Token Efficiency
        success = self._evaluate_success(episode)
        if success == 0 or episode.tokens_used == 0:
            token_eff = 0.0
        else:
            token_eff = min(1.0, baselines["token_limit"] / episode.tokens_used)

        # Time Efficiency
        duration = episode.end_time - episode.start_time
        if duration <= 0:
            time_eff = 1.0
        else:
            time_eff = min(1.0, baselines["time_limit_seconds"] / duration)

        return (step_eff + token_eff + time_eff) / 3.0

    def _evaluate_robustness(self, episode: Episode) -> float:
        action_steps = [s for s in episode.steps if s.type == StepType.ACTION]
        errors = [i for i, s in enumerate(action_steps) if s.tool_output is not None and "error" in str(s.tool_output).lower()]

        if not errors:
            return 1.0

        success = self._evaluate_success(episode)
        return success
