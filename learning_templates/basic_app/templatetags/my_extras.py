from django import template

register = template.library()

# value and string argument arg
@register.filter(name='cut')
def cut(value,arg):
    """
    This cuts out all values of args from the string
    """
    return value.replace(arg,'')

# register all that you have made. filter(what u want to call this filter, function name)
# register.filter('cut',cut)
# do it using decorators
