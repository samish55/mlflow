import re

from mlflow.metrics.genai import EvaluationExample


def test_evaluation_example_str():
    example1 = str(
        EvaluationExample(
            input="This is an input",
            output="This is an output",
            score=5,
            justification="This is a justification",
            grading_context={"foo": "bar"},
        )
    )
    example1_expected = """
        Input:
        This is an input

        Output:
        This is an output

        Additional information used by the model:
        key: foo
        value:
        bar

        score: 5
        justification: This is a justification
        """
    assert re.sub(r"\s+", "", example1_expected) == re.sub(r"\s+", "", example1)

    example2 = str(
        EvaluationExample(
            input="This is an input", output="This is an output", score=5, justification="It works"
        )
    )
    example2_expected = """
        Input:
        This is an input

        Output:
        This is an output

        score: 5
        justification: It works
        """
    assert re.sub(r"\s+", "", example2_expected) == re.sub(r"\s+", "", example2)
