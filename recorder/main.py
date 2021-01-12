from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/', methods=['GET'])
def handler():
    timeout = request.args.get('timeout') or '1'
    processId, err = findProcessId(request.args['containerid'])
    if err:
        print(err)
        return ('Container ID doesn\'t exist', 500)
    port = request.args.get('port') or ''
    host = request.args['host']
    
    proc = subprocess.Popen(['timeout',timeout + 's','./record.sh','--processid=' + processId,'--port=' + port, '--host=' + host],stderr=subprocess.PIPE)
    err = proc.communicate()[0]
    if err:
        print(err)
        return ('An error has occurred while running the script ./record.sh', 500)

    return ('Tcpdump succeed for process id: ' + processId ,200)

def findProcessId(containerid):
    proc = subprocess.Popen(['podman','inspect','-f','{{.State.Pid}}', containerid], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    processId, err = proc.communicate()
    
    if err:
        return None,err
    return str(processId.decode("utf-8")), None
