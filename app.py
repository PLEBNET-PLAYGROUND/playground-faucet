from flask import Flask, json
from flask import request
import os

api = Flask(__name__)

@api.route('/faucet', methods=['GET'])
def get_faucet():
  address = request.args.get('address')
  commandline = 'bitcoin-cli -named sendtoaddress address="' + address + '" amount=1 fee_rate=1'
  return os.system(os)

if __name__ == '__main__':
    api.run() 
