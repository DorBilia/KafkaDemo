from abc import abstractmethod

from confluent_kafka import Consumer


class AbstractConsumer():
    def __init__(self, config, topic):
        self.consumer = Consumer(config)
        self.consumer.subscribe([topic])
        print(f"Consumer is connected to {topic} topic")

    @abstractmethod
    def listen(self):
        pass
