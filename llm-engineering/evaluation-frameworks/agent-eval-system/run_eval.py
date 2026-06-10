import sys
import os
from src.evaluator import EvaluationEngine
from src.aggregator import ScoringAggregator
from src.runner import BenchmarkRunner
from src.fingerprint import AgentFingerprinter
from src.reporter import MarkdownReporter

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(base_dir, "data")
    config_path = os.path.join(base_dir, "config.json")

    # Initialize components
    evaluator = EvaluationEngine(config_path=config_path)
    aggregator = ScoringAggregator(config_path=config_path)
    runner = BenchmarkRunner(evaluator, aggregator)
    fingerprinter = AgentFingerprinter()
    reporter = MarkdownReporter()

    # Run benchmark
    print(f"Running benchmark on episodes in {data_dir}...")
    results = runner.run_benchmark(data_dir)

    if not results:
        print("No episodes found to evaluate.")
        return

    # Generate fingerprint
    episodes = [r['episode'] for r in results]
    fingerprint = fingerprinter.generate_fingerprint(episodes)

    # Generate report
    report = reporter.generate_report(results, fingerprint)

    # Save report
    report_path = os.path.join(base_dir, "evaluation_report.md")
    with open(report_path, "w") as f:
        f.write(report)

    print(f"Evaluation complete! Report saved to {report_path}")
    print("\n--- Summary ---")
    print(f"Agent: {fingerprint['agent_id']}")
    print(f"Bias: {fingerprint['behavioral_bias']}")
    print(f"Avg Score: {sum(r['result'].final_score for r in results) / len(results):.2f}")

if __name__ == "__main__":
    main()
