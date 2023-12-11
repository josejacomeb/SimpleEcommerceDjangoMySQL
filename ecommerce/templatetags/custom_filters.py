from django.template import Library

register = Library()

@register.filter
def getattr_filter(obj, attr):
  """
  Applies the `getattr` method on the given object with the provided attribute.
  """
  print(obj, attr)
  
  return getattr(obj, attr)