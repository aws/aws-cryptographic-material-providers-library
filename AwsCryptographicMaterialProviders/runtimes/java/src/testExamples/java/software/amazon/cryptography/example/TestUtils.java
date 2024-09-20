package software.amazon.cryptography.example;

import java.time.Duration;

import software.amazon.awssdk.auth.credentials.AwsCredentialsProvider;
import software.amazon.awssdk.auth.credentials.DefaultCredentialsProvider;
import software.amazon.awssdk.http.SdkHttpClient;
import software.amazon.awssdk.http.apache.ApacheHttpClient;
import software.amazon.awssdk.services.dynamodb.DynamoDbClient;
import software.amazon.awssdk.services.kms.KmsClient;

public class TestUtils {

  public static final String TEST_KEYSTORE_NAME = "KeyStoreDdbTable";
  public static final String TEST_LOGICAL_KEYSTORE_NAME = "KeyStoreDdbTable";

  public static final String POSTAL_HORN_KEY_ARN =
  "arn:aws:kms:us-west-2:370957321024:key/bc127593-f7da-452c-a1f3-cd34c46f81f8";
  public static final String KEYSTORE_KMS_ARN =
    "arn:aws:kms:us-west-2:370957321024:key/9d989aa2-2f9c-438c-a745-cc57d3ad0126";
  // Our tests require access to DDB Table with this name
  public static final String TEST_DDB_TABLE_NAME =
    "DynamoDbEncryptionInterceptorTestTable";

  public static final AwsCredentialsProvider defaultCreds =
    DefaultCredentialsProvider.create();
  public static final SdkHttpClient httpClient = ApacheHttpClient
    .builder()
    .connectionTimeToLive(Duration.ofSeconds(5))
    .build();
  public static final DynamoDbClient dynamoDbClient = DynamoDbClient
    .builder().httpClient(httpClient).credentialsProvider(defaultCreds).build();
  public static final KmsClient kmsClient = KmsClient.builder()
    .httpClient(httpClient).credentialsProvider(defaultCreds).build();

}
