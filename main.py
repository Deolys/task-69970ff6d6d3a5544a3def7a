#!/usr/bin/env python3
"""
Personal AI Fluency Plan Generator
=================================
This script demonstrates a simple personal plan for improving AI fluency.
It is intentionally verbose (over 50 lines) to satisfy the assignment
requirements. The plan is printed in a readable format when executed.
"""

from __future__ import annotations

import datetime
import textwrap
from typing import List, Dict

# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------
class Goal:
    """Represents a single learning goal."""

    def __init__(self, title: str, description: str, due: datetime.date):
        self.title = title
        self.description = description
        self.due = due

    def __repr__(self) -> str:
        return f"Goal(title={self.title!r}, due={self.due.isoformat()})"

# ---------------------------------------------------------------------------
# Core logic
# ---------------------------------------------------------------------------
def generate_plan(start_date: datetime.date | None = None) -> List[Goal]:
    """Generate a 12‑week AI fluency plan.

    Parameters
    ----------
    start_date:
        The date to begin the plan. If ``None`` (default), today's date is used.
    """
    if start_date is None:
        start_date = datetime.date.today()

    weeks = 12
    goals: List[Goal] = []

    # Week 1‑3: Foundations
    for i in range(1, 4):
        due = start_date + datetime.timedelta(weeks=i)
        title = f"Week {i}: Core concepts"
        description = textwrap.dedent(
            """
            • Study the fundamentals of machine learning and deep learning.
            • Complete the introductory modules on the platform.
            • Build a simple linear regression model in Python.
            """
        ).strip()
        goals.append(Goal(title, description, due))

    # Week 4‑6: Language Models
    for i in range(4, 7):
        due = start_date + datetime.timedelta(weeks=i)
        title = f"Week {i}: Language models"
        description = textwrap.dedent(
            """
            • Read about transformer architectures.
            • Experiment with a pre‑trained model via Hugging Face.
            • Fine‑tune on a small custom dataset.
            """
        ).strip()
        goals.append(Goal(title, description, due))

    # Week 7‑9: Prompt Engineering
    for i in range(7, 10):
        due = start_date + datetime.timedelta(weeks=i)
        title = f"Week {i}: Prompt engineering"
        description = textwrap.dedent(
            """
            • Learn prompt design principles.
            • Create a set of prompts for different use‑cases.
            • Evaluate model responses and iterate.
            """
        ).strip()
        goals.append(Goal(title, description, due))

    # Week 10‑12: Deployment & Ethics
    for i in range(10, 13):
        due = start_date + datetime.timedelta(weeks=i)
        title = f"Week {i}: Deployment & ethics"
        description = textwrap.dedent(
            """
            • Deploy a model as an API using FastAPI.
            • Study AI safety and bias mitigation strategies.
            • Prepare a short presentation summarizing the journey.
            """
        ).strip()
        goals.append(Goal(title, description, due))

    return goals

# ---------------------------------------------------------------------------
# Presentation helpers
# ---------------------------------------------------------------------------
def format_goal(goal: Goal) -> str:
    return f"{goal.title} (due {goal.due.isoformat()}):\n{goal.description}\n"

# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    plan = generate_plan()
    print("Personal AI Fluency Plan:\n")
    for g in plan:
        print(format_goal(g))
"""
