from typing import Literal
import logging

from datetime import datetime


class Logger:
  def __init__(self, name: str, output: Literal["console", "file"] = "console"):
    self.name = name
    self.output = output

  def debug(self, message: str):
    self._log(message, 1)

  def log(self, message: str):
    self._log(message)

  def error(self, message: str):
    self._log(message, 3)

  def _log(self, message: str, log_type: int = 2):
    try:
      log_levels = {
        1: logging.DEBUG,
        2: logging.INFO,
        3: logging.ERROR
      }
      
      level = log_levels.get(log_type, logging.INFO)
      
      if self.output == "console":
        print(f"[{datetime.now().strftime('%Y/%m/%dT%H:%M:%S')}][{logging.getLevelName(level)}]: {self.name} - {message}")
      elif self.output == "file":
        with open("log.txt", "a") as f:
          f.write(f"[{datetime.now().strftime('%Y/%m/%dT%H:%M:%S')}][{logging.getLevelName(level)}]: {self.name} - {message}\n")
    except Exception as e:
      print(f"Error: {e}")


logger = Logger("Test", "file")

logger.log('Hello World')
logger.error('Error at line 18')
logger.debug('Its working')