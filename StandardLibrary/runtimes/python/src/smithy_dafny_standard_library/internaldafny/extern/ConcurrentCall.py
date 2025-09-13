import smithy_dafny_standard_library.internaldafny.generated.ConcurrentCall

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
            callee.call(j, local_num)

smithy_dafny_standard_library.internaldafny.generated.ConcurrentCall.default__ = default__