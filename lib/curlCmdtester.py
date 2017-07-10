import json
import subprocess
from robot.api import logger

Username = None
Password = None
Protocol = "http"
Port = "8080"
headers = """\"Content-Type : application/json\"  --header \"Accept : application/json\""""


def curlCmdTester(Host,objURL,requestMethod,payload,ExpectedResponse):

    username = Username 
    password = Password
    url = "%s://%s:%s/%s" %(Protocol,Host,Port,objURL) 
    if username is not None:
        cmd = "curl -H "+ headers + " --user " + username +" : " + password+" -X " +requestMethod+   " -d " + "\'" + payload +"\'" +" "+ url
    else:
        cmd = "curl -H "+ headers + " -X " +requestMethod+  " -d " + "\'" + payload +"\'" +" "+ url
        logger.info("CURL COMMAND:")
        logger.info("%s"%cmd) 
        response = exec_cmd(cmd,payload)
        logger.info("%s OBJECT DETAILS:"%requestMethod)
        logger.info("%s"%response)
        logger.info("RESULT:%s"%response["Result"])
        logger.info("EXPECTED RESPONSE:%s"%ExpectedResponse)
        if response["Result"] == ExpectedResponse or response["Result"] == '':
            logger.info("CHECKING IF THE CONFIGURATION WAS APPLIED")
            result = validate(cmd,payload)
            if result:
                logger.info("Configuration was applied")
                return True
            else:
                logger.info("Configuration was not applied")
                return False
        else:
            return False
            


def exec_cmd(cmd,ignore_exception=False):
 
    """ execute command and return stdout output - None on error """
    try:
        false = False
        true = True
        logger.info("EXCECUTING COMMAND: %s" % cmd)
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        response = process.communicate()
        response = eval(response[0])
        return response 
    except subprocess.CalledProcessError as e:
        # exit code -2 seen on ctrl+c interrupt
        if e.returncode < 0: sys.exit("\nExiting...\n")
        if ignore_exception: 
            logger.debug("error executing cmd: %s" % e)
            logger.debug("stderr: %s" % e.output)
            return None
        logger.warn("error executing cmd: %s" % cmd)
        logger.warn("%s" % e.output)
        raise e

def validate(cmd,payload):
    false = False
    true = True
    cmd = cmd.replace("POST","GET",1)
    cmd = cmd.replace("PATCH","GET",1)
    logger.info("CURL COMMAND:")
    logger.info("%s"%cmd) 
    res = exec_cmd(cmd)
    logger.info("GET OBJECT DETAILS:")
    logger.info("%s"%res)
    payload = eval(payload)
    try:
        for param in payload.keys():
            if payload[param] == res["Object"][param]:
                result = True
            else:
                result = False
    except:
        result = False
            
    return result
