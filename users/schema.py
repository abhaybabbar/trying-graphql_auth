import graphene
from graphql_auth import mutations
from graphql_auth.schema import UserQuery, MeQuery

class Query(UserQuery, MeQuery, graphene.ObjectType):
    pass


class AuthMutation(graphene.ObjectType):
    register = mutations.Register.Field()
    verify_account = mutations.VerifyAccount.Field()
    resend_activation_email = mutations.ResendActivationEmail.Field()
    
class Mutation(AuthMutation, graphene.ObjectType):
    pass