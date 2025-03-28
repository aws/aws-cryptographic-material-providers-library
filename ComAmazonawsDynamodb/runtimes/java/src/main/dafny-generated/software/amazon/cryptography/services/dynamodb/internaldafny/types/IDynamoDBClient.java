// Interface IDynamoDBClient
// Dafny trait IDynamoDBClient compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public interface IDynamoDBClient {
  public Wrappers_Compile.Result<BatchExecuteStatementOutput, Error> BatchExecuteStatement(BatchExecuteStatementInput input);
  public Wrappers_Compile.Result<BatchGetItemOutput, Error> BatchGetItem(BatchGetItemInput input);
  public Wrappers_Compile.Result<BatchWriteItemOutput, Error> BatchWriteItem(BatchWriteItemInput input);
  public Wrappers_Compile.Result<CreateBackupOutput, Error> CreateBackup(CreateBackupInput input);
  public Wrappers_Compile.Result<CreateGlobalTableOutput, Error> CreateGlobalTable(CreateGlobalTableInput input);
  public Wrappers_Compile.Result<CreateTableOutput, Error> CreateTable(CreateTableInput input);
  public Wrappers_Compile.Result<DeleteBackupOutput, Error> DeleteBackup(DeleteBackupInput input);
  public Wrappers_Compile.Result<DeleteItemOutput, Error> DeleteItem(DeleteItemInput input);
  public Wrappers_Compile.Result<DeleteResourcePolicyOutput, Error> DeleteResourcePolicy(DeleteResourcePolicyInput input);
  public Wrappers_Compile.Result<DeleteTableOutput, Error> DeleteTable(DeleteTableInput input);
  public Wrappers_Compile.Result<DescribeBackupOutput, Error> DescribeBackup(DescribeBackupInput input);
  public Wrappers_Compile.Result<DescribeContinuousBackupsOutput, Error> DescribeContinuousBackups(DescribeContinuousBackupsInput input);
  public Wrappers_Compile.Result<DescribeContributorInsightsOutput, Error> DescribeContributorInsights(DescribeContributorInsightsInput input);
  public Wrappers_Compile.Result<DescribeEndpointsResponse, Error> DescribeEndpoints(DescribeEndpointsRequest input);
  public Wrappers_Compile.Result<DescribeExportOutput, Error> DescribeExport(DescribeExportInput input);
  public Wrappers_Compile.Result<DescribeGlobalTableOutput, Error> DescribeGlobalTable(DescribeGlobalTableInput input);
  public Wrappers_Compile.Result<DescribeGlobalTableSettingsOutput, Error> DescribeGlobalTableSettings(DescribeGlobalTableSettingsInput input);
  public Wrappers_Compile.Result<DescribeImportOutput, Error> DescribeImport(DescribeImportInput input);
  public Wrappers_Compile.Result<DescribeKinesisStreamingDestinationOutput, Error> DescribeKinesisStreamingDestination(DescribeKinesisStreamingDestinationInput input);
  public Wrappers_Compile.Result<DescribeLimitsOutput, Error> DescribeLimits(DescribeLimitsInput input);
  public Wrappers_Compile.Result<DescribeTableOutput, Error> DescribeTable(DescribeTableInput input);
  public Wrappers_Compile.Result<DescribeTableReplicaAutoScalingOutput, Error> DescribeTableReplicaAutoScaling(DescribeTableReplicaAutoScalingInput input);
  public Wrappers_Compile.Result<DescribeTimeToLiveOutput, Error> DescribeTimeToLive(DescribeTimeToLiveInput input);
  public Wrappers_Compile.Result<DisableKinesisStreamingDestinationOutput, Error> DisableKinesisStreamingDestination(DisableKinesisStreamingDestinationInput input);
  public Wrappers_Compile.Result<EnableKinesisStreamingDestinationOutput, Error> EnableKinesisStreamingDestination(EnableKinesisStreamingDestinationInput input);
  public Wrappers_Compile.Result<ExecuteStatementOutput, Error> ExecuteStatement(ExecuteStatementInput input);
  public Wrappers_Compile.Result<ExecuteTransactionOutput, Error> ExecuteTransaction(ExecuteTransactionInput input);
  public Wrappers_Compile.Result<ExportTableToPointInTimeOutput, Error> ExportTableToPointInTime(ExportTableToPointInTimeInput input);
  public Wrappers_Compile.Result<GetItemOutput, Error> GetItem(GetItemInput input);
  public Wrappers_Compile.Result<GetResourcePolicyOutput, Error> GetResourcePolicy(GetResourcePolicyInput input);
  public Wrappers_Compile.Result<ImportTableOutput, Error> ImportTable(ImportTableInput input);
  public Wrappers_Compile.Result<ListBackupsOutput, Error> ListBackups(ListBackupsInput input);
  public Wrappers_Compile.Result<ListContributorInsightsOutput, Error> ListContributorInsights(ListContributorInsightsInput input);
  public Wrappers_Compile.Result<ListExportsOutput, Error> ListExports(ListExportsInput input);
  public Wrappers_Compile.Result<ListGlobalTablesOutput, Error> ListGlobalTables(ListGlobalTablesInput input);
  public Wrappers_Compile.Result<ListImportsOutput, Error> ListImports(ListImportsInput input);
  public Wrappers_Compile.Result<ListTablesOutput, Error> ListTables(ListTablesInput input);
  public Wrappers_Compile.Result<ListTagsOfResourceOutput, Error> ListTagsOfResource(ListTagsOfResourceInput input);
  public Wrappers_Compile.Result<PutItemOutput, Error> PutItem(PutItemInput input);
  public Wrappers_Compile.Result<PutResourcePolicyOutput, Error> PutResourcePolicy(PutResourcePolicyInput input);
  public Wrappers_Compile.Result<QueryOutput, Error> Query(QueryInput input);
  public Wrappers_Compile.Result<RestoreTableFromBackupOutput, Error> RestoreTableFromBackup(RestoreTableFromBackupInput input);
  public Wrappers_Compile.Result<RestoreTableToPointInTimeOutput, Error> RestoreTableToPointInTime(RestoreTableToPointInTimeInput input);
  public Wrappers_Compile.Result<ScanOutput, Error> Scan(ScanInput input);
  public Wrappers_Compile.Result<dafny.Tuple0, Error> TagResource(TagResourceInput input);
  public Wrappers_Compile.Result<TransactGetItemsOutput, Error> TransactGetItems(TransactGetItemsInput input);
  public Wrappers_Compile.Result<TransactWriteItemsOutput, Error> TransactWriteItems(TransactWriteItemsInput input);
  public Wrappers_Compile.Result<dafny.Tuple0, Error> UntagResource(UntagResourceInput input);
  public Wrappers_Compile.Result<UpdateContinuousBackupsOutput, Error> UpdateContinuousBackups(UpdateContinuousBackupsInput input);
  public Wrappers_Compile.Result<UpdateContributorInsightsOutput, Error> UpdateContributorInsights(UpdateContributorInsightsInput input);
  public Wrappers_Compile.Result<UpdateGlobalTableOutput, Error> UpdateGlobalTable(UpdateGlobalTableInput input);
  public Wrappers_Compile.Result<UpdateGlobalTableSettingsOutput, Error> UpdateGlobalTableSettings(UpdateGlobalTableSettingsInput input);
  public Wrappers_Compile.Result<UpdateItemOutput, Error> UpdateItem(UpdateItemInput input);
  public Wrappers_Compile.Result<UpdateKinesisStreamingDestinationOutput, Error> UpdateKinesisStreamingDestination(UpdateKinesisStreamingDestinationInput input);
  public Wrappers_Compile.Result<UpdateTableOutput, Error> UpdateTable(UpdateTableInput input);
  public Wrappers_Compile.Result<UpdateTableReplicaAutoScalingOutput, Error> UpdateTableReplicaAutoScaling(UpdateTableReplicaAutoScalingInput input);
  public Wrappers_Compile.Result<UpdateTimeToLiveOutput, Error> UpdateTimeToLive(UpdateTimeToLiveInput input);
}
