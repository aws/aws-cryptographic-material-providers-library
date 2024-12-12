package software.amazon.cryptography.example.hierarchy.concurrent;

// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

import java.io.IOException;
import java.nio.ByteBuffer;
import java.util.*;
import java.util.logging.*;
import org.testng.annotations.Test;
import software.amazon.awssdk.services.dynamodb.DynamoDbClient;
import software.amazon.awssdk.services.dynamodb.model.TransactionCanceledException;
import software.amazon.awssdk.services.kms.KmsClient;
import software.amazon.cryptography.keystore.KeyStore;
import software.amazon.cryptography.keystore.model.BranchKeyMaterials;
import software.amazon.cryptography.keystore.model.CreateKeyInput;
import software.amazon.cryptography.keystore.model.GetActiveBranchKeyInput;
import software.amazon.cryptography.keystore.model.KMSConfiguration;
import software.amazon.cryptography.keystore.model.KeyStoreConfig;

// Class for testing Key Store Concurrency for Creating and Getting the branch keys
public class StorageConcurrencyTests {

  private static final String branchKeyId =
    "concurrency_test_branch_key_" + UUID.randomUUID().toString();
  private static final String keyStoreTableName = "KeyStoreDdbTable";
  private static final String logicalKeyStoreName = "KeyStoreDdbTable";
  private static final String kmsKeyId =
    "arn:aws:kms:us-west-2:370957321024:key/9d989aa2-2f9c-438c-a745-cc57d3ad0126";

  private static final KeyStore keyStore = KeyStore
    .builder()
    .KeyStoreConfig(
      KeyStoreConfig
        .builder()
        .ddbClient(DynamoDbClient.create())
        .ddbTableName(keyStoreTableName)
        .logicalKeyStoreName(logicalKeyStoreName)
        .kmsClient(KmsClient.create())
        .kmsConfiguration(
          KMSConfiguration.builder().kmsKeyArn(kmsKeyId).build()
        )
        .build()
    )
    .build();

  private static final Map<String, String> encryptionContext;

  static {
    Map<String, String> tempMap = new HashMap<>();
    tempMap.put("Example", "Encryption");
    tempMap.put("Context", "To");
    tempMap.put("Test", "Key");
    tempMap.put("Store", "Concurrency");
    encryptionContext = Collections.unmodifiableMap(tempMap);
  }

  public void createALotOfKeys() {
    try {
      String branchKeyIdGenerated = keyStore
        .CreateKey(
          CreateKeyInput
            .builder()
            .branchKeyIdentifier(branchKeyId)
            .encryptionContext(encryptionContext)
            .build()
        )
        .branchKeyIdentifier();

      logInfo(
        "Success for createALotOfKeys; BranchKeyIdGenerated: " +
          branchKeyIdGenerated
      );
    } catch (TransactionCanceledException e) {
      logInfo("Received TransactionCanceledException: " + e.getMessage());
    } catch (Exception e) {
      logError("Unexpected error occurred while creating key", e);
    }
  }

  public void getALotOfKeys() {
    BranchKeyMaterials activeBranchKeyMaterials = keyStore
      .GetActiveBranchKey(
        GetActiveBranchKeyInput
          .builder()
          .branchKeyIdentifier(branchKeyId)
          .build()
      )
      .branchKeyMaterials();

    try {
      logBranchKeyMaterials(activeBranchKeyMaterials);
      logInfo("BranchKeyMaterials processed successfully");
    } catch (Exception e) {
      logError("Error processing BranchKeyMaterials", e);
    }
  }

  @Test(threadPoolSize = 15, invocationCount = 100, timeOut = 10000)
  public void testConcurrency() {
    try {
      getALotOfKeys();
    } catch (Exception e) {
      logError("Maybe expected error in testConcurrency", e);
      createALotOfKeys();
    }
  }

  // Logger setup
  private static final Logger LOGGER = Logger.getLogger(
    StorageConcurrencyTests.class.getName()
  );
  private static FileHandler fileHandler;

  static {
    try {
      fileHandler = new FileHandler("keystore_operations.log", true);
      fileHandler.setFormatter(new SimpleFormatter());
      LOGGER.addHandler(fileHandler);
      LOGGER.setLevel(Level.ALL);
    } catch (IOException e) {
      System.err.println("Failed to set up logger: " + e.getMessage());
      e.printStackTrace();
    }
  }

  // Logging methods
  public static void logBranchKeyMaterials(BranchKeyMaterials materials) {
    StringBuilder sb = new StringBuilder();
    sb.append("BranchKeyMaterials:\n");
    sb
      .append("  Branch Key Identifier: ")
      .append(materials.branchKeyIdentifier())
      .append("\n");
    sb
      .append("  Branch Key Version: ")
      .append(materials.branchKeyVersion())
      .append("\n");

    sb.append("  Encryption Context:\n");
    for (Map.Entry<String, String> entry : materials
      .encryptionContext()
      .entrySet()) {
      sb
        .append("    ")
        .append(entry.getKey())
        .append(": ")
        .append(entry.getValue())
        .append("\n");
    }

    ByteBuffer branchKey = materials.branchKey();
    sb.append("  Branch Key (ByteBuffer):\n");
    sb.append("    Capacity: ").append(branchKey.capacity()).append("\n");
    sb.append("    Hex: ").append(bytesToHex(branchKey.array())).append("\n");

    LOGGER.info(sb.toString());
  }

  public static void logInfo(String message) {
    LOGGER.info(message);
  }

  public static void logWarning(String message) {
    LOGGER.warning(message);
  }

  public static void logError(String message, Throwable thrown) {
    LOGGER.log(Level.SEVERE, message, thrown);
  }

  private static String bytesToHex(byte[] bytes) {
    StringBuilder sb = new StringBuilder();
    for (byte b : bytes) {
      sb.append(String.format("%02X ", b));
    }
    return sb.toString();
  }
}
