from abc import abstractmethod

from confluent_kafka import Producer


class AbstractProducer:
    def __init__(self, config):
        self.producer = Producer(config)

    @abstractmethod
    def publish(self, topic, message):
        pass

