from import_export.widgets import(
    format_datetime,
    Widget,
)
from django.conf import settings
from datetime import date, datetime
from django.utils import timezone
import django


class BooleanWidget(Widget):
    TRUE_VALUES = ["1", 1, True, "true", "TRUE", "True"]
    FALSE_VALUES = ["0", 0, False, "false", "FALSE", "False"]
    NULL_VALUES = ["", None, "null", "NULL", "none", "NONE", "None"]

    def render(self, value, obj=None):
        """
        On export, ``True`` is represented as ``1``, ``False`` as ``0``, and
        ``None``/NULL as a empty string.

        Note that these values are also used on the import confirmation view.
        """
        if value in self.NULL_VALUES:
            return ""
        return self.TRUE_VALUES[2] if value else self.FALSE_VALUES[2]

    def clean(self, value, row=None, *args, **kwargs):
        if value in self.NULL_VALUES:
            return None
        return True if value in self.TRUE_VALUES else False


class CustomDateWidget(Widget):
    """
    Widget for converting date fields.

    Takes optional ``format`` parameter.
    """

    def __init__(self, format=None):
        if format is None:
            if not settings.DATE_INPUT_FORMATS:
                formats = ("%Y-%m-%d",)
            else:
                formats = settings.DATE_INPUT_FORMATS
        else:
            formats = (format,)
        self.formats = formats

    def clean(self, value, row=None, *args, **kwargs):
        if not value:
            return None
        if isinstance(value, date):
            return value
        for format in self.formats:
            try:
                return datetime.strptime(value, format).date()
            except (ValueError, TypeError):
                continue
        raise ValueError("Enter a valid date.")

    def render(self, value, obj=None):
        if not value:
            return ""
        return format_datetime(value, self.formats[0])


class CustomDateTimeWidget(Widget):
    """
    Widget for converting date fields.

    Takes optional ``format`` parameter. If none is set, either
    ``settings.DATETIME_INPUT_FORMATS`` or ``"%Y-%m-%d %H:%M:%S"`` is used.
    """

    def __init__(self, format=None):
        if format is None:
            if not settings.DATETIME_INPUT_FORMATS:
                formats = ("%Y-%m-%d %H:%M:%S",)
            else:
                formats = settings.DATETIME_INPUT_FORMATS
        else:
            formats = (format,)
        self.formats = formats

    def clean(self, value, row=None, *args, **kwargs):
        if not value:
            return None
        if isinstance(value, datetime):
            return value
        for format in self.formats:
            try:
                dt = datetime.strptime(value, format)
                if settings.USE_TZ:
                    # make datetime timezone aware so we don't compare
                    # naive datetime to an aware one
                    dt = timezone.make_aware(dt, timezone.get_default_timezone())
                return dt
            except (ValueError, TypeError):
                continue
        raise ValueError("Enter a valid date/time.")

    def render(self, value, obj=None):
        if not value:
            return ""
        if settings.USE_TZ:
            value = timezone.localtime(value)
        return format_datetime(value, self.formats[0])