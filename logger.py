import logging
from datetime import datetime


class ConsoleLogger:
  def __init__(self, name: str):
    self.name = name

  def debug(self, message: str):
    self._print(message, 1)

  def log(self, message: str):
    self._print(message)

  def error(self, message: str):
    self._print(message, 3)

  def _print(self, message: str, log_type: int = 2):
    try:
      log_levels = {
        1: logging.DEBUG,
        2: logging.INFO,
        3: logging.ERROR
      }
      
      level = log_levels.get(log_type, logging.INFO)
      
      print(f"[{datetime.now().strftime('%Y/%m/%dT%H:%M:%S')}][{logging.getLevelName(level)}]: {self.name} - {message}")
    except Exception as e:
      print(f"Error: {e}")


console_logger = ConsoleLogger("Test")

console_logger.log('Hello World')
console_logger.error('Error at line 18')
console_logger.debug('Its working')