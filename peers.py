from charms.reactive import Endpoint


class KafkaPeers(Endpoint):

    def kafka_broker_count(self):
        """
        Counts number of kafka brokers by counting 
        peer relations.

        broker_count = #peers_relations + 1
        """
        return len(self.relations[0].units) + 1 