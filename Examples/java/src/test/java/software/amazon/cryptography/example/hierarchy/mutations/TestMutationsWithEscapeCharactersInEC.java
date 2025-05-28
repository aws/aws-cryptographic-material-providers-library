// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
package software.amazon.cryptography.example.hierarchy.mutations;

import java.util.Collections;
import java.util.HashMap;
import java.util.Map;
import java.util.Objects;
import java.util.UUID;
import org.testng.Assert;
import org.testng.annotations.Test;
import software.amazon.cryptography.example.DdbHelper;
import software.amazon.cryptography.example.Fixtures;
import software.amazon.cryptography.example.hierarchy.AdminProvider;
import software.amazon.cryptography.example.hierarchy.CreateKeyExample;
import software.amazon.cryptography.example.hierarchy.KeyStoreProvider;
import software.amazon.cryptography.keystore.KeyStore;
import software.amazon.cryptography.keystore.model.GetActiveBranchKeyInput;
import software.amazon.cryptography.keystore.model.GetActiveBranchKeyOutput;
import software.amazon.cryptography.keystore.model.HierarchyVersion;
import software.amazon.cryptography.keystoreadmin.model.KeyStoreAdminException;

public class TestMutationsWithEscapeCharactersInEC {
}
