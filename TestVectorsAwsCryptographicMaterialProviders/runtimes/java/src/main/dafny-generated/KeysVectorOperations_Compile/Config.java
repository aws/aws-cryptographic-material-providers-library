// Class Config
// Dafny class Config compiled into Java
package KeysVectorOperations_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class Config {
  public dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends KeyMaterial_Compile.KeyMaterial> _keys;
  public JSON_mValues_Compile.JSON _keysJson;
  public Config (dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends KeyMaterial_Compile.KeyMaterial> keys, JSON_mValues_Compile.JSON keysJson) {
    this._keys = keys;
    this._keysJson = keysJson;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    Config o = (Config)other;
    return true && java.util.Objects.equals(this._keys, o._keys) && java.util.Objects.equals(this._keysJson, o._keysJson);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._keys);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._keysJson);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("KeysVectorOperations.Config.Config");
    s.append("(");
    s.append(dafny.Helpers.toString(this._keys));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._keysJson));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<Config> _TYPE = dafny.TypeDescriptor.<Config>referenceWithInitializer(Config.class, () -> Config.Default());
  public static dafny.TypeDescriptor<Config> _typeDescriptor() {
    return (dafny.TypeDescriptor<Config>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final Config theDefault = Config.create(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>,KeyMaterial_Compile.KeyMaterial> empty(), JSON_mValues_Compile.JSON.Default());
  public static Config Default() {
    return theDefault;
  }
  public static Config create(dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends KeyMaterial_Compile.KeyMaterial> keys, JSON_mValues_Compile.JSON keysJson) {
    return new Config(keys, keysJson);
  }
  public static Config create_Config(dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends KeyMaterial_Compile.KeyMaterial> keys, JSON_mValues_Compile.JSON keysJson) {
    return create(keys, keysJson);
  }
  public boolean is_Config() { return true; }
  public dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends KeyMaterial_Compile.KeyMaterial> dtor_keys() {
    return this._keys;
  }
  public JSON_mValues_Compile.JSON dtor_keysJson() {
    return this._keysJson;
  }
}
