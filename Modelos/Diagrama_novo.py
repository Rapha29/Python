#precisa instalar o Graphviz no computador / https://graphviz.org/download/

from diagrams import Cluster, Diagram
from diagrams.aws.compute import ECS 
from diagrams.aws.database import Elasticache, RDS
from diagrams.aws.network import ELB, Route53

with Diagram("Clustered web Services", show=False):
    dns = Route53("dns")
    lb = ELB("lb")

    with Cluster("Services"):
        svc_group = [ECS("web1"),
                    ECS("web2"),
                    ECS("web3")]

    with Cluster("DB Cluster"):
        db_master = RDS("userdb")
        db_read_only = RDS("userdb ro")

    memcached = Elasticache("memcached")

    dns >> lb >> svc_group
    svc_group >> db_master
    svc_group >> db_read_only
    svc_group >> memcached
