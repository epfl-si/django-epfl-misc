# (c) ECOLE POLYTECHNIQUE FEDERALE DE LAUSANNE, Switzerland, VPSI, 2021.
# See the LICENSE file for more details.

from functools import wraps

from django.utils.decorators import available_attrs
from django.views.decorators.cache import cache_page


def cache_anonymous_user(timeout, cache="default"):
    """
    Decorator to make a multilanguage view cached for anonymous users.
    Usage::

        @cache_anonymous_user(60 * 15)
        def my_view(request):
            # I can assume now that the view is cached for anonymous users.
    """

    def decorator(view_func):
        @wraps(view_func, assigned=available_attrs(view_func))
        def _wrapped_view(request, *args, **kwargs):
            if request.user.is_authenticated:
                return view_func(request, *args, **kwargs)
            else:
                key_prefix = request.LANGUAGE_CODE + "_"
                return cache_page(timeout, key_prefix=key_prefix, cache=cache)(
                    view_func
                )(request, *args, **kwargs)

        return _wrapped_view

    return decorator