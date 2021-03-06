from pathlib import Path
from subprocess import CalledProcessError

import pytest


def idfn(options):
    return "-and-".join(flag.strip("-") for flag in options if flag.startswith("--"))


@pytest.mark.parametrize(
    "options",
    [
        ["--exclude", "excluded.*"],
        ["--include", "included.*"],
        ["--exclude-dir", "excluded"],
        ["--include-dir", "included"],
        ["--include-dir", "included", "--exclude", "excluded.*"],
        ["--exclude-dir", "excluded", "--include", "included.*"],
        ["--exclude", "excluded.*", "--exclude", "included.*"],
        ["--exclude-dir", "excluded", "--exclude-dir", "included"],
        ["--include", "excluded.*", "--include", "included.*"],
        ["--include-dir", "excluded", "--include-dir", "included"],
    ],
    ids=idfn,
)
def test_exclude_include(run_semgrep_in_tmp, snapshot, options):
    snapshot.assert_match(
        run_semgrep_in_tmp(
            "rules/eqeq.yaml", options=options, target_name="exclude_include",
        ),
        "results.json",
    )
