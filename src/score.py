from dataclasses import dataclass

@dataclass
class EvaluationCase:
    expected: str
    actual: str

def exact_match(case: EvaluationCase) -> float:
    return float(case.expected.strip().lower() == case.actual.strip().lower())

def aggregate(cases: list[EvaluationCase]) -> float:
    if not cases:
        return 0.0
    return sum(exact_match(c) for c in cases) / len(cases)
