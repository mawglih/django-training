from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value,arg):
  """
  Cuts all vals of arg frim the string
  """

  return value.replace(arg,'')

# register.filter('cut',cut)