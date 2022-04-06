import logging

# Follow logging best practises for libraries and only import a NullHandler so 
# logging can be configured by the user.
logging.getLogger(__name__).addHandler(logging.NullHandler())

# ##################################### LOGS #####################################
# # Uncomment the below section when developing if logging is required.
# ################################################################################
# # Initialize the logger and specify the level of logging. This will log "DEBUG" 
# # and higher messages to file and log "INFO" and higher messages to the console.
# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s %(levelname)s: %(message)s',
#                     datefmt='%d-%m-%y %H:%M:%S',
#                     filename='debug.log',
#                     filemode='w')

# # Define a "handler" which writes "INFO" messages or higher to the "sys.stderr".
# console = logging.StreamHandler()
# console.setLevel(logging.INFO)

# # Set a format which is simpler for console messages.
# formatter = logging.Formatter('[%(asctime)s]: %(message)s', datefmt='%H:%M:%S')

# # Tell the console "handler" to use this format.
# console.setFormatter(formatter)

# # Add the "handler" to the "root logger".
# logging.getLogger('').addHandler(console)

# ################################################################################

# Version of gen-pygments-css package
__version__ = "0.0.3"