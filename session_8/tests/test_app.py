from typer.testing import CliRunner
from src.session_8.app import app

runner = CliRunner()

def test_triangle():
    result = runner.invoke(app, ["triangle", "10", "5"])
    assert result.exit_code == 0
    assert "25" in result.output

def test_square():
    result = runner.invoke(app, ["square", "4"])
    assert result.exit_code == 0
    assert "16" in result.output

def test_sum():
    result = runner.invoke(app, ["sum", "3", "5"])
    assert result.exit_code == 0
    assert "8" in result.output

def test_subtraction():
    result = runner.invoke(app, ["subtraction", "10", "4"])
    assert result.exit_code == 0
    assert "6" in result.output