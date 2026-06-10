import pytest
import sys
import os

# Add the project src to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../llm-engineering/evaluation-frameworks/agent-eval-system')))

from src.models import Task, Episode, Step, StepType
from src.evaluator import EvaluationEngine
from src.aggregator import ScoringAggregator
from src.runner import BenchmarkRunner
from src.fingerprint import AgentFingerprinter

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
        agent_id="jules-agent",
        task=task,
        final_output="This was a success",
        steps=[Step(type=StepType.THOUGHT, content="thinking")]
    )
    result = evaluator.evaluate_episode(episode)
    assert result.task_success == 1.0

def test_efficiency_metrics(evaluator):
    task = Task(task_id="T1", prompt="test", expected_outcome="success")
    episode = Episode(
        episode_id="E1",
        agent_id="jules-agent",
        task=task,
        final_output="success",
        steps=[Step(type=StepType.THOUGHT, content="thinking")] * 10,
        tokens_used=5000,
        start_time=0.0,
        end_time=100.0
    )
    result = evaluator.evaluate_episode(episode)
    assert result.efficiency < 1.0

def test_benchmark_runner_loading():
    evaluator = EvaluationEngine()
    aggregator = ScoringAggregator()
    runner = BenchmarkRunner(evaluator, aggregator)

    # Path to real data for test
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../llm-engineering/evaluation-frameworks/agent-eval-system'))
    data_dir = os.path.join(base_dir, "data")

    results = runner.run_benchmark(data_dir)
    assert len(results) >= 4
    assert all('episode' in r and 'result' in r for r in results)

def test_fingerprint_logic():
    fingerprinter = AgentFingerprinter()
    task = Task(task_id="T1", prompt="test", expected_outcome="success")

    # Thought-heavy episode
    ep1 = Episode(
        episode_id="E1", agent_id="jules-agent", task=task,
        steps=[
            Step(type=StepType.THOUGHT, content="T1"),
            Step(type=StepType.THOUGHT, content="T2"),
            Step(type=StepType.THOUGHT, content="T3"),
            Step(type=StepType.ACTION, content="jules-agent")
        ]
    )

    # Action-heavy episode
    ep2 = Episode(
        episode_id="E2", agent_id="jules-agent", task=task,
        steps=[
            Step(type=StepType.ACTION, content="jules-agent"),
            Step(type=StepType.ACTION, content="A2"),
            Step(type=StepType.ACTION, content="A3")
        ]
    )

    fp1 = fingerprinter.generate_fingerprint([ep1])
    assert fp1['behavioral_bias'] == "thought-heavy (deliberative)"

    fp2 = fingerprinter.generate_fingerprint([ep2])
    assert fp2['behavioral_bias'] == "action-heavy (impulsive)"

def test_config_loading():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../llm-engineering/evaluation-frameworks/agent-eval-system'))
    config_path = os.path.join(base_dir, "config.json")

    evaluator = EvaluationEngine(config_path=config_path)
    aggregator = ScoringAggregator(config_path=config_path)

    assert aggregator.weights['task_success'] == 0.30
    assert evaluator.config['baselines']['ideal_steps'] == 5
