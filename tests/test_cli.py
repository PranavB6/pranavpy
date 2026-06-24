from typer.testing import CliRunner
from pranavpy.cli import app

runner = CliRunner()

def test_main():
    result = runner.invoke(app, ["--name", "Alice"])
    assert result.exit_code == 0
    assert "Hello Alice" in result.output

def test_missing_name():
    result = runner.invoke(app, [])
    assert result.exit_code != 0  # should fail without required arg