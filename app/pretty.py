"""Prettier stacktrace."""
try:
    import pretty_errors  # type: ignore
except ImportError:
    pass


def simple():
    """Set simple and pretty stacktrace."""
    try:
        pretty_errors.configure(
            separator_character="*",
            filename_display=pretty_errors.FILENAME_EXTENDED,
            line_number_first=True,
            display_link=True,
            line_color=pretty_errors.RED + "> " + pretty_errors.default_config.line_color,
            code_color="  " + pretty_errors.default_config.line_color,
            truncate_code=True,
            display_locals=True,
        )
    except NameError:
        pass


def full():
    """Set more verbose stacktrace."""
    try:
        pretty_errors.configure(
            separator_character="*",
            filename_display=pretty_errors.FILENAME_EXTENDED,
            line_number_first=True,
            display_link=True,
            lines_before=5,
            lines_after=2,
            line_color=pretty_errors.RED + "> " + pretty_errors.default_config.line_color,
            code_color="  " + pretty_errors.default_config.line_color,
            truncate_code=True,
            display_locals=True,
            display_trace_locals=True,
        )
    except NameError:
        pass
