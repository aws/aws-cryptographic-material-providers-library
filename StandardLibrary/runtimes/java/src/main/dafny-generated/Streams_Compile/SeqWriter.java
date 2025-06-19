// Class SeqWriter
// Dafny class SeqWriter compiled into Java
package Streams_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class SeqWriter<T> {
  protected dafny.TypeDescriptor<T> _td_T;
  public SeqWriter(dafny.TypeDescriptor<T> _td_T) {
    this._td_T = _td_T;
    this.data = dafny.DafnySequence.<T> empty(_td_T);
  }
  public dafny.DafnySequence<? extends T> data;
  public void __ctor()
  {
    (this).data = dafny.DafnySequence.<T> empty(_td_T);
  }
  public long WriteElements(dafny.DafnySequence<? extends T> elems)
  {
    long n = 0L;
    (this).data = dafny.DafnySequence.<T>concatenate(this.data, elems);
    n = (long) (elems).cardinalityInt();
    return n;
  }
  public static <T> dafny.TypeDescriptor<SeqWriter<T>> _typeDescriptor(dafny.TypeDescriptor<T> _td_T) {
    return (dafny.TypeDescriptor<SeqWriter<T>>) (dafny.TypeDescriptor<?>) dafny.TypeDescriptor.<SeqWriter<T>>referenceWithInitializer(SeqWriter.class, () -> (SeqWriter<T>) null);
  }
  @Override
  public java.lang.String toString() {
    return "Streams.SeqWriter";
  }
}
