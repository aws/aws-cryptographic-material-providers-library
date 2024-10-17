package software.amazon.cryptography.example;

import javax.annotation.Nullable;

import software.amazon.awssdk.services.dynamodb.DynamoDbClient;
import software.amazon.awssdk.services.kms.KmsClient;
import software.amazon.awssdk.auth.credentials.AwsCredentialsProvider;
import software.amazon.awssdk.auth.credentials.DefaultCredentialsProvider;
import software.amazon.awssdk.http.SdkHttpClient;
import software.amazon.awssdk.http.apache.ApacheHttpClient;

public class ClientProvider {
  private static final AwsCredentialsProvider defaultCreds =
    DefaultCredentialsProvider.create();
  private static final SdkHttpClient httpClient = ApacheHttpClient.create();

  public static DynamoDbClient dynamoDB(
    @Nullable DynamoDbClient dynamoDbClient
  ) {
    if (dynamoDbClient == null) {
      //noinspection resource
      dynamoDbClient = DynamoDbClient.builder()
        .httpClient(httpClient)
        .credentialsProvider(defaultCreds)
        .build();
    }
    return dynamoDbClient;
  }

  public static KmsClient kms(
    @Nullable KmsClient kmsClient
  ) {
    if (kmsClient == null) {
      //noinspection resource
      kmsClient = KmsClient.builder()
        .httpClient(httpClient)
        .credentialsProvider(defaultCreds)
        .build();
    }
    return kmsClient;
  }
}
