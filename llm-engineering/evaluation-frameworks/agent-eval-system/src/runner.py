import json
import os
from typing import List, Dict
from .models import Episode, Task, Step, StepType, EvalResult
from .evaluator import EvaluationEngine
from .aggregator import ScoringAggregator

class BenchmarkRunner:
    def __init__(self, evaluator: EvaluationEngine, aggregator: ScoringAggregator):
        self.evaluator = evaluator
        self.aggregator = aggregator

    def load_episode_from_json(self, file_path: str) -> Episode:
        with open(file_path, 'r') as f:
            data = json.load(f)

        task_data = data['task']
        task = Task(
            task_id=task_data['task_id'],
            prompt=task_data['prompt'],
            expected_outcome=task_data['expected_outcome'],
            difficulty=task_data.get('difficulty', 1.0)
        )

        steps = []
        for s in data.get('steps', []):
            steps.append(Step(
                type=StepType(s['type']),
                content=s['content'],
                tool_name=s.get('tool_name'),
                tool_input=s.get('tool_input'),
                tool_output=s.get('tool_output'),
                timestamp=s.get('timestamp', 0.0)
            ))

        return Episode(
            episode_id=data['episode_id'],
            agent_id=data['agent_id'],
            task=task,
            steps=steps,
            final_output=data.get('final_output', ""),
            tokens_used=data.get('tokens_used', 0),
            start_time=data.get('start_time', 0.0),
            end_time=data.get('end_time', 0.0)
        )

    def run_benchmark(self, data_dir: str) -> List[Dict]:
        results = []
        for filename in os.listdir(data_dir):
            if filename.endswith('.json'):
                path = os.path.join(data_dir, filename)
                try:
                    episode = self.load_episode_from_json(path)
                    raw_result = self.evaluator.evaluate_episode(episode)
                    final_result = self.aggregator.aggregate(raw_result, episode)
                    results.append({
                        "episode": episode,
                        "result": final_result
                    })
                except Exception as e:
                    print(f"Error processing {filename}: {e}")
        return results
