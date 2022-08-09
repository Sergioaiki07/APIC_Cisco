import requests #para trabajar la api
import json #para trabajar con json
import conf #carga de variables de acceso y url

def obtener_token(): #obtener token
    url = conf.URL+"aaaLogin.json" #llamada a la pagina de login
    body = { #Cuerpo del mensaje http donde ira las variables de nombre y paswrd
        "aaaUser": {
            "attributes": { #atributos para pasar as credenciales
                "name": conf.USR,
                "pwd": conf.PASS
            }
        }
    }
    cabecera = { #cabecera del codigo http para explicar que tipo de contenida de pasara
        "Content-Type": "application/json"
    }
    requests.packages.urllib3.disable_warnings()
    respuesta = requests.post(url, headers=cabecera, data=json.dumps(body), verify=False) #envio datos
    token = respuesta.json()['imdata'][0]['aaaLogin']['attributes']['token'] #selcciono el token dentro de los valores devueltos
    print(respuesta.json())

    return token
print(obtener_token())
def Estado_leaf(leaf): #consulta por los dos leaf que estan en el laboratorio
    try:
        TOKEN = obtener_token()
        url = conf.URL + "node/mo/topology/pod-1/node-"+leaf+"/sys.json?query-target=subtree&target-subtree-class=l1PhysIf,l1FcPhysIf&rsp-subtree-include=health,faults" #url de consulta con la variable que indica al leaf seleccionado
        cab = {"content-Type": "application/json"} #cabecera del codigo http para explicar que tipo de contenida de pasara
        cookies = {"APIC-Cookie": TOKEN} #Cookies que pasan por http para validar el token con la api
        requests.packages.urllib3.disable_warnings()
        respuesta = requests.get(url, headers=cab, cookies=cookies, verify=False)
        return respuesta
    except:
        return "Hubo un problema, por favor verifica la conexión y/o los datos ingresados"
#prueba del puerto 1/49 que esta up
def adm_puerto(puerto,estado,nodo): #funcion donde tiene las variables del puerto , si quiere encender o apagar la interfaz y si el nodo a modificar
    try:
        TOKEN = obtener_token()
        if(nodo == '1'):
            nodo='101'
        elif(nodo == '2'):
            nodo = '102'
        cookies = {"APIC-Cookie": TOKEN}
        url = conf.URL+"node/mo/uni/fabric/outofsvc.json"
        if(estado == "2"): #url si se quiere apagar la interfaz
            body = {
                "fabricRsOosPath": {
                    "attributes": {
                        "tDn": "topology/pod-1/paths-"+nodo+"/pathep-[eth"+puerto+"]",
                        "lc": "blacklist"
                    },
                    "children": []
                }
            }
        elif(estado == "1"):#url si se quiere encernder la interfaz
            body = {
                "fabricRsOosPath": {
                    "attributes": {
                        "dn": "uni/fabric/outofsvc/rsoosPath-[topology/pod-1/paths-"+nodo+"/pathep-[eth"+puerto+"]]",
                        "status": "deleted"
                    },
                    "children": []
                }
            }
        cabecera = {
            "Content-Type": "application/json"
        }
        requests.packages.urllib3.disable_warnings()
        respuesta = requests.post(url, headers=cabecera, cookies=cookies, data=json.dumps(body), verify=False)
         #respuesta si fue o no ejecutada
        return respuesta
    except:#para controlar algun error devolviendo un estring
        return "Hubo un problema, por favor verifica la conexión y/o los datos ingresados"
