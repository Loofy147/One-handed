from typing import List, Dict
from .models import EvalResult, Episode

class MarkdownReporter:
    def generate_report(self, benchmark_results: List[Dict], fingerprint: Dict) -> str:
        lines = []
        lines.append("# Agent Evaluation Report")
        lines.append(f"## Agent Profile: {fingerprint.get('agent_id', 'Unknown')}")
        lines.append("")
        lines.append("### Behavioral Fingerprint")
        lines.append(f"- **Behavioral Bias**: {fingerprint.get('behavioral_bias')}")
        lines.append(f"- **Avg Steps/Task**: {fingerprint.get('avg_steps_per_task')}")
        lines.append(f"- **Thought/Action Ratio**: {fingerprint.get('thought_action_ratio')}")
        lines.append(f"- **Total Tokens**: {fingerprint.get('total_tokens_consumed')}")
        lines.append("")

        lines.append("### Task Breakdown")
        lines.append("| Task ID | Final Score | Success | Reasoning | Constraints | Efficiency |")
        lines.append("|---------|-------------|---------|-----------|-------------|------------|")

        for entry in benchmark_results:
            ep = entry['episode']
            res = entry['result']
            lines.append(f"| {ep.task.task_id} | {res.final_score:.2f} | {res.task_success:.2f} | {res.reasoning:.2f} | {res.constraints_satisfied:.2f} | {res.efficiency:.2f} |")

        lines.append("")
        avg_score = sum(r['result'].final_score for r in benchmark_results) / len(benchmark_results) if benchmark_results else 0
        lines.append(f"**Aggregate Benchmark Score: {avg_score:.2f}**")

        return "\n".join(lines)
