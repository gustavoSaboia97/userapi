from src.graphql.models.model.user import User
from src.repository.UserRepository import UserRepository
from graphene import ObjectType
import graphene


class Query(ObjectType):
    user = graphene.Field(User, user_id=graphene.String(required=True))
    users = graphene.List(User)

    def resolve_user(self, info, user_id: str) -> User:

        user_repo = UserRepository()
        user_info = user_repo.get_user_by_id(user_id)

        return User(
            user_id=user_info.user_id,
            name=user_info.name,
            login=user_info.login,
            access_token=user_info.access_token
        )

    def resolve_users(self, info) -> list:

        user_repo = UserRepository()
        return user_repo.get_users()


schema = graphene.Schema(query=Query)
