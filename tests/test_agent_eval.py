import pytest
import sys
import os

# Add the project src to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../llm-engineering/evaluation-frameworks/agent-eval-system')))

from src.models import Task, Episode, Step, StepType
from src.evaluator import EvaluationEngine
from src.aggregator import ScoringAggregator

@pytest.fixture
def evaluator():
    return EvaluationEngine()

@pytest.fixture
def aggregator():
    return ScoringAggregator()

def test_evaluation_success(evaluator):
    task = Task(task_id="T1", prompt="test", expected_outcome="success")
    episode = Episode(
        episode_id="E1",
        agent_id="A1",
        task=task,
        final_output="This was a success",
        steps=[Step(type=StepType.THOUGHT, content="thinking")]
    )
    result = evaluator.evaluate_episode(episode)
    assert result.task_success == 1.0

def test_evaluation_failure(evaluator):
    task = Task(task_id="T1", prompt="test", expected_outcome="success")
    episode = Episode(
        episode_id="E1",
        agent_id="A1",
        task=task,
        final_output="failure",
        steps=[Step(type=StepType.THOUGHT, content="thinking")]
    )
    result = evaluator.evaluate_episode(episode)
    assert result.task_success == 0.0

def test_efficiency_metrics(evaluator):
    task = Task(task_id="T1", prompt="test", expected_outcome="success")
    # Low efficiency episode
    episode = Episode(
        episode_id="E1",
        agent_id="A1",
        task=task,
        final_output="success",
        steps=[Step(type=StepType.THOUGHT, content="thinking")] * 10,
        tokens_used=5000,
        start_time=0.0,
        end_time=100.0
    )
    result = evaluator.evaluate_episode(episode)
    # Efficiency should be less than 1.0
    assert result.efficiency < 1.0

def test_robustness_recovery(evaluator):
    task = Task(task_id="T1", prompt="test", expected_outcome="success")
    episode = Episode(
        episode_id="E1",
        agent_id="A1",
        task=task,
        final_output="success",
        steps=[
            Step(type=StepType.ACTION, content="call", tool_name="tool", tool_output="Error: timeout"),
            Step(type=StepType.ACTION, content="retry", tool_name="tool", tool_output="success")
        ]
    )
    result = evaluator.evaluate_episode(episode)
    # Succeeded despite error
    assert result.robustness == 1.0

def test_scoring_aggregation(evaluator, aggregator):
    task = Task(task_id="T1", prompt="test", expected_outcome="success", difficulty=1.0)
    episode = Episode(
        episode_id="E1",
        agent_id="A1",
        task=task,
        final_output="success",
        steps=[Step(type=StepType.THOUGHT, content="thinking")]
    )
    raw_result = evaluator.evaluate_episode(episode)
    final_result = aggregator.aggregate(raw_result, episode)
    assert 0.0 <= final_result.final_score <= 1.0
