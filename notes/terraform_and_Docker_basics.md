# Terraform vs Docker — Learning Notes & Examples

## 📌 Purpose of This Repository

This repository is for **learning and documenting the difference between Terraform and Docker**, and how they are commonly used **together** in modern software and data platforms.

The goal is to understand:
- What each tool does
- Where their responsibilities differ
- How they fit into a typical cloud setup

This is **not** a production-ready project — it’s a learning reference.

---

## 🧱 What Is Terraform?

**Terraform** is a tool used to **create and manage infrastructure** (mostly in the cloud) using configuration files instead of manual setup.

In simple terms:
- You *describe* what infrastructure you want
- Terraform *builds and maintains* it for you

### Terraform is used to create things like:
- Virtual machines / servers
- Networks and firewalls
- Databases
- Cloud storage
- Permissions and access rules

Terraform works with many cloud providers such as:
- AWS
- Azure
- Google Cloud

### Key idea:
**Infrastructure as Code** — your cloud setup is defined in files that can be version-controlled.

---

## 📦 What Is Docker?

**Docker** is a tool used to **package and run applications** in a consistent way.

Docker bundles:
- Your application
- Its libraries
- Its dependencies
- Its runtime environment

Into a single unit called a **container**.

This ensures:
- The app runs the same on every machine
- Fewer “works on my computer” problems

### Docker is used to:
- Build containers from a `Dockerfile`
- Run applications inside containers
- Start, stop, and manage app processes

---

## 🔍 Terraform vs Docker — Key Differences

| Aspect | Terraform | Docker |
|------|---------|--------|
| Purpose | Infrastructure provisioning | Application packaging |
| Scope | Cloud resources | App + dependencies |
| Creates servers | ✅ Yes | ❌ No |
| Runs applications | ❌ No | ✅ Yes |
| Manages cloud services | ✅ Yes | ❌ No |
| Ensures app consistency | ❌ No | ✅ Yes |

### In short:
- Terraform answers **“What infrastructure should exist?”**
- Docker answers **“What runs on that infrastructure?”**

---

## 🤝 Are Terraform and Docker Used Together?

**Yes — very often.**

A common real-world flow looks like this:

1. **Terraform**
   - Creates servers
   - Sets up networks and security
   - Provisions databases or clusters

2. **Docker**
   - Packages the application
   - Runs the app on those servers

Terraform **prepares the environment**  
Docker **runs the software inside it**

---

## 🧠 Analogy (Layman-Friendly)

Think of building and running a restaurant:

- **Terraform**  
  Builds the restaurant:
  - The building
  - Electricity
  - Plumbing
  - Kitchen layout

- **Docker**  
  Prepares and runs the meals:
  - Ingredients
  - Recipes
  - Cooking process

You need **both**, but they do very different jobs.

---

## 🌍 Where Kubernetes Fits (High Level)

In larger systems:
- Terraform may create a **Kubernetes cluster**
- Kubernetes manages **Docker containers**
- Docker runs the applications

Terraform → Kubernetes → Docker

---

## 🎯 Why This Matters (Data & Analytics Context)

Understanding the separation of responsibilities helps with:
- Cloud-based data platforms
- Analytics engineering workflows
- Scalable ETL / ELT pipelines
- Collaboration between data, engineering, and DevOps teams

This knowledge is commonly expected in:
- Data engineering roles
- Analytics engineering roles
- Platform or DevOps-adjacent positions

---

## 🚀 Possible Next Learning Steps

Future additions to this repository could include:
- Basic Terraform configuration examples
- Simple Dockerfile examples
- Folder structure examples
- Diagrams of cloud architectures
- Notes on Kubernetes basics
- Example use cases for data or analytics projects

---

## 📚 Disclaimer

This repository is for **educational purposes** and reflects a learning journey, not production-level expertise.
---
## 🛠️ Key Terraform Commands (Beginner-Friendly)

This section lists commonly used Terraform commands and explains what they do in simple terms.
---
### terraform init

- Initializes a Terraform project.

- What it does:

  - Downloads required provider plugins (for example AWS, Azure, or GCP)

  - Sets up the working directory

  - Prepares Terraform to run commands

Run this first in any new or cloned Terraform project.

##### Example command: terraform init

### terraform validate

- Checks whether the Terraform configuration files are syntactically valid.

- What it does:

  - Verifies correct syntax

  - Checks for basic configuration errors

  - Does not contact the cloud provider

  - Useful for catching mistakes early.

##### Example command: terraform validate

### terraform fmt

- Formats Terraform files into a standard, readable style.

- What it does:

  - Aligns spacing and indentation

  - Improves readability

  - Keeps code consistent across projects

  - Often used before committing changes to Git.

##### Example command: terraform fmt

### terraform plan

- Shows what Terraform will do before making any changes.

- What it does:

  - Compares desired state (your code) with current state

  - Shows which resources will be created, changed, or destroyed

  - Makes no changes to infrastructure

  - This is a safe preview step.

##### Example command:terraform plan

### terraform apply

- Creates or updates infrastructure based on the configuration.

- What it does:

  - Executes the changes shown in terraform plan

  - Creates, modifies, or deletes cloud resources

  - Updates the Terraform state file

  - Usually asks for confirmation before applying changes.

##### Example command:terraform apply

### terraform destroy

- Removes all infrastructure managed by the Terraform project.

- What it does:

  - Deletes cloud resources created by Terraform

  - Cleans up infrastructure

  - Helps avoid unnecessary cloud costs

  - ⚠️ Use with caution.

##### Example command:terraform destroy

### terraform show

- Displays the current Terraform state in a human-readable format.

- What it does:

  - Shows what infrastructure Terraform is currently managing

  - Reads information from the Terraform state file

  - Helpful for inspection and debugging.

##### Example command:terraform show

### terraform output

- Displays values defined in outputs.tf.

- What it does:

  - Shows useful information such as IP addresses or resource IDs

  - Makes it easy to retrieve values after deployment

##### Example command:terraform output
---
## 🔁 Typical Terraform Workflow
A common beginner-friendly workflow:
- terraform init
- terraform fmt
- terraform validate
- terraform plan
