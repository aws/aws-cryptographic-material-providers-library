package software.amazon.cryptography.example;

import java.util.Map;
import org.apache.commons.collections4.MapUtils;
import software.amazon.awssdk.utils.ImmutableMap;

public class Constants {

  public static final String BRANCH_KEY_ID = "branch-key-id";
  public static final String TYPE = "type";
  public static final String CREATE_TIME = "create-time";
  public static final String TYPE_MUTATION_COMMITMENT =
    "branch:MUTATION_COMMITMENT";
  public static final String TYPE_MUTATION_INDEX = "branch:MUTATION_INDEX";
  public static final String TYPE_ACTIVE = "branch:ACTIVE";
  public static final String TYPE_VERSION = "branch:version:";
  public static final String TYPE_BEACON = "beacon:ACTIVE";
  public static final Map<String, String> DEFAULT_ENCRYPTION_CONTEXT =
    ImmutableMap.<String, String>builder().put("Robbie", "Is a Dog.").build();
}
