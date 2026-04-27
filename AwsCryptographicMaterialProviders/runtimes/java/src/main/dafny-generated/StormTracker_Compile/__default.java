// Class __default
// Dafny class __default compiled into Java
package StormTracker_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache DefaultStorm() {
    return software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache.create(1000, Wrappers_Compile.Option.<java.lang.Integer>create_Some(software.amazon.cryptography.materialproviders.internaldafny.types.CountingNumber._typeDescriptor(), 1), (int) ((10) * (1000)), (int) ((1) * (1000)), 20, (int) ((10) * (1000)), 20, Wrappers_Compile.Option.<software.amazon.cryptography.materialproviders.internaldafny.types.TimeUnits>create_Some(software.amazon.cryptography.materialproviders.internaldafny.types.TimeUnits._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.TimeUnits.create_Milliseconds()));
  }
  public static boolean ConsistentSettings(software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache cache) {
    return ((((cache).dtor_graceInterval()) <= ((cache).dtor_gracePeriod())) && (((cache).dtor_inFlightTTL()) <= ((cache).dtor_gracePeriod()))) && (((cache).dtor_graceInterval()) <= ((cache).dtor_inFlightTTL()));
  }
  public static dafny.DafnySequence<? extends Character> N(int n) {
    return StandardLibrary_mString_Compile.__default.Base10Int2String(java.math.BigInteger.valueOf(n));
  }
  public static dafny.DafnySequence<? extends Character> BadCacheMsg(software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache cache) {
    dafny.DafnySequence<? extends Character> _0_msg = dafny.DafnySequence.asString("For a StormCache : ");
    dafny.DafnySequence<? extends Character> _1_msg = dafny.DafnySequence.<Character>concatenate(_0_msg, ((!(((cache).dtor_graceInterval()) <= ((cache).dtor_gracePeriod()))) ? (dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("graceInterval must not exceed gracePeriod, yet configuration has graceInterval="), __default.N((cache).dtor_graceInterval())), dafny.DafnySequence.asString(" and gracePeriod=")), __default.N((cache).dtor_gracePeriod())), dafny.DafnySequence.asString(". "))) : (dafny.DafnySequence.asString(""))));
    dafny.DafnySequence<? extends Character> _2_msg = dafny.DafnySequence.<Character>concatenate(_1_msg, ((!(((cache).dtor_inFlightTTL()) <= ((cache).dtor_gracePeriod()))) ? (dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("inFlightTTL must not exceed gracePeriod, yet configuration has inFlightTTL="), __default.N((cache).dtor_inFlightTTL())), dafny.DafnySequence.asString(" and gracePeriod=")), __default.N((cache).dtor_gracePeriod())), dafny.DafnySequence.asString(". "))) : (dafny.DafnySequence.asString(""))));
    return _2_msg;
  }
  public static Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> CheckSettings(software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache cache) {
    if (__default.ConsistentSettings(cache)) {
      return Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Pass(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    } else {
      return Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Fail(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(__default.BadCacheMsg(cache)));
    }
  }
  @Override
  public java.lang.String toString() {
    return "StormTracker._default";
  }
}
