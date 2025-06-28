#!/usr/bin/env python3
"""
Fuzz Testing Runner for AWS Cryptographic Material Providers Library

This script runs the fuzzed test vectors through the existing test infrastructure
to detect failures and vulnerabilities.
"""

import os
import sys
import json
import subprocess
import logging
from datetime import datetime
from typing import Dict, Any, List, Optional


# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('fuzz_failures.log'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)


class FuzzTestRunner:
    """Runner for fuzz testing using existing test infrastructure."""
    
    def __init__(self, test_dir: str = "fuzz_testing"):
        self.test_dir = test_dir
        self.failures = []
        self.success_count = 0
        self.failure_count = 0
        
    def setup_test_environment(self) -> bool:
        """Set up the test environment with fuzzed files."""
        try:
            # Check if required files exist
            required_files = [
                "fuzz_test.json",
                "fuzz_keys.json"
            ]
            
            for file_path in required_files:
                if not os.path.exists(file_path):
                    logger.error(f"Required file not found: {file_path}")
                    return False
            
            # Copy fuzzed files to the test directory
            test_target_dir = "dafny/TestVectorsAwsCryptographicMaterialProviders/test/"
            
            # Ensure target directory exists
            os.makedirs(test_target_dir, exist_ok=True)
            
            # Backup original files
            if os.path.exists(f"{test_target_dir}/test.json"):
                os.rename(f"{test_target_dir}/test.json", f"{test_target_dir}/test.json.backup")
            if os.path.exists(f"{test_target_dir}/keys.json"):
                os.rename(f"{test_target_dir}/keys.json", f"{test_target_dir}/keys.json.backup")
            
            # Copy fuzzed files
            import shutil
            shutil.copy2("fuzz_test.json", f"{test_target_dir}/test.json")
            shutil.copy2("fuzz_keys.json", f"{test_target_dir}/keys.json")
            
            logger.info("Test environment set up successfully")
            return True
            
        except Exception as e:
            logger.error(f"Failed to set up test environment: {e}")
            return False
    
    def restore_original_files(self):
        """Restore original test files."""
        try:
            test_target_dir = "dafny/TestVectorsAwsCryptographicMaterialProviders/test/"
            
            # Remove fuzzed files
            if os.path.exists(f"{test_target_dir}/test.json"):
                os.remove(f"{test_target_dir}/test.json")
            if os.path.exists(f"{test_target_dir}/keys.json"):
                os.remove(f"{test_target_dir}/keys.json")
            
            # Restore original files
            if os.path.exists(f"{test_target_dir}/test.json.backup"):
                os.rename(f"{test_target_dir}/test.json.backup", f"{test_target_dir}/test.json")
            if os.path.exists(f"{test_target_dir}/keys.json.backup"):
                os.rename(f"{test_target_dir}/keys.json.backup", f"{test_target_dir}/keys.json")
            
            logger.info("Original files restored")
            
        except Exception as e:
            logger.error(f"Failed to restore original files: {e}")
    
    def run_make_command(self, command: str) -> tuple[bool, str]:
        """
        Run a make command and return success status and output.
        
        Args:
            command: The make command to run
            
        Returns:
            Tuple of (success, output)
        """
        try:
            logger.info(f"Running: make {command}")
            
            result = subprocess.run(
                ["make", command],
                capture_output=True,
                text=True,
                cwd="..",  # Run from parent directory where Makefile is
                timeout=300  # 5 minute timeout
            )
            
            success = result.returncode == 0
            output = result.stdout + result.stderr
            
            if success:
                logger.info(f"✓ {command} completed successfully")
            else:
                logger.error(f"✗ {command} failed with return code {result.returncode}")
                logger.error(f"Output: {output}")
            
            return success, output
            
        except subprocess.TimeoutExpired:
            logger.error(f"✗ {command} timed out after 5 minutes")
            return False, "Command timed out"
        except Exception as e:
            logger.error(f"✗ {command} failed with exception: {e}")
            return False, str(e)
    
    def run_fuzz_tests(self) -> bool:
        """
        Run the complete fuzz testing workflow.
        
        Returns:
            True if all tests passed, False otherwise
        """
        logger.info("=== Starting Fuzz Test Run ===")
        logger.info(f"Timestamp: {datetime.now()}")
        
        # Set up test environment
        if not self.setup_test_environment():
            return False
        
        try:
            # Step 1: Generate encrypt manifest
            logger.info("Step 1: Generating encrypt manifest...")
            success, output = self.run_make_command("test_generate_vectors_python")
            if not success:
                self.record_failure("manifest_generation", "Failed to generate encrypt manifest", output)
            
            # Step 2: Run encryption tests
            logger.info("Step 2: Running encryption tests...")
            success, output = self.run_make_command("test_encrypt_vectors_python")
            if not success:
                self.record_failure("encryption", "Encryption tests failed", output)
            else:
                self.success_count += 1
            
            # Step 3: Run decryption tests
            logger.info("Step 3: Running decryption tests...")
            success, output = self.run_make_command("test_decrypt_encrypt_vectors_python")
            if not success:
                self.record_failure("decryption", "Decryption tests failed", output)
            else:
                self.success_count += 1
            
            # Log summary
            self.log_summary()
            
            return len(self.failures) == 0
            
        finally:
            # Always restore original files
            self.restore_original_files()
    
    def record_failure(self, test_type: str, description: str, output: str):
        """Record a test failure."""
        failure = {
            "timestamp": datetime.now().isoformat(),
            "test_type": test_type,
            "description": description,
            "output": output
        }
        
        self.failures.append(failure)
        self.failure_count += 1
        
        logger.error(f"FAILURE: {test_type} - {description}")
    
    def log_summary(self):
        """Log a summary of the test run."""
        logger.info("=== Fuzz Test Summary ===")
        logger.info(f"Total tests run: {self.success_count + self.failure_count}")
        logger.info(f"Successful: {self.success_count}")
        logger.info(f"Failures: {self.failure_count}")
        
        if self.failures:
            logger.error("=== Failures Detected ===")
            for i, failure in enumerate(self.failures, 1):
                logger.error(f"Failure {i}:")
                logger.error(f"  Type: {failure['test_type']}")
                logger.error(f"  Description: {failure['description']}")
                logger.error(f"  Timestamp: {failure['timestamp']}")
                logger.error(f"  Output: {failure['output'][:500]}...")  # Truncate long output
        
        # Save detailed failure report
        if self.failures:
            with open("fuzz_detailed_failures.json", "w") as f:
                json.dump(self.failures, f, indent=2)
            logger.info("Detailed failure report saved to fuzz_detailed_failures.json")


def main():
    """Main function to run fuzz tests."""
    print("=== AWS Cryptographic Material Providers Fuzz Testing Runner ===")
    
    # Check if we're in the right directory
    # if not os.path.exists("fuzz_testing"):
    #     print("Error: fuzz_testing directory not found. Run from TestVectorsAwsCryptographicMaterialProviders directory.")
    #     sys.exit(1)
    
    # Check if fuzzed test vectors exist
    if not os.path.exists("fuzz_test.json"):
        print("Error: fuzz_test.json not found. Run fuzz_generator.py first.")
        sys.exit(1)
    
    # Run the fuzz tests
    runner = FuzzTestRunner()
    success = runner.run_fuzz_tests()
    
    if success:
        print("\n🎉 All fuzz tests passed!")
        sys.exit(0)
    else:
        print(f"\n❌ {runner.failure_count} fuzz test(s) failed!")
        print("Check fuzz_failures.log for details.")
        sys.exit(1)


if __name__ == "__main__":
    main() 