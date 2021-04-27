import numbers, math, decimal

def format_duration(num_seconds):
    time_units = (dict(divider=1, singular='second', plural='seconds'), 
                  dict(divider=60, singular='minute', plural='minutes'),
                  dict(divider=60 * 60, singular='hour', plural='hours'),
                  dict(divider=60 * 60 * 24, singular='day', plural='days'),
                  dict(divider=60 * 60 * 24 * 365, singular='year', plural='years'))
                  
    def pluralize(count, singular, plural=None):
        if not plural:
            plural = singular + 's'
        return '%s %s' % (count, singular if count == 1 else plural)
    
    def concatenate(items):
        items = list(items)
        if len(items) > 1:
            return ', '.join(items[:-1]) + ' and ' + items[-1]
        elif items:
            return items[0]
        else:
            return ''
    
    if not num_seconds:
        return 'now'
    if num_seconds < 60:
        return pluralize(num_seconds, 'second')
    else:
        result = []
        relevant_units = list(reversed(time_units))
        for unit in relevant_units:
            divider = decimal.Decimal(str(unit['divider']))
            count = num_seconds / divider
            num_seconds %= divider
            if unit != relevant_units[-1]:
                count = int(count)
            if count:
                result.append(pluralize(count, unit['singular'], unit['plural']))
    return concatenate(result)