#!/usr/bin/env python3
import sys
import time
import subprocess
import os

# Add the current directory to the path so we can import mock_helpers
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

def run_fuzz_tests_for_duration():
    """
    Run fuzz tests continuously for a specified duration.
    
    Uses TEST_DURATION environment variable (minutes) to determine how long to run.
    """
    # Get the duration from environment or use default
    duration_min = int(os.environ.get('TEST_DURATION', '10'))
    end_time = time.time() + (duration_min * 60)
    
    print(f"Running fuzz tests for {duration_min} minutes...")
    
    # Determine the path to run_tests.py based on where this script is executed from
    current_dir = os.path.dirname(os.path.abspath(__file__))
    this_file_name = os.path.basename(__file__)
    
    if this_file_name in os.listdir('.'):
        # We're in the test directory
        runner_path = 'run_tests.py'
    elif 'test' in os.listdir('.') and this_file_name in os.listdir('./test'):
        # We're in the package root directory
        runner_path = 'test/run_tests.py'
    else:
        # Use absolute path as fallback
        runner_path = os.path.join(current_dir, 'run_tests.py')
    
    print(f"Using test runner at path: {runner_path}")
    
    # Run continuous tests until the time expires
    count = 0
    while time.time() < end_time:
        print(f"Running test iteration {count+1}...")
        # Use our custom test runner which includes mocks
        result = subprocess.call(['python', runner_path])
        if result != 0:
            print(f"Test iteration {count+1} failed with exit code {result}")
            sys.exit(result)
        
        count += 1
        remaining = int((end_time - time.time())/60)
        print(f"Completed {count} iterations. Time remaining: {remaining} minutes")
    
    print(f"Completed {count} total test iterations")

if __name__ == "__main__":
    run_fuzz_tests_for_duration()
