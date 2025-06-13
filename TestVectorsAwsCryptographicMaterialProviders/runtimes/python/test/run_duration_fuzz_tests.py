#!/usr/bin/env python3
import sys
import time
import subprocess
import os

def run_fuzz_tests_for_duration():
    """
    Run fuzz tests continuously for a specified duration.
    
    Uses TEST_DURATION environment variable (minutes) to determine how long to run.
    """
    # Get the duration from environment or use default
    duration_min = int(os.environ.get('TEST_DURATION', '10'))
    end_time = time.time() + (duration_min * 60)
    
    print(f"Running fuzz tests for {duration_min} minutes...")
    
    # Run continuous tests until the time expires
    count = 0
    while time.time() < end_time:
        print(f"Running test iteration {count+1}...")
        result = subprocess.call(['python', '-m', 'pytest', '-xvs', 'test/test_fuzz_encryption.py'])
        if result != 0:
            print(f"Test iteration {count+1} failed with exit code {result}")
            sys.exit(result)
        
        count += 1
        remaining = int((end_time - time.time())/60)
        print(f"Completed {count} iterations. Time remaining: {remaining} minutes")
    
    print(f"Completed {count} total test iterations")

if __name__ == "__main__":
    run_fuzz_tests_for_duration()
