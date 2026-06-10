# Agent Evaluation & Optimization Guide

This guide explains how to use the evaluation system to measure and improve AI agent performance.

## Using Constraints for Optimization

Constraints are powerful tools for shaping agent behavior. By defining strict constraints in the `Task` model, you can evaluate an agent's ability to follow complex instructions.

### Example Constraint Definition
```python
task = Task(
    task_id="T-200",
    prompt="Explain RAG in under 100 words without using the word 'database'.",
    expected_outcome="Accurate explanation of RAG",
    constraints=["under 100 words", "no 'database'"]
)
```

The system will automatically score the agent based on how many of these keywords/phrases appear (or don't appear) in the final output.

## Improving Your Score

1. **Reasoning**: Ensure your agent uses `THOUGHT` steps. The evaluator looks for at least 3 thought steps for a perfect reasoning score.
2. **Planning**: Use keywords like "first", "next", "then", and "finally" in your thoughts to signal a clear plan.
3. **Efficiency**: Keep the step count close to the baseline (default: 5) and minimize token usage.
4. **Robustness**: If a tool fails, ensure the agent identifies the error and tries a different approach or explains the limitation.

## Extending the Evaluator

You can add custom heuristic checks in `src/evaluator.py`. For example, you might add a check for:
- Tone of voice (formal vs. informal).
- JSON schema validity for structured outputs.
- Specific API usage patterns.

## Weighted Scoring

The final score is a weighted average. You can customize these weights in `config.json` to prioritize different aspects of performance (e.g., making safety more important for customer-facing agents).
