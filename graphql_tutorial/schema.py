import graphene
from app.schema import Query
from app.mutation import Mutation

class Query(Query):
    pass

class Mutation(Mutation):
    pass 

schema = graphene.Schema(query=Query, mutation=Mutation)