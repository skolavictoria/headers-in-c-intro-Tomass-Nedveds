import subprocess
import os
import pytest

# Define task directories and expected executables
tasks = {
    "Task1": {
        "files": ["greetings.c", "main.c"],
        "executable": "hello",
        "expected_output": "Hello, World!\n"
    },
    "Task2": {
        "files": ["math_operations.c", "print_operations.c", "main.c"],
        "executable": "math_printer",
        "expected_output": "Result: 15\n"  # Using add(10, 5) as per main.c in Task 2
    },
    "Task3": {
        "files": ["array_utils.c", "utils.c", "main.c"],
        "executable": "array_util_demo",
        "expected_output": "3 3 3 3 3 \n"
    }
}

@pytest.mark.parametrize("task, details", tasks.items())
def test_tasks(task, details):
    # Prepare the command to compile the C files
    compile_command = ["gcc"] + details["files"] + ["-o", details["executable"]]
    task_dir = f"./{task}"

    # Change directory to the task directory
    original_dir = os.getcwd()
    os.chdir(task_dir)
    
    # Compile the files
    compilation_result = subprocess.run(compile_command, capture_output=True, text=True)
    assert compilation_result.returncode == 0, f"Compilation failed for {task}: {compilation_result.stderr}"

    # Run the executable if compilation was successful
    run_result = subprocess.run(f"./{details['executable']}", capture_output=True, text=True)
    assert run_result.returncode == 0, f"Execution failed for {task}: {run_result.stderr}"

    # Check the output
    assert run_result.stdout == details["expected_output"], f"Output mismatch for {task}: {run_result.stdout}"

    # Clean up by removing the executable and return to the original directory
    os.remove(details["executable"])
    os.chdir(original_dir)
