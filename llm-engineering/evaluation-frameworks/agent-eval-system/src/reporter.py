from typing import List, Dict
from .models import EvalResult, Episode, StepType

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

        lines.append("### Agent Trajectories (Visualization)")
        for entry in benchmark_results:
            ep = entry['episode']
            lines.append(f"#### Task: {ep.task.task_id}")
            lines.append("```mermaid")
            lines.append("graph TD")
            lines.append("  Start((Start)) --> S0")

            for i, step in enumerate(ep.steps):
                step_label = step.type.value.capitalize()
                if step.tool_name:
                    step_label += f": {step.tool_name}"

                # Sanitize content for mermaid
                content = step.content[:30].replace('"', "'").replace("\n", " ") + "..."
                lines.append(f"  S{i}[\"{step_label}<br/>{content}\"]")

                if i < len(ep.steps) - 1:
                    lines.append(f"  S{i} --> S{i+1}")
                else:
                    lines.append(f"  S{i} --> End((End))")

            lines.append("```")
            lines.append("")

        avg_score = sum(r['result'].final_score for r in benchmark_results) / len(benchmark_results) if benchmark_results else 0
        lines.append(f"**Aggregate Benchmark Score: {avg_score:.2f}**")

        return "\n".join(lines)
