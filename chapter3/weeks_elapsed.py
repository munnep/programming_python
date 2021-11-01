def weeks_elapsed(day1: int, day2: int) -> int:
    """
    def weeks_elapsed(day1, day2): (int, int) -> int
    day1 and day2 are days in the same year. Return the number of full weeks
    that have elapsed between the two days.
    >>> weeks_elapsed(3, 20)
    2
    >>> weeks_elapsed(20, 3)
    2
    >>> weeks_elapsed(8, 5)
    >>> weeks_elapsed(40, 61)
    """
    max_day = max(day1, day2)
    min_day = min(day1, day2)
    days_in_between = max_day - min_day
    return days_in_between // 7

