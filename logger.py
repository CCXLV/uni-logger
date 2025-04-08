from typing import Literal
import logging

from datetime import datetime

"""
  This is a simple logger class that logs messages to the console or a file.
"""
class Logger:
  def __init__(self, name: str, output: Literal["console", "file"] = "console"):
    self.name = name
    """This is the name of the logger."""
    self.output = output
    """This is the output of the logger."""

  def debug(self, message: str):
    """This is a debug message."""
    self._log(message, 1)

  def log(self, message: str):
    """This is a log message."""
    self._log(message)

  def error(self, message: str):
    """This is an error message."""
    self._log(message, 3)

  def _log(self, message: str, log_type: int = 2):
    """This is a main function that logs a message to the console or a file."""
    try:
      """This is a try block that logs a message to the console or a file."""
      log_levels = {
        1: logging.DEBUG,
        2: logging.INFO,
        3: logging.ERROR
      }

      """This is a level variable that gets the log level from the log_levels dictionary."""
      level = log_levels.get(log_type, logging.INFO)
      
      if self.output == "console":
        """This is a if statement that logs a message to the console."""
        print(f"[{datetime.now().strftime('%Y/%m/%dT%H:%M:%S')}][{logging.getLevelName(level)}]: {self.name} - {message}")
      elif self.output == "file":
        """This is a elif statement that logs a message to a file."""
        with open("log.txt", "a") as f:
          f.write(f"[{datetime.now().strftime('%Y/%m/%dT%H:%M:%S')}][{logging.getLevelName(level)}]: {self.name} - {message}\n")
    except Exception as e:
      print(f"Error: {e}")


"""This is a test of the logger."""
logger = Logger("Test", "file")

"""This is a test of the logger."""
logger.log('Hello World')
logger.error('Error at line 18')
logger.debug('Its working')