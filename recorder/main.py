from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/', methods=['GET'])
def handler():
    timeout = request.args.get('timeout') or '1'
    processid = request.args['processid']
    port = request.args.get('port') or ''
    host = request.args['host']

    proc = subprocess.Popen(['timeout',timeout + 's','./record.sh','--processid=' + processid,'--port=' + port, '--host=' + host],stderr=subprocess.PIPE)
    err = proc.communicate()[0]

    if err:
        return ('An error has occurred while running the script ./record.sh', 500)

    return ('Succeded',200)
