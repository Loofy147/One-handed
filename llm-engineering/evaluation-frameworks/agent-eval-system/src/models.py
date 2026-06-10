from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
from enum import Enum

class StepType(Enum):
    THOUGHT = "thought"
    ACTION = "action"
    OBSERVATION = "observation"
    FINAL_ANSWER = "final_answer"

@dataclass
class Step:
    type: StepType
    content: str
    tool_name: Optional[str] = None
    tool_input: Optional[Dict[str, Any]] = None
    tool_output: Optional[Any] = None
    timestamp: float = 0.0

@dataclass
class Task:
    task_id: str
    prompt: str
    expected_outcome: str
    difficulty: float = 1.0
    constraints: List[str] = field(default_factory=list)

@dataclass
class Episode:
    episode_id: str
    agent_id: str
    task: Task
    steps: List[Step] = field(default_factory=list)
    final_output: str = ""
    tokens_used: int = 0
    start_time: float = 0.0
    end_time: float = 0.0

@dataclass
class EvalResult:
    task_success: float = 0.0
    reasoning: float = 0.0
    tool_use: float = 0.0
    planning: float = 0.0
    efficiency: float = 0.0
    robustness: float = 0.0
    safety: float = 0.0
    constraints_satisfied: float = 0.0
    final_score: float = 0.0
    breakdown: Dict[str, float] = field(default_factory=dict)
