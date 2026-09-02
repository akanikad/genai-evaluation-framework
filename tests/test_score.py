from src.score import EvaluationCase, aggregate

def test_aggregate():
    cases = [
        EvaluationCase("approved", "approved"),
        EvaluationCase("review", "wrong"),
    ]
    assert aggregate(cases) == 0.5
