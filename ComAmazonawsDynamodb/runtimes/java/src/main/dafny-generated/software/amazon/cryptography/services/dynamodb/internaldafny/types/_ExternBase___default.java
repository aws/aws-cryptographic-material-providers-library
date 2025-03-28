// Class _ExternBase___default
// Dafny class __default compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public abstract class _ExternBase___default {
  public _ExternBase___default() {
  }
  public static boolean IsValid__AttributeName(dafny.DafnySequence<? extends Character> x) {
    return ((java.math.BigInteger.valueOf((x).length())).signum() != -1) && ((java.math.BigInteger.valueOf((x).length())).compareTo(java.math.BigInteger.valueOf(65535L)) <= 0);
  }
  public static boolean IsValid__AttributeNameList(dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> x) {
    return (java.math.BigInteger.ONE).compareTo(java.math.BigInteger.valueOf((x).length())) <= 0;
  }
  public static boolean IsValid__AutoScalingPolicyName(dafny.DafnySequence<? extends Character> x) {
    return ((java.math.BigInteger.ONE).compareTo(java.math.BigInteger.valueOf((x).length())) <= 0) && ((java.math.BigInteger.valueOf((x).length())).compareTo(java.math.BigInteger.valueOf(256L)) <= 0);
  }
  public static boolean IsValid__AutoScalingRoleArn(dafny.DafnySequence<? extends Character> x) {
    return ((java.math.BigInteger.ONE).compareTo(java.math.BigInteger.valueOf((x).length())) <= 0) && ((java.math.BigInteger.valueOf((x).length())).compareTo(java.math.BigInteger.valueOf(1600L)) <= 0);
  }
  public static boolean IsValid__BackupArn(dafny.DafnySequence<? extends Character> x) {
    return ((java.math.BigInteger.valueOf(37L)).compareTo(java.math.BigInteger.valueOf((x).length())) <= 0) && ((java.math.BigInteger.valueOf((x).length())).compareTo(java.math.BigInteger.valueOf(1024L)) <= 0);
  }
  public static boolean IsValid__BackupName(dafny.DafnySequence<? extends Character> x) {
    return ((java.math.BigInteger.valueOf(3L)).compareTo(java.math.BigInteger.valueOf((x).length())) <= 0) && ((java.math.BigInteger.valueOf((x).length())).compareTo(java.math.BigInteger.valueOf(255L)) <= 0);
  }
  public static boolean IsValid__BackupsInputLimit(int x) {
    return ((1) <= (x)) && ((x) <= (100));
  }
  public static boolean IsValid__BackupSizeBytes(long x) {
    return java.lang.Long.signum((x)) != -1;
  }
  public static boolean IsValid__BatchGetRequestMap(dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends KeysAndAttributes> x) {
    return ((java.math.BigInteger.ONE).compareTo(java.math.BigInteger.valueOf((x).size())) <= 0) && ((java.math.BigInteger.valueOf((x).size())).compareTo(java.math.BigInteger.valueOf(100L)) <= 0);
  }
  public static boolean IsValid__BatchWriteItemRequestMap(dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends WriteRequest>> x) {
    return ((java.math.BigInteger.ONE).compareTo(java.math.BigInteger.valueOf((x).size())) <= 0) && ((java.math.BigInteger.valueOf((x).size())).compareTo(java.math.BigInteger.valueOf(25L)) <= 0);
  }
  public static boolean IsValid__BilledSizeBytes(long x) {
    return java.lang.Long.signum((x)) != -1;
  }
  public static boolean IsValid__CancellationReasonList(dafny.DafnySequence<? extends CancellationReason> x) {
    return ((java.math.BigInteger.ONE).compareTo(java.math.BigInteger.valueOf((x).length())) <= 0) && ((java.math.BigInteger.valueOf((x).length())).compareTo(java.math.BigInteger.valueOf(100L)) <= 0);
  }
  public static boolean IsValid__ClientRequestToken(dafny.DafnySequence<? extends Character> x) {
    return ((java.math.BigInteger.ONE).compareTo(java.math.BigInteger.valueOf((x).length())) <= 0) && ((java.math.BigInteger.valueOf((x).length())).compareTo(java.math.BigInteger.valueOf(36L)) <= 0);
  }
  public static boolean IsValid__CloudWatchLogGroupArn(dafny.DafnySequence<? extends Character> x) {
    return ((java.math.BigInteger.ONE).compareTo(java.math.BigInteger.valueOf((x).length())) <= 0) && ((java.math.BigInteger.valueOf((x).length())).compareTo(java.math.BigInteger.valueOf(1024L)) <= 0);
  }
  public static boolean IsValid__ConsumedCapacityUnits(dafny.DafnySequence<? extends java.lang.Byte> x) {
    return ((java.math.BigInteger.valueOf(8L)).compareTo(java.math.BigInteger.valueOf((x).length())) <= 0) && ((java.math.BigInteger.valueOf((x).length())).compareTo(java.math.BigInteger.valueOf(8L)) <= 0);
  }
  public static boolean IsValid__CsvDelimiter(dafny.DafnySequence<? extends Character> x) {
    return ((java.math.BigInteger.ONE).compareTo(java.math.BigInteger.valueOf((x).length())) <= 0) && ((java.math.BigInteger.valueOf((x).length())).compareTo(java.math.BigInteger.ONE) <= 0);
  }
  public static boolean IsValid__CsvHeader(dafny.DafnySequence<? extends Character> x) {
    return ((java.math.BigInteger.ONE).compareTo(java.math.BigInteger.valueOf((x).length())) <= 0) && ((java.math.BigInteger.valueOf((x).length())).compareTo(java.math.BigInteger.valueOf(65536L)) <= 0);
  }
  public static boolean IsValid__CsvHeaderList(dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> x) {
    return ((java.math.BigInteger.ONE).compareTo(java.math.BigInteger.valueOf((x).length())) <= 0) && ((java.math.BigInteger.valueOf((x).length())).compareTo(java.math.BigInteger.valueOf(255L)) <= 0);
  }
  public static boolean IsValid__DoubleObject(dafny.DafnySequence<? extends java.lang.Byte> x) {
    return ((java.math.BigInteger.valueOf(8L)).compareTo(java.math.BigInteger.valueOf((x).length())) <= 0) && ((java.math.BigInteger.valueOf((x).length())).compareTo(java.math.BigInteger.valueOf(8L)) <= 0);
  }
  public static boolean IsValid__ErrorCount(long x) {
    return java.lang.Long.signum((x)) != -1;
  }
  public static boolean IsValid__ExportArn(dafny.DafnySequence<? extends Character> x) {
    return ((java.math.BigInteger.valueOf(37L)).compareTo(java.math.BigInteger.valueOf((x).length())) <= 0) && ((java.math.BigInteger.valueOf((x).length())).compareTo(java.math.BigInteger.valueOf(1024L)) <= 0);
  }
  public static boolean IsValid__GlobalSecondaryIndexAutoScalingUpdateList(dafny.DafnySequence<? extends GlobalSecondaryIndexAutoScalingUpdate> x) {
    return (java.math.BigInteger.ONE).compareTo(java.math.BigInteger.valueOf((x).length())) <= 0;
  }
  public static boolean IsValid__GlobalTableGlobalSecondaryIndexSettingsUpdateList(dafny.DafnySequence<? extends GlobalTableGlobalSecondaryIndexSettingsUpdate> x) {
    return ((java.math.BigInteger.ONE).compareTo(java.math.BigInteger.valueOf((x).length())) <= 0) && ((java.math.BigInteger.valueOf((x).length())).compareTo(java.math.BigInteger.valueOf(20L)) <= 0);
  }
  public static boolean IsValid__ImportArn(dafny.DafnySequence<? extends Character> x) {
    return ((java.math.BigInteger.valueOf(37L)).compareTo(java.math.BigInteger.valueOf((x).length())) <= 0) && ((java.math.BigInteger.valueOf((x).length())).compareTo(java.math.BigInteger.valueOf(1024L)) <= 0);
  }
  public static boolean IsValid__ImportedItemCount(long x) {
    return java.lang.Long.signum((x)) != -1;
  }
  public static boolean IsValid__ImportNextToken(dafny.DafnySequence<? extends Character> x) {
    return ((java.math.BigInteger.valueOf(112L)).compareTo(java.math.BigInteger.valueOf((x).length())) <= 0) && ((java.math.BigInteger.valueOf((x).length())).compareTo(java.math.BigInteger.valueOf(1024L)) <= 0);
  }
  public static boolean IsValid__IndexName(dafny.DafnySequence<? extends Character> x) {
    return ((java.math.BigInteger.valueOf(3L)).compareTo(java.math.BigInteger.valueOf((x).length())) <= 0) && ((java.math.BigInteger.valueOf((x).length())).compareTo(java.math.BigInteger.valueOf(255L)) <= 0);
  }
  public static boolean IsValid__ItemCollectionSizeEstimateBound(dafny.DafnySequence<? extends java.lang.Byte> x) {
    return ((java.math.BigInteger.valueOf(8L)).compareTo(java.math.BigInteger.valueOf((x).length())) <= 0) && ((java.math.BigInteger.valueOf((x).length())).compareTo(java.math.BigInteger.valueOf(8L)) <= 0);
  }
  public static boolean IsValid__ItemCount(long x) {
    return java.lang.Long.signum((x)) != -1;
  }
  public static boolean IsValid__ItemResponseList(dafny.DafnySequence<? extends ItemResponse> x) {
    return ((java.math.BigInteger.ONE).compareTo(java.math.BigInteger.valueOf((x).length())) <= 0) && ((java.math.BigInteger.valueOf((x).length())).compareTo(java.math.BigInteger.valueOf(100L)) <= 0);
  }
  public static boolean IsValid__KeyList(dafny.DafnySequence<? extends dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> x) {
    return ((java.math.BigInteger.ONE).compareTo(java.math.BigInteger.valueOf((x).length())) <= 0) && ((java.math.BigInteger.valueOf((x).length())).compareTo(java.math.BigInteger.valueOf(100L)) <= 0);
  }
  public static boolean IsValid__KeySchema(dafny.DafnySequence<? extends KeySchemaElement> x) {
    return ((java.math.BigInteger.ONE).compareTo(java.math.BigInteger.valueOf((x).length())) <= 0) && ((java.math.BigInteger.valueOf((x).length())).compareTo(java.math.BigInteger.valueOf(2L)) <= 0);
  }
  public static boolean IsValid__KeySchemaAttributeName(dafny.DafnySequence<? extends Character> x) {
    return ((java.math.BigInteger.ONE).compareTo(java.math.BigInteger.valueOf((x).length())) <= 0) && ((java.math.BigInteger.valueOf((x).length())).compareTo(java.math.BigInteger.valueOf(255L)) <= 0);
  }
  public static boolean IsValid__ListContributorInsightsLimit(int x) {
    return (x) <= (100);
  }
  public static boolean IsValid__ListExportsMaxLimit(int x) {
    return ((1) <= (x)) && ((x) <= (25));
  }
  public static boolean IsValid__ListImportsMaxLimit(int x) {
    return ((1) <= (x)) && ((x) <= (25));
  }
  public static boolean IsValid__ListTablesInputLimit(int x) {
    return ((1) <= (x)) && ((x) <= (100));
  }
  public static boolean IsValid__NonKeyAttributeName(dafny.DafnySequence<? extends Character> x) {
    return ((java.math.BigInteger.ONE).compareTo(java.math.BigInteger.valueOf((x).length())) <= 0) && ((java.math.BigInteger.valueOf((x).length())).compareTo(java.math.BigInteger.valueOf(255L)) <= 0);
  }
  public static boolean IsValid__NonKeyAttributeNameList(dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> x) {
    return ((java.math.BigInteger.ONE).compareTo(java.math.BigInteger.valueOf((x).length())) <= 0) && ((java.math.BigInteger.valueOf((x).length())).compareTo(java.math.BigInteger.valueOf(20L)) <= 0);
  }
  public static boolean IsValid__NonNegativeLongObject(long x) {
    return java.lang.Long.signum((x)) != -1;
  }
  public static boolean IsValid__ParameterizedStatements(dafny.DafnySequence<? extends ParameterizedStatement> x) {
    return ((java.math.BigInteger.ONE).compareTo(java.math.BigInteger.valueOf((x).length())) <= 0) && ((java.math.BigInteger.valueOf((x).length())).compareTo(java.math.BigInteger.valueOf(100L)) <= 0);
  }
  public static boolean IsValid__PartiQLBatchRequest(dafny.DafnySequence<? extends BatchStatementRequest> x) {
    return ((java.math.BigInteger.ONE).compareTo(java.math.BigInteger.valueOf((x).length())) <= 0) && ((java.math.BigInteger.valueOf((x).length())).compareTo(java.math.BigInteger.valueOf(25L)) <= 0);
  }
  public static boolean IsValid__PartiQLNextToken(dafny.DafnySequence<? extends Character> x) {
    return ((java.math.BigInteger.ONE).compareTo(java.math.BigInteger.valueOf((x).length())) <= 0) && ((java.math.BigInteger.valueOf((x).length())).compareTo(java.math.BigInteger.valueOf(32768L)) <= 0);
  }
  public static boolean IsValid__PartiQLStatement(dafny.DafnySequence<? extends Character> x) {
    return ((java.math.BigInteger.ONE).compareTo(java.math.BigInteger.valueOf((x).length())) <= 0) && ((java.math.BigInteger.valueOf((x).length())).compareTo(java.math.BigInteger.valueOf(8192L)) <= 0);
  }
  public static boolean IsValid__PolicyRevisionId(dafny.DafnySequence<? extends Character> x) {
    return ((java.math.BigInteger.ONE).compareTo(java.math.BigInteger.valueOf((x).length())) <= 0) && ((java.math.BigInteger.valueOf((x).length())).compareTo(java.math.BigInteger.valueOf(255L)) <= 0);
  }
  public static boolean IsValid__PositiveIntegerObject(int x) {
    return (1) <= (x);
  }
  public static boolean IsValid__PositiveLongObject(long x) {
    return ((long) 1L) <= (x);
  }
  public static boolean IsValid__PreparedStatementParameters(dafny.DafnySequence<? extends AttributeValue> x) {
    return (java.math.BigInteger.ONE).compareTo(java.math.BigInteger.valueOf((x).length())) <= 0;
  }
  public static boolean IsValid__ProcessedItemCount(long x) {
    return java.lang.Long.signum((x)) != -1;
  }
  public static boolean IsValid__ReplicaAutoScalingUpdateList(dafny.DafnySequence<? extends ReplicaAutoScalingUpdate> x) {
    return (java.math.BigInteger.ONE).compareTo(java.math.BigInteger.valueOf((x).length())) <= 0;
  }
  public static boolean IsValid__ReplicaGlobalSecondaryIndexList(dafny.DafnySequence<? extends ReplicaGlobalSecondaryIndex> x) {
    return (java.math.BigInteger.ONE).compareTo(java.math.BigInteger.valueOf((x).length())) <= 0;
  }
  public static boolean IsValid__ReplicaGlobalSecondaryIndexSettingsUpdateList(dafny.DafnySequence<? extends ReplicaGlobalSecondaryIndexSettingsUpdate> x) {
    return ((java.math.BigInteger.ONE).compareTo(java.math.BigInteger.valueOf((x).length())) <= 0) && ((java.math.BigInteger.valueOf((x).length())).compareTo(java.math.BigInteger.valueOf(20L)) <= 0);
  }
  public static boolean IsValid__ReplicaSettingsUpdateList(dafny.DafnySequence<? extends ReplicaSettingsUpdate> x) {
    return ((java.math.BigInteger.ONE).compareTo(java.math.BigInteger.valueOf((x).length())) <= 0) && ((java.math.BigInteger.valueOf((x).length())).compareTo(java.math.BigInteger.valueOf(50L)) <= 0);
  }
  public static boolean IsValid__ReplicationGroupUpdateList(dafny.DafnySequence<? extends ReplicationGroupUpdate> x) {
    return (java.math.BigInteger.ONE).compareTo(java.math.BigInteger.valueOf((x).length())) <= 0;
  }
  public static boolean IsValid__ResourceArnString(dafny.DafnySequence<? extends Character> x) {
    return ((java.math.BigInteger.ONE).compareTo(java.math.BigInteger.valueOf((x).length())) <= 0) && ((java.math.BigInteger.valueOf((x).length())).compareTo(java.math.BigInteger.valueOf(1283L)) <= 0);
  }
  public static boolean IsValid__S3Bucket(dafny.DafnySequence<? extends Character> x) {
    return ((java.math.BigInteger.valueOf((x).length())).signum() != -1) && ((java.math.BigInteger.valueOf((x).length())).compareTo(java.math.BigInteger.valueOf(255L)) <= 0);
  }
  public static boolean IsValid__S3Prefix(dafny.DafnySequence<? extends Character> x) {
    return ((java.math.BigInteger.valueOf((x).length())).signum() != -1) && ((java.math.BigInteger.valueOf((x).length())).compareTo(java.math.BigInteger.valueOf(1024L)) <= 0);
  }
  public static boolean IsValid__S3SseKmsKeyId(dafny.DafnySequence<? extends Character> x) {
    return ((java.math.BigInteger.ONE).compareTo(java.math.BigInteger.valueOf((x).length())) <= 0) && ((java.math.BigInteger.valueOf((x).length())).compareTo(java.math.BigInteger.valueOf(2048L)) <= 0);
  }
  public static boolean IsValid__ScanSegment(int x) {
    return (java.lang.Integer.signum((x)) != -1) && ((x) <= (999999));
  }
  public static boolean IsValid__ScanTotalSegments(int x) {
    return ((1) <= (x)) && ((x) <= (1000000));
  }
  public static boolean IsValid__StreamArn(dafny.DafnySequence<? extends Character> x) {
    return ((java.math.BigInteger.valueOf(37L)).compareTo(java.math.BigInteger.valueOf((x).length())) <= 0) && ((java.math.BigInteger.valueOf((x).length())).compareTo(java.math.BigInteger.valueOf(1024L)) <= 0);
  }
  public static boolean IsValid__TableArn(dafny.DafnySequence<? extends Character> x) {
    return ((java.math.BigInteger.ONE).compareTo(java.math.BigInteger.valueOf((x).length())) <= 0) && ((java.math.BigInteger.valueOf((x).length())).compareTo(java.math.BigInteger.valueOf(1024L)) <= 0);
  }
  public static boolean IsValid__TableName(dafny.DafnySequence<? extends Character> x) {
    return ((java.math.BigInteger.valueOf(3L)).compareTo(java.math.BigInteger.valueOf((x).length())) <= 0) && ((java.math.BigInteger.valueOf((x).length())).compareTo(java.math.BigInteger.valueOf(255L)) <= 0);
  }
  public static boolean IsValid__TagKeyString(dafny.DafnySequence<? extends Character> x) {
    return ((java.math.BigInteger.ONE).compareTo(java.math.BigInteger.valueOf((x).length())) <= 0) && ((java.math.BigInteger.valueOf((x).length())).compareTo(java.math.BigInteger.valueOf(128L)) <= 0);
  }
  public static boolean IsValid__TagValueString(dafny.DafnySequence<? extends Character> x) {
    return ((java.math.BigInteger.valueOf((x).length())).signum() != -1) && ((java.math.BigInteger.valueOf((x).length())).compareTo(java.math.BigInteger.valueOf(256L)) <= 0);
  }
  public static boolean IsValid__TimeToLiveAttributeName(dafny.DafnySequence<? extends Character> x) {
    return ((java.math.BigInteger.ONE).compareTo(java.math.BigInteger.valueOf((x).length())) <= 0) && ((java.math.BigInteger.valueOf((x).length())).compareTo(java.math.BigInteger.valueOf(255L)) <= 0);
  }
  public static boolean IsValid__TransactGetItemList(dafny.DafnySequence<? extends TransactGetItem> x) {
    return ((java.math.BigInteger.ONE).compareTo(java.math.BigInteger.valueOf((x).length())) <= 0) && ((java.math.BigInteger.valueOf((x).length())).compareTo(java.math.BigInteger.valueOf(100L)) <= 0);
  }
  public static boolean IsValid__TransactWriteItemList(dafny.DafnySequence<? extends TransactWriteItem> x) {
    return ((java.math.BigInteger.ONE).compareTo(java.math.BigInteger.valueOf((x).length())) <= 0) && ((java.math.BigInteger.valueOf((x).length())).compareTo(java.math.BigInteger.valueOf(100L)) <= 0);
  }
  public static boolean IsValid__WriteRequests(dafny.DafnySequence<? extends WriteRequest> x) {
    return ((java.math.BigInteger.ONE).compareTo(java.math.BigInteger.valueOf((x).length())) <= 0) && ((java.math.BigInteger.valueOf((x).length())).compareTo(java.math.BigInteger.valueOf(25L)) <= 0);
  }
  public static boolean IsDummySubsetType(java.math.BigInteger x) {
    return (x).signum() == 1;
  }
  @Override
  public java.lang.String toString() {
    return "ComAmazonawsDynamodbTypes._default";
  }
}
