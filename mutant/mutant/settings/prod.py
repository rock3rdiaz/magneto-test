from mutant.settings.base import *

env = environ.Env(DEBUG=(bool, False))
# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, '../../.env'))