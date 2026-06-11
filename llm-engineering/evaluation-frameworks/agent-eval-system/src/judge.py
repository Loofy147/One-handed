import json
import random

class LLMJudge:
    """
    A simulated LLM-as-Judge to provide nuanced evaluation.
    In a production environment, this would call a powerful model like GPT-4 or Claude.
    """
    def __init__(self, model_name="simulated-judge"):
        self.model_name = model_name

    def judge_reasoning(self, thoughts: str):
        # Heuristic simulation of LLM judging
        if not thoughts:
            return 0.0, "No reasoning provided."

        words = thoughts.split()
        if len(words) > 50:
            return 0.95, "Comprehensive and logical step-by-step reasoning."
        elif len(words) > 20:
            return 0.75, "Clear intent but lacks granular detail."
        else:
            return 0.4, "Reasoning is too brief to verify logic."

    def judge_success(self, final_output: str, expected_outcome: str):
        # Semantic similarity simulation
        if expected_outcome.lower() in final_output.lower():
            return 1.0, "The agent successfully achieved the target outcome."

        # Simulate partial credit
        common_words = set(expected_outcome.lower().split()) & set(final_output.lower().split())
        if len(common_words) > 0:
            score = min(0.8, len(common_words) / len(expected_outcome.split()))
            return score, f"Partial success based on semantic overlap ({score})."

        return 0.0, "The agent failed to meet the objective."

if __name__ == "__main__":
    judge = LLMJudge()
    print(judge.judge_reasoning("First I will search for the file, then I will read its content to extract the key information."))
    print(judge.judge_success("The result is 42", "42"))
