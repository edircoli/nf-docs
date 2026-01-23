"""
Progress reporting for nf-docs extraction.

This module provides a callback-based progress reporting system that can be
used with rich.Progress or any other progress display mechanism.
"""

from collections.abc import Callable
from dataclasses import dataclass
from enum import Enum, auto
from typing import Protocol


class ExtractionPhase(Enum):
    """Phases of the extraction process."""

    STARTING = auto()
    CHECKING_CACHE = auto()
    PARSING_SCHEMA = auto()
    PARSING_CONFIG = auto()
    PARSING_README = auto()
    LSP_STARTING = auto()
    LSP_INITIALIZING = auto()
    LSP_INDEXING = auto()
    LSP_SCANNING_FILES = auto()
    LSP_EXTRACTING_SYMBOLS = auto()
    LSP_STOPPING = auto()
    FINALIZING = auto()
    COMPLETE = auto()


@dataclass
class ProgressUpdate:
    """A progress update message."""

    phase: ExtractionPhase
    message: str
    current: int | None = None
    total: int | None = None
    detail: str | None = None

    @property
    def has_progress(self) -> bool:
        """Whether this update has numeric progress information."""
        return self.current is not None and self.total is not None

    @property
    def percent(self) -> float | None:
        """Get progress as a percentage, or None if not applicable."""
        if self.current is not None and self.total is not None and self.total > 0:
            return (self.current / self.total) * 100
        return None


class ProgressCallback(Protocol):
    """Protocol for progress callback functions."""

    def __call__(self, update: ProgressUpdate) -> None:
        """
        Called when progress is updated.

        Args:
            update: The progress update information
        """
        ...


# Type alias for the callback
ProgressCallbackType = Callable[[ProgressUpdate], None]


def null_progress(update: ProgressUpdate) -> None:
    """A no-op progress callback for when progress reporting is not needed."""
    pass
