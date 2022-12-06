import time
import tracemalloc

from taxifare.ml_logic.params import DATASET_SIZE

def get_dataset_timestamp(df=None):
    """
    Retrieve the date of the latest available datapoint, at monthly granularity
    """

    import pandas as pd
    from taxifare.ml_logic.data import get_chunk

    if df is None:
        # Trick specific to this taxifare challenge:
        # Query simply one row from the TRAIN_DATASET, it's enough to deduce the latest datapoint available
        df = get_chunk(source_name=f"train_{DATASET_SIZE}",
                       index=0,
                       chunk_size=1,
                       verbose=False)

    # retrieve first row timestamp
    ts = pd.to_datetime(df.pickup_datetime[:1])[0]

    if ts.year < 2015:
        # Trick specific to this taxifare challenge:
        # We can consider all past training dataset to stop at 2014-12.
        # New datapoints will start to be collected month by month starting 2015-01
        ts = ts.replace(year=2014, month=12)

    # adjust date to monthly granularity
    ts = ts.replace(day=1, hour=0, minute=0, second=0, microsecond=0, nanosecond=0)

    return ts


def simple_time_and_memory_tracker(method):

    # ### Log Level
    # 0: Nothing
    # 1: Print Time and Memory usage of functions
    LOG_LEVEL = 1

    def method_with_trackers(*args, **kw):
        ts = time.time()
        tracemalloc.start()
        result = method(*args, **kw)
        _, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        te = time.time()
        duration = te - ts
        if LOG_LEVEL > 0:
            output = f"{method.__qualname__} executed in {round(duration, 2)} seconds, using up to {round(peak / 1024**2,2)}MB of RAM"
            print(output)
        return result

    return method_with_trackers
