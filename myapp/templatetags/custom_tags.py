from django import template
register = template.Library()

@register.filter(name="remove_specials")
def remove_chars(value, arg):
#    print('value', value)
#    print('arg', arg)
   for character in arg:
     value = value.replace(character, "")
   return value