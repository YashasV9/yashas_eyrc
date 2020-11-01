import time
import paho.mqtt.client as paho
import paho.mqtt.subscribe as subscribe
broker="broker.hivemq.com"    
client= paho.Client("client-001") 
print("connecting to broker ",broker)
client.connect(broker)
client.loop_start()
gulbul_var = ""
while gulbul_var!='start':
    msg = subscribe.simple("yashasbigboi/1", hostname=broker)
    gulbul_var = str(msg.payload.decode("utf-8"))
    print(gulbul_var)