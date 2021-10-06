from flask import Flask, json
from flask import request,send_file,send_from_directory,abort
import os

api = Flask(__name__)

@api.route('/faucet', methods=['GET'])
def get_faucet():
  address = request.args.get('address')
  commandline = 'bitcoin-cli -named sendtoaddress address="' + address + '" amount=1 fee_rate=1'
  os.system(commandline)
  return "Success"

@api.route('/graph', methods=['GET'])
def get_graph():
  try:
    return send_from_directory("/root/graph", filename="graph.json", as_attachment=False)
  except FileNotFoundError:
    abort(404)

if __name__ == '__main__':
    api.run() 
