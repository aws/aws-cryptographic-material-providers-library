#!/bin/bash

# Fuzz Testing Script for AWS Cryptographic Material Providers Library
# Run this from the TestVectorsAwsCryptographicMaterialProviders directory

set -e  # Exit on any error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Logging function
log() {
    echo -e "${BLUE}[$(date '+%Y-%m-%d %H:%M:%S')]${NC} $1" | tee -a fuzz_test.log
}

error() {
    echo -e "${RED}[$(date '+%Y-%m-%d %H:%M:%S')] ERROR:${NC} $1" | tee -a fuzz_test.log
}

success() {
    echo -e "${GREEN}[$(date '+%Y-%m-%d %H:%M:%S')] SUCCESS:${NC} $1" | tee -a fuzz_test.log
}

warning() {
    echo -e "${YELLOW}[$(date '+%Y-%m-%d %H:%M:%S')] WARNING:${NC} $1" | tee -a fuzz_test.log
}

# Check if we're in the right directory
if [ ! -f "Makefile" ]; then
    error "Must run from TestVectorsAwsCryptographicMaterialProviders directory"
    exit 1
fi

log "=== Starting Fuzz Testing Workflow ==="

# Step 1: Generate fuzzed test vectors
log "Step 1: Generating fuzzed test vectors..."
cd runtimes/python
if ! python3 fuzz_generator.py; then
    error "Failed to generate fuzzed test vectors"
    exit 1
fi
success "Generated fuzzed test vectors"
cd ../..

# Step 2: Run encryption tests
log "Step 2: Running encryption tests..."
if ! make test_encrypt_vectors_python; then
    error "Encryption tests failed"
    exit 1
fi
success "Encryption tests completed"

# Step 3: Run decryption tests
log "Step 3: Running decryption tests..."
if ! make test_decrypt_encrypt_vectors_python; then
    error "Decryption tests failed"
    exit 1
fi
success "Decryption tests completed"

log "=== Fuzz Testing Workflow Completed Successfully ==="
success "All tests passed! Check fuzz_test.log for details." 