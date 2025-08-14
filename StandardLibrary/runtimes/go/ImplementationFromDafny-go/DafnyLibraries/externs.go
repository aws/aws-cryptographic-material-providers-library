package DafnyLibraries

import (
	sync "sync"

	Std_Wrappers "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/Wrappers"
	_dafny "github.com/dafny-lang/DafnyRuntimeGo/v4/dafny"
)

// Definition of class MutableMap copied over from
// https://github.com/robin-aws/dafny/blob/2a6f6db373ab09e16eb2aeb67c90cabfb8957907/Source/DafnyStandardLibraries/src/Std_Concurrent/Std_Concurrent.go
type MutableMap struct {
	// Default implementation - synchronized Dafny map<K, V>,
	// which is just a list of key-value pairs
	// with O(n) lookup.
	mu            sync.Mutex
	dafnyInternal _dafny.Map

	// Optimized for seq<bytes>
	// The Dafny byte sequences are converted to Go strings,
	// which can contain arbitrary bytes,
	// and are comparable and hence can be used as map keys,
	// whereas a Go byte array cannot.
	goInternal sync.Map

	// Switch to control which is active
	bytesKeys bool
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

func (_this *MutableMap) Ctor__(bytesKeys bool) {
	{
		_this.bytesKeys = bytesKeys
	}
}

// Converts a Dafny seq<byte> to a Go string,
// which can contain artibitrary bytes.
func dafnyBytesToGoString(b interface{}) string {
	return string(_dafny.ToByteArray(b.(_dafny.Sequence)))
}

// Converts a Dafny seq<byte> from a Go string,
// which can contain artibitrary bytes.
func dafnyBytesFromGoString(b interface{}) _dafny.Sequence {
	return _dafny.SeqOfBytes([]byte(b.(string)))
}

func (_this *MutableMap) Keys() _dafny.Set {
	{
		if _this.bytesKeys {
			keys := make([]interface{}, 0)

			_this.goInternal.Range(func(key, value interface{}) bool {
				keys = append(keys, dafnyBytesFromGoString(key))
				return true
			})

			return _dafny.SetOf(keys[:]...)
		} else {
			_this.mu.Lock()
			defer _this.mu.Unlock()

			return _this.dafnyInternal.Keys()
		}
	}
}
func (_this *MutableMap) HasKey(k interface{}) bool {
	{
		if _this.bytesKeys {
			_, ok := _this.goInternal.Load(dafnyBytesToGoString(k))
			return ok
		} else {
			_this.mu.Lock()
			defer _this.mu.Unlock()

			return _this.dafnyInternal.Contains(k)
		}
	}
}
func (_this *MutableMap) Values() _dafny.Set {
	{
		if _this.bytesKeys {
			values := make([]interface{}, 0)

			_this.goInternal.Range(func(key, value interface{}) bool {
				values = append(values, value)
				return true
			})

			return _dafny.SetOf(values[:]...)
		} else {
			_this.mu.Lock()
			defer _this.mu.Unlock()

			return _this.dafnyInternal.Values()
		}
	}
}
func (_this *MutableMap) Items() _dafny.Set {
	{
		if _this.bytesKeys {
			items := make([]interface{}, 0)

			_this.goInternal.Range(func(key, value interface{}) bool {
				items = append(items, _dafny.TupleOf(dafnyBytesFromGoString(key), value))
				return true
			})

			return _dafny.SetOf(items[:]...)
		} else {
			_this.mu.Lock()
			defer _this.mu.Unlock()

			return _this.dafnyInternal.Items()
		}
	}
}
func (_this *MutableMap) Get(k interface{}) Std_Wrappers.Option {
	{
		if _this.bytesKeys {
			value, ok := _this.goInternal.Load(dafnyBytesToGoString(k))
			if ok {
				return Std_Wrappers.Companion_Option_.Create_Some_(value)
			} else {
				return Std_Wrappers.Companion_Option_.Create_None_()
			}
		} else {
			_this.mu.Lock()
			defer _this.mu.Unlock()

			value, ok := _this.dafnyInternal.Find(k)
			if ok {
				return Std_Wrappers.Companion_Option_.Create_Some_(value)
			} else {
				return Std_Wrappers.Companion_Option_.Create_None_()
			}
		}
	}
}
func (_this *MutableMap) Put(k interface{}, v interface{}) {
	if _this.bytesKeys {
		_this.goInternal.Store(dafnyBytesToGoString(k), v)
	} else {
		_this.mu.Lock()
		defer _this.mu.Unlock()

		_this.dafnyInternal = _this.dafnyInternal.UpdateUnsafe(k, v)
	}
}
func (_this *MutableMap) Remove(k interface{}) {
	{
		if _this.bytesKeys {
			_this.goInternal.Delete(dafnyBytesToGoString(k))
		} else {
			_this.mu.Lock()
			defer _this.mu.Unlock()

			// This could be special-cased for a single remove to be a bit faster,
			// but it's still going to be O(n) so likely not worth it.
			_this.dafnyInternal = _this.dafnyInternal.Subtract(_dafny.SetOf(k))
		}
	}
}
func (_this *MutableMap) Size() _dafny.Int {
	{
		if _this.bytesKeys {
			var c _dafny.Int = _dafny.Zero

			_this.goInternal.Range(func(key, value interface{}) bool {
				c = c.Plus(_dafny.One)
				return true
			})

			return c
		} else {
			_this.mu.Lock()
			defer _this.mu.Unlock()

			return _this.dafnyInternal.Cardinality()
		}
	}
}

// End of class MutableMap

// This is handrolled extern
func (_this *MutableMap) Select(k interface{}) interface{} {
	r := _this.Get(k)
	if r.Is_None() {
		return nil
	}
	return r.Dtor_value()
}
