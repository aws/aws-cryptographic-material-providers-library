package ConcurrentCall

import "sync"

func ConcurrentCall(calle Callee, serialIters uint32, concurrentIters uint32) {
	var wg sync.WaitGroup
	for i := uint32(0); i < concurrentIters; i++ {
		wg.Add(1)
		concurrentPos := i
		go func() {
			defer wg.Done()
			for j := uint32(0); j < serialIters; j++ {
				calle.Call(j, concurrentPos)
			}
		}()
		wg.Wait()
	}
}
