import aws_cryptographic_materialproviders.internaldafny.generated.StormTracker

class StormTracker(aws_cryptographic_materialproviders.internaldafny.generated.StormTracker.StormTracker):

    # store generated ctor__ as base,
    # so that when we overwrite the generated class with the extern class,
    # we can still refer to it.
    base_ctor = aws_cryptographic_materialproviders.internaldafny.generated.StormTracker.StormTracker.ctor__

    def ctor__(self, cache):
        if cache.fanOut > 1:
            raise ValueError("StormTracker cache fanOut cannot be greater than 1.")
        self.base_ctor(cache)

aws_cryptographic_materialproviders.internaldafny.generated.StormTracker.StormTracker = StormTracker