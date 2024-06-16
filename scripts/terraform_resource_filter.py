import json
import sys
import os

def filter_resources_by_type(plan_json, resource_type):
    filtered_resources = []

    planned_values = plan_json.get('planned_values', {})
    root_module = planned_values.get('root_module', {})
    resources = root_module.get('resources', [])

    for resource in resources:
        if resource.get('type') == resource_type:
            filtered_resources.append(resource)

    return filtered_resources

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 terraform_resource_filter.py <path_to_plan.json> <resource_type>")
        sys.exit(1)

    json_file = sys.argv[1]
    input_resource_type = sys.argv[2]

    try:
        with open(json_file, 'r') as f:
            plan_data = json.load(f)
    except FileNotFoundError:
        print(f"Error: File '{json_file}' not found.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: Unable to parse JSON from file '{json_file}'.")
        sys.exit(1)

    filtered_resources = filter_resources_by_type(plan_data, input_resource_type)

    if filtered_resources:
        temp_dir = os.path.join(os.path.dirname(json_file), 'temp')
        os.makedirs(temp_dir, exist_ok=True) 

        for resource in filtered_resources:
            resource_name = resource.get('name', 'unnamed_resource')
            filtered_file = os.path.join(temp_dir, f"{resource_name}.json")
            with open(filtered_file, 'w') as f:
                json.dump(resource, f, indent=2)

        print(f"Filtered resources of type '{input_resource_type}' saved as '{resource_name}.json' in the '{temp_dir}' directory.")
    else:
        print(f"No resources of type '{input_resource_type}' found.")
