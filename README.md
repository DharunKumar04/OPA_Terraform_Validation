# OPA Terraform Validation using GitHub Action

### Project Description

This project provides a GitHub Action workflow to validate Terraform plans against Open Policy Agent (OPA) policies. Users can manually trigger the workflow, specify the project folder and resource type, and perform validation to ensure compliance with defined policies. The workflow includes steps for Terraform initialization, plan generation, resource filtering, and OPA policy evaluation, integrating seamlessly with AWS credentials stored as GitHub secrets.

---

### Features of the project

- **Manual Trigger**            : Initiate the workflow manually by specifying the project folder and resource type, providing flexibility in validation timing.
- **Terraform Plan Validation** : Automatically validate Terraform plans using OPA policies to ensure compliance with infrastructure standards and governance.
- **Resource Filtering**        : Efficiently filter and isolate specific resource types from the Terraform plan for targeted policy evaluation.
- **OPA Policy Evaluation**     : Conduct thorough evaluations of filtered resources against OPA policies, generating detailed compliance reports.

---

### Prerequisites to use this project

1.  A GitHub repository with Terraform configurations.
2.  OPA policies defined and stored in the `rego_policies` directory within the repository.
3.  AWS credentials stored as GitHub secrets `AWS_ACCESS_KEY` and `AWS_SECRET_KEY`.

---

### About `terraform_resource_filter.py`

-   The Python script is designed to filter specific resource types from a Terraform plan JSON file and save each filtered resource as an individual JSON file. 
-   It automates the extraction and individual saving of specific Terraform resources, facilitating further processing or validation, such as policy compliance checks using tools like Open Policy Agent (OPA). 
-   By isolating resources, users can focus on specific parts of their infrastructure code, enabling more granular and efficient validation workflows

#### Features of the script

-   **Filter Resources:** Extracts resources of a specified type from a Terraform plan JSON file.
-   **JSON File Generation:** Saves each filtered resource as a separate JSON file in a designated directory.
-   **Error Handling:** Includes robust error handling for file not found and JSON parsing issues.

#### Functions of the script

-   **Extract planned values:** Retrieves the `planned_values` key from the JSON.
-   **Extract root module:** Retrieves the root_module key from `planned_values`.
-   **Extract resources:** Retrieves the resources list from the `root_module`.
-   **Filter resources:** Iterates over the resources and appends those matching the specified `resource_type` to `filtered_resources`.

---

### Usage

#### Trigger the Workflow

1.  Go to the `Actions` tab of your GitHub repository.
2.  Select the `OPA Validation` workflow.
3.  Click on `Run workflow`.
4.  Provide the required inputs:
    -   **Project**: The project folder containing Terraform configurations.
    -   **Resource**: The resource type to validate.

#### Monitor the Workflow

1.  Once the workflow is triggered, you can monitor its progress in the Actions tab.
2.  The workflow will perform the following steps:
    -   Check out the code.
    -   Validate the existence of the project directory and Rego policy file.
    -   Install Terraform, AWS CLI, and OPA.
    -   Initialize Terraform, create a plan, and convert it to JSON.
    -   Run the Python script to filter resources.
    -   Evaluate filtered resources using OPA and save the results.

---

### Results

After the workflow completes, results will be saved in the specified project directory under a `result` folder. Each evaluated resource will have a corresponding JSON file with the evaluation output and can be viewed as a result in the workflow page.

#### How It Helps and Reduces Time

1.  **Automated Workflow**: By automating the validation process, the workflow eliminates the need for manual intervention. This saves time and ensures consistent application of policies.
2.  **Focused Validation**: The use of the terraform_resource_filter.py script ensures that only relevant resources are evaluated. This reduces the amount of data to be processed and speeds up the validation process.
3.  **Continuous Integration**: Integrating OPA policy evaluation into the CI/CD pipeline means that policy compliance is checked early and often. This reduces the risk of non-compliant configurations being deployed.

#### Useful Scenarios

1.  **Infrastructure as Code (IaC) Compliance**: When managing infrastructure through code, it's crucial to ensure that configurations comply with organizational policies. This workflow automates the compliance checks, making it easier to maintain governance.
2.  **Continuous Integration**: Integrating OPA policy evaluation into the CI/CD pipeline means that policy compliance is checked early and often. This reduces the risk of non-compliant configurations being deployed.
3.  **Consistent Compliance**: Ensures that all Terraform plans adhere to the defined OPA policies, maintaining compliance across the entire infrastructure.
---

### Conclusion

This project automates the validation of Terraform plans against OPA policies using GitHub Actions, ensuring that your infrastructure as code adheres to defined compliance and governance rules.
By integrating this workflow into your development process, you can ensure that your Terraform configurations are consistently evaluated against your policies, saving time and reducing the risk of deploying non-compliant infrastructure.

---