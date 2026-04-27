// Class Value
// Dafny class Value compiled into Java
package JSON_mGrammar_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class Value {
  public Value() {
  }
  private static final dafny.TypeDescriptor<Value> _TYPE = dafny.TypeDescriptor.<Value>referenceWithInitializer(Value.class, () -> Value.Default());
  public static dafny.TypeDescriptor<Value> _typeDescriptor() {
    return (dafny.TypeDescriptor<Value>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final Value theDefault = Value.create_Null(jnull.defaultValue());
  public static Value Default() {
    return theDefault;
  }
  public static Value create_Null(JSON_mUtils_mViews_mCore_Compile.View__ n) {
    return new Value_Null(n);
  }
  public static Value create_Bool(JSON_mUtils_mViews_mCore_Compile.View__ b) {
    return new Value_Bool(b);
  }
  public static Value create_String(jstring str) {
    return new Value_String(str);
  }
  public static Value create_Number(jnumber num) {
    return new Value_Number(num);
  }
  public static Value create_Object(Bracketed<JSON_mUtils_mViews_mCore_Compile.View__, jKeyValue, JSON_mUtils_mViews_mCore_Compile.View__, JSON_mUtils_mViews_mCore_Compile.View__> obj) {
    return new Value_Object(obj);
  }
  public static Value create_Array(Bracketed<JSON_mUtils_mViews_mCore_Compile.View__, Value, JSON_mUtils_mViews_mCore_Compile.View__, JSON_mUtils_mViews_mCore_Compile.View__> arr) {
    return new Value_Array(arr);
  }
  public boolean is_Null() { return this instanceof Value_Null; }
  public boolean is_Bool() { return this instanceof Value_Bool; }
  public boolean is_String() { return this instanceof Value_String; }
  public boolean is_Number() { return this instanceof Value_Number; }
  public boolean is_Object() { return this instanceof Value_Object; }
  public boolean is_Array() { return this instanceof Value_Array; }
  public JSON_mUtils_mViews_mCore_Compile.View__ dtor_n() {
    Value d = this;
    return ((Value_Null)d)._n;
  }
  public JSON_mUtils_mViews_mCore_Compile.View__ dtor_b() {
    Value d = this;
    return ((Value_Bool)d)._b;
  }
  public jstring dtor_str() {
    Value d = this;
    return ((Value_String)d)._str;
  }
  public jnumber dtor_num() {
    Value d = this;
    return ((Value_Number)d)._num;
  }
  public Bracketed<JSON_mUtils_mViews_mCore_Compile.View__, jKeyValue, JSON_mUtils_mViews_mCore_Compile.View__, JSON_mUtils_mViews_mCore_Compile.View__> dtor_obj() {
    Value d = this;
    return ((Value_Object)d)._obj;
  }
  public Bracketed<JSON_mUtils_mViews_mCore_Compile.View__, Value, JSON_mUtils_mViews_mCore_Compile.View__, JSON_mUtils_mViews_mCore_Compile.View__> dtor_arr() {
    Value d = this;
    return ((Value_Array)d)._arr;
  }
}
