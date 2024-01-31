import graphene
from app.schema import Query
from app.mutation import Mutation
# from users.mutation import AuthMutation
# from graphql_auth.schema import UserQuery

class Query(Query):
    pass

class Mutation(Mutation):
    pass 

schema = graphene.Schema(query=Query, mutation=Mutation)