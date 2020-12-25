import os, re

class Console():
   @staticmethod
   def move_cursor(x, y):
      print(f'\033[{y+1};{x+1}f', end='')
      
   @staticmethod
   def cls():
      os.system('clear' if os.name == 'posix' else 'cls')
   

class FormatString(str):
   END = '\033[0m'
   UP = '\033[1A'
   
   def __init__(self, string) -> None:
      super(str, string)
      
   def _format(self, n):
      return FormatString(f'\033[{n}m' + self + FormatString.END)
   
   @property
   def header(self): 
      return self._format(95)
   @property
   def blue(self): 
      return self._format(94)
   @property
   def cyan(self): 
      return self._format(96)
   @property
   def green(self): 
      return self._format(92)
   @property
   def warning(self): 
      return self._format(93)
   @property
   def fail(self): 
      return self._format(91)
   @property
   def bold(self): 
      return self._format(1)
   @property
   def underline(self): 
      return self._format(4)
   @property
   def normal(self):
      return self
   
class sstr(str):
   TAGS = {
      'bold': 'bold',
      'underline': 'underline',
      'purple': 'header',
      'blue': 'blue',
      'cyan': 'cyan',
      'green': 'green',
      'yellow': 'warning',
      'red': 'fail',
   }
   def __new__(cls, string, *args, **kwargs):
      res = string
      for tag, style in sstr.TAGS.items():
         res = re.sub(f'<{tag}\|'+r'(.*)'+f'>', getattr(FormatString(r'\1'), style), res)
      return super(sstr, cls).__new__(cls, res)
   
   def __init__(self, string: str):
      pass