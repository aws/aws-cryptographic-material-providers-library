# TODO-Python-PYTHONPATH: Extend generated class.
# This copy-paste of generated code resolves a circular import,
# but should be able to be removed as part of PYTHONPATH system removal.
class Callee:
    pass
    def call(self, serialPos, concurrentPos):
        pass

from threading import Thread

class default__:
    @staticmethod
    def ConcurrentCall(callee, serial_iters, concurrent_iters):
        thread_list = []
        for i in range(0, concurrent_iters):
            local_num = i
            thread_list.append(
                Thread(target=default__._executor_call, args=(callee, serial_iters, local_num))
            )

        for i in range(0, concurrent_iters):
            thread_list[i].start()

        for i in range(0, concurrent_iters):
            thread_list[i].join()

    def _executor_call(callee, serial_iters, local_num):
        for j in range(0, serial_iters):
            print("doing the thing")
            callee.call(j, local_num)
