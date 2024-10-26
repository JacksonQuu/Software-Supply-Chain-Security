import subprocess

def test_inclusion():
    result = subprocess.run(
        ["python", "main.py",
         "--inclusion", "128595953",
         "--artifact", "artifact.md"],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0, f"Test failed. Error message:\n{result.stdout}"

if __name__ == "__main__":
    test_inclusion()
