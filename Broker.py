from kafka import KafkaProducer
import json
from Data import get_registration
import time
def json_serializer(Data):
    return json.dumps(Data).encode("utf-8")


producer = KafkaProducer(bootstrap_servers=['192.168.0.186:9092'],
                         value_serializer=json_serializer)

if __name__ == "__main__":
    while 1 ==1:
        Register_User = get_registration()
        print(Register_User)
        producer.send('Test',Register_User)
        time.sleep(4)
