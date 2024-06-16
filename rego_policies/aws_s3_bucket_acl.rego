package play

import future.keywords.if

resource_name = input.type

    policy_violations[violations] {
        violations := {
            "failed": acl_failed,
            "error_description": "The ACL of the Bucket should be PRIVATE",
            "resource_name": resource_name,
            "severity": "HIGH",
        }
    }

    acl_failed if {
        acl := input.values.acl
    acl != "private"
} else = false
