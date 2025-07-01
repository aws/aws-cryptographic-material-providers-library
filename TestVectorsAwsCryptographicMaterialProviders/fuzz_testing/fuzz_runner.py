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
        
        # Load the fuzzed test vectors for detailed logging
        try:
            with open("fuzz_test.json", "r") as f:
                fuzz_data = json.load(f)
            test_vectors = fuzz_data.get("tests", {})
            logger.info(f"Loaded {len(test_vectors)} fuzzed test vectors")
        except Exception as e:
            logger.error(f"Failed to load fuzz test data: {e}")
            test_vectors = {}
        
        # Set up test environment
        if not self.setup_test_environment():
            return False
        
        try:
            # Step 1: Generate encrypt manifest
            logger.info("Step 1: Generating encrypt manifest...")
            success, output = self.run_make_command("test_generate_vectors_python")
            if not success:
                self.record_failure("manifest_generation", "Failed to generate encrypt manifest", output, test_vectors)
            
            # Step 2: Run encryption tests
            logger.info("Step 2: Running encryption tests...")
            success, output = self.run_make_command("test_encrypt_vectors_python")
            if not success:
                self.record_failure("encryption", "Encryption tests failed", output, test_vectors)
            else:
                self.success_count += 1
            
            # Step 3: Run decryption tests
            logger.info("Step 3: Running decryption tests...")
            success, output = self.run_make_command("test_decrypt_encrypt_vectors_python")
            if not success:
                self.record_failure("decryption", "Decryption tests failed", output, test_vectors)
            else:
                self.success_count += 1
            
            # Log summary
            self.log_summary()
            
            return len(self.failures) == 0
            
        finally:
            # Always restore original files
            self.restore_original_files()
    
    def record_failure(self, test_type: str, description: str, output: str, test_vectors: dict = None):
        """Record a test failure with detailed information."""
        # Try to extract specific test vector information from the output
        failed_test_ids = self.extract_failed_test_ids(output)
        
        failure = {
            "timestamp": datetime.now().isoformat(),
            "test_type": test_type,
            "description": description,
            "output": output,
            "failed_test_ids": failed_test_ids,
            "fuzzed_inputs": {}
        }
        
        # Add details about the failed test vectors
        if test_vectors and failed_test_ids:
            for test_id in failed_test_ids:
                if test_id in test_vectors:
                    failure["fuzzed_inputs"][test_id] = {
                        "algorithm_suite": test_vectors[test_id].get("algorithmSuiteId"),
                        "encryption_context": test_vectors[test_id].get("encryptionContext"),
                        "required_keys": test_vectors[test_id].get("requiredEncryptionContextKeys"),
                        "reproduced_context": test_vectors[test_id].get("reproducedEncryptionContext"),
                        "key_description": test_vectors[test_id].get("encryptKeyDescription")
                    }
        
        self.failures.append(failure)
        self.failure_count += 1
        
        logger.error(f"FAILURE: {test_type} - {description}")
        
        # Log detailed information about failed test vectors
        if failed_test_ids:
            logger.error(f"Failed test IDs: {failed_test_ids}")
            for test_id in failed_test_ids:
                if test_vectors and test_id in test_vectors:
                    test = test_vectors[test_id]
                    logger.error(f"  Test {test_id}:")
                    logger.error(f"    Algorithm: {test.get('algorithmSuiteId')}")
                    logger.error(f"    Context: {test.get('encryptionContext')}")
                    logger.error(f"    Required Keys: {test.get('requiredEncryptionContextKeys')}")
                    logger.error(f"    Reproduced Context: {test.get('reproducedEncryptionContext')}")
    
    def extract_failed_test_ids(self, output: str) -> list:
        """Extract test IDs from failure output."""
        # Look for patterns like "Test ID: abc123-def456" or similar
        import re
        
        # Common patterns for test IDs in the output
        patterns = [
            r'Test ID:\s*([a-f0-9-]+)',
            r'Test\s+([a-f0-9-]+)\s+failed',
            r'Vector\s+([a-f0-9-]+)\s+failed',
            r'([a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})'
        ]
        
        failed_ids = []
        for pattern in patterns:
            matches = re.findall(pattern, output, re.IGNORECASE)
            failed_ids.extend(matches)
        
        return list(set(failed_ids))  # Remove duplicates
    
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
                
                if failure.get('failed_test_ids'):
                    logger.error(f"  Failed Test IDs: {failure['failed_test_ids']}")
                    
                    # Show details of failed test vectors
                    for test_id in failure['failed_test_ids']:
                        if test_id in failure.get('fuzzed_inputs', {}):
                            test_info = failure['fuzzed_inputs'][test_id]
                            logger.error(f"    Test {test_id}:")
                            logger.error(f"      Algorithm: {test_info.get('algorithm_suite')}")
                            logger.error(f"      Context: {test_info.get('encryption_context')}")
                            logger.error(f"      Required Keys: {test_info.get('required_keys')}")
                            logger.error(f"      Reproduced Context: {test_info.get('reproduced_context')}")
                
                # Show truncated output
                output_preview = failure['output'][:1000] + "..." if len(failure['output']) > 1000 else failure['output']
                logger.error(f"  Output Preview: {output_preview}")
        
        # Save detailed failure report
        if self.failures:
            detailed_report = {
                "summary": {
                    "total_tests": self.success_count + self.failure_count,
                    "successful": self.success_count,
                    "failures": self.failure_count,
                    "timestamp": datetime.now().isoformat()
                },
                "failures": self.failures
            }
            
            with open("fuzz_detailed_failures.json", "w") as f:
                json.dump(detailed_report, f, indent=2)
            logger.info("Detailed failure report saved to fuzz_detailed_failures.json")
            
            # Also create a human-readable summary
            with open("fuzz_failure_summary.txt", "w") as f:
                f.write("=== FUZZ TEST FAILURE SUMMARY ===\n")
                f.write(f"Timestamp: {datetime.now()}\n")
                f.write(f"Total Tests: {self.success_count + self.failure_count}\n")
                f.write(f"Successful: {self.success_count}\n")
                f.write(f"Failures: {self.failure_count}\n\n")
                
                for i, failure in enumerate(self.failures, 1):
                    f.write(f"FAILURE {i}:\n")
                    f.write(f"  Type: {failure['test_type']}\n")
                    f.write(f"  Description: {failure['description']}\n")
                    f.write(f"  Timestamp: {failure['timestamp']}\n")
                    
                    if failure.get('failed_test_ids'):
                        f.write(f"  Failed Test IDs: {failure['failed_test_ids']}\n")
                        
                        for test_id in failure['failed_test_ids']:
                            if test_id in failure.get('fuzzed_inputs', {}):
                                test_info = failure['fuzzed_inputs'][test_id]
                                f.write(f"    Test {test_id}:\n")
                                f.write(f"      Algorithm: {test_info.get('algorithm_suite')}\n")
                                f.write(f"      Context: {test_info.get('encryption_context')}\n")
                                f.write(f"      Required Keys: {test_info.get('required_keys')}\n")
                                f.write(f"      Reproduced Context: {test_info.get('reproduced_context')}\n")
                    
                    f.write(f"  Output: {failure['output']}\n\n")
            
            logger.info("Human-readable summary saved to fuzz_failure_summary.txt")


def main():
    """Main function to run fuzz tests."""
    print("=== AWS Cryptographic Material Providers Fuzz Testing Runner ===")
    
    # Check if we're in the right directory
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