from flask import Flask
from blueprints.continuous_resource_blueprint import create_continuous_resource_blueprint



def create_app() -> Flask:
    app = Flask(__name__)

    # Register continuous resource blueprints
    app.register_blueprint(
        create_continuous_resource_blueprint(
            blueprint_name="CarsBlueprint", # The name, used by flask when using the url_for function
            resource_type="Car", # The resource type
            resource_prefix="cars" # The base of the url for this resource type
        ),
        url_prefix='/api'
    )

    app.register_blueprint(
        create_continuous_resource_blueprint(
            blueprint_name="LorriesBlueprint", # The name, used by flask when using the url_for function
            resource_type="Lorries", # The resource type
            resource_prefix="lorries" # The base of the url for this resource type
        ),
        url_prefix='/api'
    )

    app.register_blueprint(
        create_continuous_resource_blueprint(
            blueprint_name="TrucksBlueprint", # The name, used by flask when using the url_for function
            resource_type="Trucks", # The resource type
            resource_prefix="trucks" # The base of the url for this resource type
        ),
        url_prefix='/api'
    )



    return app

if __name__=="__main__":
    app = create_app()
    app.run(host="127.0.0.1", port=5000, debug=True)