import os
import yaml

PORTAL_CONFIG = os.path.join(os.path.dirname(__file__), '../configs/configs.yml')
CONFIG = yaml.load(file(PORTAL_CONFIG, 'r'))

class ConfigHelper(object):
      def __init__(self):
          self.halo_key = CONFIG["halo"]["api_key"]
          self.halo_secret = CONFIG["halo"]["api_secret_key"]
          self.key = CONFIG["halo"]["key"]
