"""Main app package."""

try:
    from app import pretty

    pretty.full()
except ImportError:
    pass
