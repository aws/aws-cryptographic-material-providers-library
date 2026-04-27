// Class __default
// Dafny class __default compiled into Java
package JSON_mUtils_mViews_mCore_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static boolean Adjacent(View__ lv, View__ rv)
  {
    return (((lv).dtor_end()) == ((rv).dtor_beg())) && (((lv).dtor_s()).equals((rv).dtor_s()));
  }
  public static View__ Merge(View__ lv, View__ rv)
  {
    View__ _0_dt__update__tmp_h0 = lv;
    int _1_dt__update_hend_h0 = (rv).dtor_end();
    return View__.create((_0_dt__update__tmp_h0).dtor_s(), (_0_dt__update__tmp_h0).dtor_beg(), _1_dt__update_hend_h0);
  }
  @Override
  public java.lang.String toString() {
    return "JSON.Utils.Views.Core._default";
  }
}
