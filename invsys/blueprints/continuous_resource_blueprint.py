from flask import Blueprint, jsonify, request

database = []

# POST /{resource_type} - to create an instance of the resource
# GET /{resource_type} - to get all instances of a given resource type
# GET /{resource_type}/<resource_id> - get a specific instance
# DELETE /{resource_type}/<resource_id> - delete a specific instance of a resource
# POST /{resource_type}/<resource_id>/allocations - create an allocation for this resource instance
# GET /{resource_type}/<resource_id>/allocations - get all allocations for this resource instance
# GET /{resource_type}/<resource_id>/allocations/<allocation_id> - get a specific allocation
# DELETE /{resource_type}/<resource_id>/allocations/<allocation_id> - delete the allocation

def create_continuous_resource_blueprint(blueprint_name: str, resource_type: str, resource_prefix: str) -> Blueprint:
    """
    blueprint_name: name of the blueprint, used by Flask for routing
    resource_type: name of the specific type of interval resource, such as Car or Lorry
    resource_prefix: the plural resource to be used in the api endpoint, such as cars, resulting in "/cars"
    """
    blueprint = Blueprint(blueprint_name, __name__)

    @blueprint.route(f'/{resource_prefix}', methods=["POST"])
    def create_resource():
        #database.append()
        database.append({"type":request.get_json()["type"],"price":request.get_json()["price"]})
        return jsonify({}), 201
    
    @blueprint.route(f'/{resource_prefix}', methods=["GET"])
    def get_resources():
        #return jsonify({}), 201
        return jsonify(database), 201
    
    @blueprint.route(f'/{resource_prefix}', methods=["GET"])
    def get_resource():
        return jsonify({}), 201
        
    @blueprint.route(f'/{resource_prefix}',methods=["DELETE"])
    def delete_resources():
        return jsonify({}), 201

    @blueprint.route(f'/{resource_prefix}',methods=["POST"])
    def create_allocation():
        return jsonify({}), 201

    @blueprint.route(f'/{resource_prefix}',methods=["GET"])
    def get_allocations():
        return jsonify({}), 201

    @blueprint.route(f'/{resource_prefix}',methods=["GET"])
    def get_allocations():
        return jsonify({}), 201

    @blueprint.route(f'/{resource_prefix}',methods=["DELETE"])
    def delete_allocation():
        return jsonify({}), 201

    return blueprint