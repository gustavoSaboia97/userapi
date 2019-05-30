from graphene import ObjectType
import graphene


class User(ObjectType):
    user_id = graphene.String()
    name = graphene.String()
    login = graphene.String()
    access_token = graphene.String()
