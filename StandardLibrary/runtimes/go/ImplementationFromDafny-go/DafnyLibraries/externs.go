package DafnyLibraries

import "github.com/dafny-lang/DafnyRuntimeGo/dafny"

// TODO: Do we even need this struct? Why not use dafnyMap directly?
type NativeMutableMap struct {
	MutableMapTrait
	dafnyMap dafny.Map
}

var staticMap = NativeMutableMap{
	MutableMapTrait: New_MutableMap_(),
	dafnyMap:        dafny.EmptyMap,
}

func (*MutableMap) Content() dafny.Map {
	return staticMap.dafnyMap
}
func (*MutableMap) HasKey(k interface{}) bool {
	return staticMap.dafnyMap.Contains(k)
}
func (*MutableMap) Select(k interface{}) interface{} {
	return staticMap.dafnyMap.Get(k)
}
func (*MutableMap) Items() dafny.Set {
	return staticMap.dafnyMap.Items()
}

func (*MutableMap) Keys() dafny.Set {
	return staticMap.dafnyMap.Keys()
}
func (*MutableMap) Put(k interface{}, v interface{}) {
	staticMap.dafnyMap.Update(k, v)
}
func (*MutableMap) Remove(k interface{}) {
	staticMap.dafnyMap.Subtract(dafny.SetOf(k))
}
func (*MutableMap) Size() dafny.Int {
	return staticMap.dafnyMap.Cardinality()
}
func (*MutableMap) Values() dafny.Set {
	return staticMap.dafnyMap.Values()
}
