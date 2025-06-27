#!/bin/bash

# Run fuzzed test vectors with encryption and decryption processes
# This script generates random test vectors using Hypothesis and runs them
# through the encryption and decryption commands to find any issues.

set -e

# Default parameters
NUM_VECTORS=1000
RUNTIME="python"
OUTPUT_DIR=""
VERBOSE=false
FAIL_LOG="fuzz_failures.log"

# Parse command line arguments
while [[ $# -gt 0 ]]; do
  case $1 in
    --runtime)
      RUNTIME="$2"
      shift 2
      ;;
    --num-vectors)
      NUM_VECTORS="$2"
      shift 2
      ;;
    --output-dir)
      OUTPUT_DIR="$2"
      shift 2
      ;;
    --verbose)
      VERBOSE=true
      shift
      ;;
    --help)
      echo "Usage: $0 [options]"
      echo ""
      echo "Options:"
      echo "  --runtime <runtime>     Runtime to test (python, java, net, rust, go)"
      echo "  --num-vectors <n>       Number of test vectors to generate (default: 1000)"
      echo "  --output-dir <dir>      Output directory for test vectors"
      echo "  --verbose               Print verbose output"
      echo "  --help                  Show this help message"
      exit 0
      ;;
    *)
      echo "Unknown option: $1"
      exit 1
      ;;
  esac
done

# Set up directories
if [ -z "$OUTPUT_DIR" ]; then
  case $RUNTIME in
    python)
      OUTPUT_DIR="../../../runtimes/python"
      ;;
    java)
      OUTPUT_DIR="../../.."
      ;;
    net)
      OUTPUT_DIR="../../../runtimes/net"
      ;;
    rust)
      OUTPUT_DIR="../../../runtimes/rust"
      ;;
    go)
      OUTPUT_DIR="../../../runtimes/go"
      ;;
    *)
      echo "Unknown runtime: $RUNTIME"
      exit 1
      ;;
  esac
fi

# Ensure output directory exists
mkdir -p "$OUTPUT_DIR"

# Get the absolute path
ABSOLUTE_OUTPUT_DIR=$(cd "$OUTPUT_DIR" && pwd)

# Get script directory for relative paths
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/../../.." && pwd)"

# Clean up any old logs
rm -f "$FAIL_LOG"

echo "===== Running Fuzz Tests ====="
echo "Runtime: $RUNTIME"
echo "Number of vectors: $NUM_VECTORS"
echo "Output directory: $ABSOLUTE_OUTPUT_DIR"
echo "===============================\n"

echo "Step 1: Generating fuzzed test vectors..."
python3 "$SCRIPT_DIR/generate_fuzz_vectors.py" --num-vectors "$NUM_VECTORS" --output-dir "$ABSOLUTE_OUTPUT_DIR" --filename "fuzz_manifest.json"

echo "\nStep 2: Running encryption on generated vectors..."
cd "$ROOT_DIR"

# Check if we're already in the TestVectors directory
if [[ "$ROOT_DIR" == */TestVectorsAwsCryptographicMaterialProviders ]]; then
  TOX_CONFIG_PATH="runtimes/python"
else
  TOX_CONFIG_PATH="TestVectorsAwsCryptographicMaterialProviders/runtimes/python"
fi

case $RUNTIME in
  python)
    if [ "$VERBOSE" = true ]; then
      python3 -m tox -c "$TOX_CONFIG_PATH" --verbose -e cli -- encrypt --manifest-path "$ABSOLUTE_OUTPUT_DIR" --decrypt-manifest-path "$ABSOLUTE_OUTPUT_DIR"
    else
      python3 -m tox -c "$TOX_CONFIG_PATH" -e cli -- encrypt --manifest-path "$ABSOLUTE_OUTPUT_DIR" --decrypt-manifest-path "$ABSOLUTE_OUTPUT_DIR"
    fi
    ;;
  java)
    # Set Java paths based on current directory
    if [[ "$ROOT_DIR" == */TestVectorsAwsCryptographicMaterialProviders ]]; then
      JAVA_PATH="runtimes/java"
    else
      JAVA_PATH="TestVectorsAwsCryptographicMaterialProviders/runtimes/java"
    fi
    gradle -p "$JAVA_PATH" run --args="encrypt --manifest-path $ABSOLUTE_OUTPUT_DIR --decrypt-manifest-path $ABSOLUTE_OUTPUT_DIR"
    ;;
  net)
    # Set .NET paths based on current directory
    if [[ "$ROOT_DIR" == */TestVectorsAwsCryptographicMaterialProviders ]]; then
      NET_PATH="runtimes/net"
    else
      NET_PATH="TestVectorsAwsCryptographicMaterialProviders/runtimes/net"
    fi
    dotnet restore "$NET_PATH"
    dotnet build "$NET_PATH"
    dotnet run --project "$NET_PATH" --framework net6.0 encrypt --manifest-path "$ABSOLUTE_OUTPUT_DIR" --decrypt-manifest-path "$ABSOLUTE_OUTPUT_DIR"
    ;;
  rust)
    # Set Rust path based on current directory
    if [[ "$ROOT_DIR" == */TestVectorsAwsCryptographicMaterialProviders ]]; then
      cd runtimes/rust
    else
      cd TestVectorsAwsCryptographicMaterialProviders/runtimes/rust
    fi
    cargo run --bin test-vectors --features="wrapped-client" --release -- encrypt --manifest-path "$ABSOLUTE_OUTPUT_DIR" --decrypt-manifest-path "$ABSOLUTE_OUTPUT_DIR"
    ;;
  go)
    go -C TestVectorsAwsCryptographicMaterialProviders/runtimes/go/ImplementationFromDafny-go run ImplementationFromDafny.go encrypt --manifest-path="$ABSOLUTE_OUTPUT_DIR" --decrypt-manifest-path="$ABSOLUTE_OUTPUT_DIR"
    ;;
esac

echo "\nStep 3: Running decryption to verify..."
cd "$ROOT_DIR"
case $RUNTIME in
  python)
    if [ "$VERBOSE" = true ]; then
      python3 -m tox -c "$TOX_CONFIG_PATH" --verbose -e cli -- decrypt --manifest-path "$ABSOLUTE_OUTPUT_DIR"
    else
      python3 -m tox -c "$TOX_CONFIG_PATH" -e cli -- decrypt --manifest-path "$ABSOLUTE_OUTPUT_DIR"
    fi
    ;;
  java)
    gradle -p "$JAVA_PATH" run --args="decrypt --manifest-path $ABSOLUTE_OUTPUT_DIR"
    ;;
  net)
    dotnet run --project "$NET_PATH" --framework net6.0 decrypt --manifest-path "$ABSOLUTE_OUTPUT_DIR"
    ;;
  rust)
    # Set Rust path based on current directory (if not already set)
    if [[ "$ROOT_DIR" == */TestVectorsAwsCryptographicMaterialProviders ]]; then
      cd runtimes/rust
    else
      cd TestVectorsAwsCryptographicMaterialProviders/runtimes/rust
    fi
    cargo run --bin test-vectors --features="wrapped-client" --release -- decrypt --manifest-path "$ABSOLUTE_OUTPUT_DIR"
    ;;
  go)
    # Set Go path based on current directory
    if [[ "$ROOT_DIR" == */TestVectorsAwsCryptographicMaterialProviders ]]; then
      GO_PATH="runtimes/go/ImplementationFromDafny-go"
    else
      GO_PATH="TestVectorsAwsCryptographicMaterialProviders/runtimes/go/ImplementationFromDafny-go"
    fi
    go -C "$GO_PATH" run ImplementationFromDafny.go decrypt --manifest-path="$ABSOLUTE_OUTPUT_DIR"
    ;;
esac

echo "\nFuzz testing completed successfully!"
echo "$(wc -l < "$ABSOLUTE_OUTPUT_DIR/fuzz_manifest.json") test vectors were processed."

# Check for failures in the output
if [ -f "$FAIL_LOG" ]; then
  FAILURE_COUNT=$(wc -l < "$FAIL_LOG")
  echo "\n❌ Found $FAILURE_COUNT failures. See $FAIL_LOG for details."
  exit 1
else
  echo "\n✅ All tests passed!"
fi
