import graphene
from users.schema import Query as UserQuery

class Query(UserQuery):
    pass

schema = graphene.Schema(query=Query)