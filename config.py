import configparser

# read config file
config = configparser.ConfigParser()
config.read('config.ini')

evalbits = config['preshared'].getint('EvaluationBits')
secretkey = config['preshared']['SecretKey']
retries =  config['preshared'].getint('RetryCount')


