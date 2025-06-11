
# Example structure for fuzzing with Hypothesis

import hypothesis
from hypothesis import given, strategies as st
from aws_cryptographic_material_providers_library import MaterialProviders

# Define reusable strategies for generating input data
@st.composite
def encryption_contexts(draw):
    # Generate diverse encryption contexts with different characteristics
    num_pairs = draw(st.integers(min_value=0, max_value=100))
    context = {}
    for _ in range(num_pairs):
        # Generate keys with different characteristics
        key_type = draw(st.sampled_from(["normal", "empty", "long", "special"]))
        key = generate_key_by_type(draw, key_type)
        
        # Generate values with different characteristics
        value_type = draw(st.sampled_from(["normal", "empty", "binary", "long"]))
        value = generate_value_by_type(draw, value_type)
        
        context[key] = value
    return context

# Test invariants with the generated data
@given(encryption_context=encryption_contexts())
def test_encryption_context_handling(encryption_context):
    # Setup test environment
    mpl = MaterialProviders.builder().build()
    keyring = setup_test_keyring(mpl)
    
    try:
        # Perform encryption with the fuzzed encryption context
        encryption_result = perform_encryption(mpl, keyring, encryption_context, b"test data")
        
        # Verify decryption works correctly with the same context
        decryption_result = perform_decryption(mpl, keyring, encryption_context, encryption_result)
        
        # Verify the invariants that should always hold
        assert decryption_result == b"test data"
        
    except Exception as e:
        # Capture and classify errors
        classify_error(e, encryption_context)
        # Re-raise if it's an actual bug and not an expected validation error
        if not is_expected_validation_error(e):
            raise