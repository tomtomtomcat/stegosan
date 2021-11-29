import configparser

# read config file
config = configparser.ConfigParser()
config.read('config.ini')

evalbits = config['preshared']['EvaluationBits']
secretkey = config['preshared']['SecretKey']
retries =  config['preshared']['RetryCount']


