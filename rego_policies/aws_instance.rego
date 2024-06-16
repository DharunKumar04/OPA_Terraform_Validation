package play

import future.keywords.if

resource_name = input.type

policy_violations[violations] {
	violations := {
		"failed": tags_all_Environment_failed,
		"error_description": "The environment should be DEVELOPMENT",
		"resource_name": resource_name,
		"severity": "HIGH",
	}
}

tags_all_Environment_failed if {
	tags_all_Environment := input.values.tags_all.Environment
	tags_all_Environment != "Development"
} else = false

policy_violations[violations] {
	violations := {
		"failed": hibernation_failed,
		"error_description": "The hibernation should be set to NULL",
		"resource_name": resource_name,
		"severity": "HIGH",
	}
}

hibernation_failed if {
	hibernation := input.values.hibernation
	hibernation != null
} else = false
