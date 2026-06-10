import sys
import os
import json
from src.models import Task, Episode, Step, StepType
from src.evaluator import EvaluationEngine
from src.aggregator import ScoringAggregator

def main():
    # Setup a sample episode with performance metrics
    task = Task(
        task_id="T1",
        prompt="Calculate 123 * 456 and verify the result.",
        expected_outcome="56088",
        difficulty=1.5
    )

    steps = [
        Step(type=StepType.THOUGHT, content="First, I will multiply 123 by 456. Next, I will return the result."),
        Step(type=StepType.ACTION, content="using calculator", tool_name="calculator", tool_input={"expr": "123 * 456"}, tool_output="56088"),
        Step(type=StepType.FINAL_ANSWER, content="The result of 123 * 456 is 56088.")
    ]

    episode = Episode(
        episode_id="E1",
        agent_id="test_agent",
        task=task,
        steps=steps,
        final_output="The result of 123 * 456 is 56088.",
        tokens_used=500,
        start_time=0.0,
        end_time=5.0
    )

    # Run evaluation
    evaluator = EvaluationEngine()
    aggregator = ScoringAggregator()

    raw_result = evaluator.evaluate_episode(episode)
    final_result = aggregator.aggregate(raw_result, episode)

    # Output results
    print(f"Agent ID: {episode.agent_id}")
    print(f"Task ID: {episode.task.task_id}")
    print(f"Final Score: {final_result.final_score:.2f}")
    print("\nBreakdown:")
    for metric, val in final_result.breakdown.items():
        print(f"  - {metric}: {val:.2f}")

if __name__ == "__main__":
    main()
