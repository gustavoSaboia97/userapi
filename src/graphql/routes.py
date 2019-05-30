from flask import Blueprint

from flask_graphql import GraphQLView
from src.graphql.schemas.schema import schema

graphql_blueprint = Blueprint("graphql_blueprint", __name__)

graphql_blueprint.add_url_rule(
    "/graphql/",
    view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True)
)
