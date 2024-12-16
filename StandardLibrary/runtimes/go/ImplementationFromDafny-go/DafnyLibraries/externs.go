package DafnyLibraries

import (
	sync "sync"

	_dafny "github.com/dafny-lang/DafnyRuntimeGo/v4/dafny"
	Std_Wrappers "github.com/dafny-lang/DafnyStandardLibGo/Wrappers"
)

// Definition of class MutableMap
type MutableMap struct {
	Internal sync.Map
}

func New_MutableMap_() *MutableMap {
	return &MutableMap{}
}

type CompanionStruct_MutableMap_ struct {
}

var Companion_MutableMap_ = CompanionStruct_MutableMap_{}

func (_this *MutableMap) Equals(other *MutableMap) bool {
	return _this == other
}

func (_this *MutableMap) EqualsGeneric(x interface{}) bool {
	other, ok := x.(*MutableMap)
	return ok && _this.Equals(other)
}

func (*MutableMap) String() string {
	return "ExternConcurrent.MutableMap"
}

func Type_MutableMap_(Type_K_ _dafny.TypeDescriptor, Type_V_ _dafny.TypeDescriptor) _dafny.TypeDescriptor {
	return type_MutableMap_{Type_K_, Type_V_}
}

type type_MutableMap_ struct {
	Type_K_ _dafny.TypeDescriptor
	Type_V_ _dafny.TypeDescriptor
}

func (_this type_MutableMap_) Default() interface{} {
	return (*MutableMap)(nil)
}

func (_this type_MutableMap_) String() string {
	return "ExternConcurrent.MutableMap"
}
func (_this *MutableMap) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = &MutableMap{}

func (_this *MutableMap) Ctor__() {
	{
	}
}
func (_this *MutableMap) Keys() _dafny.Set {
	{
		keys := make([]interface{}, 0)

		_this.Internal.Range(func(key, value interface{}) bool {
			keys = append(keys, key)
			return true
		})

		return _dafny.SetOf(keys[:]...)
	}
}
func (_this *MutableMap) HasKey(k interface{}) bool {
	{
		_, ok := _this.Internal.Load(k)
		return ok
	}
}
func (_this *MutableMap) Values() _dafny.Set {
	{
		values := make([]interface{}, 0)

		_this.Internal.Range(func(key, value interface{}) bool {
			values = append(values, value)
			return true
		})

		return _dafny.SetOf(values[:]...)
	}
}
func (_this *MutableMap) Items() _dafny.Set {
	{
		items := make([]interface{}, 0)

		_this.Internal.Range(func(key, value interface{}) bool {
			items = append(items, _dafny.TupleOf(key, value))
			return true
		})

		return _dafny.SetOf(items[:]...)
	}
}
func (_this *MutableMap) Select(k interface{}) interface{} {
	r := _this.Get(k)
	if r.Is_None() {
		return nil
	}
	return r.Dtor_value()
}
func (_this *MutableMap) Get(k interface{}) Std_Wrappers.Option {
	{
		value, ok := _this.Internal.Load(k)
		if ok {
			return Std_Wrappers.Companion_Option_.Create_Some_(value)
		} else {
			return Std_Wrappers.Companion_Option_.Create_None_()
		}
	}
}
func (_this *MutableMap) Put(k interface{}, v interface{}) {
	{
		_this.Internal.Store(k, v)
	}
}
func (_this *MutableMap) Remove(k interface{}) {
	{
		_this.Internal.Delete(k)
	}
}
func (_this *MutableMap) Size() _dafny.Int {
	{
		var c _dafny.Int = _dafny.Zero

		_this.Internal.Range(func(key, value interface{}) bool {
			c = c.Plus(_dafny.One)
			return true
		})

		return c
	}
}
