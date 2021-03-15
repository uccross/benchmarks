import json
import os

from ..tests._asserts import assert_cli, get_cli_output


this_dir = os.path.abspath(os.path.dirname(__file__))
benchmarks_file = os.path.join(this_dir, "..", "..", "benchmarks.json")


def test_list_cli():
    command = ["conbench", "list"]

    with open(benchmarks_file) as f:
        benchmarks = json.dumps(json.load(f), indent=2)

    try:
        assert_cli(command, benchmarks)
    except AssertionError:
        output = get_cli_output(command)
        with open(benchmarks_file, "w") as f:
            f.write(output)
            f.write("\n")
            msg = (
                "Warning benchmarks.json was re-generated. "
                "Confirm the diff and commit it. "
                "This test should pass if you now run it again. "
            )
        assert False, msg
