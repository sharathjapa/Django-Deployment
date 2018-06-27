from django import template

register = template.Library()

@register.filter(name='chop')
def chop(value, arg):
    """
    This cuts all values of "arg" from the string!
    """
    return value.replace(arg,'')


#register.filter('chop',chop) #name for the custom filter, method for the custom filter
