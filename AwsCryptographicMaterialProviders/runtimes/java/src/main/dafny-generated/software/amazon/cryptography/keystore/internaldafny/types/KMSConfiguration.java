// Class KMSConfiguration
// Dafny class KMSConfiguration compiled into Java
package software.amazon.cryptography.keystore.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public abstract class KMSConfiguration {
  public KMSConfiguration() {
  }
  private static final dafny.TypeDescriptor<KMSConfiguration> _TYPE = dafny.TypeDescriptor.<KMSConfiguration>referenceWithInitializer(KMSConfiguration.class, () -> KMSConfiguration.Default());
  public static dafny.TypeDescriptor<KMSConfiguration> _typeDescriptor() {
    return (dafny.TypeDescriptor<KMSConfiguration>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final KMSConfiguration theDefault = software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration.create_kmsKeyArn(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
  public static KMSConfiguration Default() {
    return theDefault;
  }
  public static KMSConfiguration create_kmsKeyArn(dafny.DafnySequence<? extends Character> kmsKeyArn) {
    return new KMSConfiguration_kmsKeyArn(kmsKeyArn);
  }
  public static KMSConfiguration create_kmsMRKeyArn(dafny.DafnySequence<? extends Character> kmsMRKeyArn) {
    return new KMSConfiguration_kmsMRKeyArn(kmsMRKeyArn);
  }
  public static KMSConfiguration create_discovery(Discovery discovery) {
    return new KMSConfiguration_discovery(discovery);
  }
  public static KMSConfiguration create_mrDiscovery(MRDiscovery mrDiscovery) {
    return new KMSConfiguration_mrDiscovery(mrDiscovery);
  }
  public boolean is_kmsKeyArn() { return this instanceof KMSConfiguration_kmsKeyArn; }
  public boolean is_kmsMRKeyArn() { return this instanceof KMSConfiguration_kmsMRKeyArn; }
  public boolean is_discovery() { return this instanceof KMSConfiguration_discovery; }
  public boolean is_mrDiscovery() { return this instanceof KMSConfiguration_mrDiscovery; }
  public dafny.DafnySequence<? extends Character> dtor_kmsKeyArn() {
    KMSConfiguration d = this;
    return ((KMSConfiguration_kmsKeyArn)d)._kmsKeyArn;
  }
  public dafny.DafnySequence<? extends Character> dtor_kmsMRKeyArn() {
    KMSConfiguration d = this;
    return ((KMSConfiguration_kmsMRKeyArn)d)._kmsMRKeyArn;
  }
  public Discovery dtor_discovery() {
    KMSConfiguration d = this;
    return ((KMSConfiguration_discovery)d)._discovery;
  }
  public MRDiscovery dtor_mrDiscovery() {
    KMSConfiguration d = this;
    return ((KMSConfiguration_mrDiscovery)d)._mrDiscovery;
  }
}
