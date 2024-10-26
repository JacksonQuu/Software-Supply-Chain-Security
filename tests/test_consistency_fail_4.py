import subprocess

def test_consistency():
    """
    Using wrong tree-size and root-hash
    """
    result = subprocess.run(
        ["python", "main.py", "--consistency",
         "--tree-id", "6691691",
         "--tree-size", "12345678",
         "--root-hash",
         "abcd0252423f2b41489c10c4b848b034bad90903be100a7c5877f4f98d6f5b6f"],
        capture_output=True,
        text=True
    )
    assert result.returncode == 1, "The program should throw an error, but it doesn't."

if __name__ == "__main__":
    test_consistency()
