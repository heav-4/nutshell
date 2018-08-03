from cli import ARGS

RAND_SEED = 83_523


def _printv(*stuff, pre='  ', **kwargs):
    """
    val: Thing to print.
    pre: What to prepend to val on print.
    **kwargs: Passed to printq()
    """
    for val in filter(None, stuff):
        printq(*(f'{pre}{i}' for i in (val if type(val) is list else [val])), **kwargs)


def printv(*args, start='\n', end=None, accum=True, **kwargs):
    """
    *args: Things to print, ordered by level of verbosity. Group items using a list.
    start: What to print before anything else.
    accum: Whether to print everything up to VERBOSITY or just the item at VERBOSITY
    **kwargs: Passed to _printv()
    """
    if not ARGS.verbosity:
        return
    if any(args[:ARGS.verbosity]):
        printq(start, end='')
    if accum:
        _printv(*args[:ARGS.verbosity-1], **kwargs)
    try:
        _printv(args[ARGS.verbosity-1], end=end, **kwargs)
    except IndexError:
        pass


def printq(*args, **kwargs):
    if ARGS.quiet:
        return
    print(*args, **kwargs)
