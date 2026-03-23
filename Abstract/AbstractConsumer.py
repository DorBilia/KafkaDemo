from abc import abstractmethod

from confluent_kafka import Consumer


class AbstractConsumer:
    def __init__(self, config, topic):
        self.consumer = Consumer(config)
        self.consumer.subscribe([topic])
        print(f"Consumer is connected to {topic} topic")

    def listen(self):
        try:
            while True:
                msg = self.consumer.poll(1.0)
                if msg is None:
                    continue
                elif msg.error():
                    print(f"error: {msg.error()}")
                else:
                    self.handle_event(msg)
        except KeyboardInterrupt:
            print("Shutting down")
        finally:
            self.consumer.close()

    @abstractmethod
    def handle_event(self, msg):
        pass
