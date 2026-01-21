## In Big Query
Need to setup a service account (Big Query Admin, storage admin and compute admin rols ) and then get new json key

### To fix formatting
(base) biancaniemann@Biancas-Air terrademo % terraform fmt
main.tf

### to export the keys file
(base) biancaniemann@Biancas-Air terrademo % export GOOGLE_CREDENTIALS='/workspaces/data_engineering_zoomcamp/pipeline/terraform/keys/my-creds.json'

(base) biancaniemann@Biancas-Air terrademo % echo $GOOGLE_CREDENTIALS
/Users/biancaniemann/Documents/DTC_Zoomcamp/terrademo/keys/my-creds.json

### Initialize
(base) biancaniemann@Biancas-Air terrademo % terraform init
Initializing the backend...
Initializing provider plugins...
- Finding hashicorp/google versions matching "7.16.0"...
- Installing hashicorp/google v7.16.0...
- Installed hashicorp/google v7.16.0 (signed by HashiCorp)
Terraform has created a lock file .terraform.lock.hcl to record the provider
selections it made above. Include this file in your version control repository
so that Terraform can guarantee to make the same selections by default when
you run "terraform init" in the future.

Terraform has been successfully initialized!

You may now begin working with Terraform. Try running "terraform plan" to see
any changes that are required for your infrastructure. All Terraform commands
should now work.

If you ever set or change modules or backend configuration for Terraform,
rerun this command to reinitialize your working directory. If you forget, other
commands will detect it and remind you to do so if necessary.
(base) biancaniemann@Biancas-Air terrademo % terraform plan

Terraform used the selected providers to generate the following execution plan.
Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # google_storage_bucket.demo-bucket will be created
  + resource "google_storage_bucket" "demo-bucket" {
      + effective_labels            = {
          + "goog-terraform-provisioned" = "true"
        }
      + force_destroy               = true
      + id                          = (known after apply)
      + location                    = "EU"
      + name                        = "fine-pride-447109-q8-terra-bucket"
      + project                     = (known after apply)
      + project_number              = (known after apply)
      + public_access_prevention    = (known after apply)
      + rpo                         = (known after apply)
      + self_link                   = (known after apply)
      + storage_class               = "STANDARD"
      + terraform_labels            = {
          + "goog-terraform-provisioned" = "true"
        }
      + time_created                = (known after apply)
      + uniform_bucket_level_access = (known after apply)
      + updated                     = (known after apply)
      + url                         = (known after apply)

      + lifecycle_rule {
          + action {
              + type          = "AbortIncompleteMultipartUpload"
                # (1 unchanged attribute hidden)
            }
          + condition {
              + age                    = 1
              + matches_prefix         = []
              + matches_storage_class  = []
              + matches_suffix         = []
              + with_state             = (known after apply)
                # (3 unchanged attributes hidden)
            }
        }

      + soft_delete_policy (known after apply)

      + versioning (known after apply)

      + website (known after apply)
    }

Plan: 1 to add, 0 to change, 0 to destroy.

─────────────────────────────────────────────────────────────────────────────────────

Note: You didn't use the -out option to save this plan, so Terraform can't guarantee
to take exactly these actions if you run "terraform apply" now.

### Apply (Can check in BQ and should now see the bucket)
(base) biancaniemann@Biancas-Air terrademo % terraform apply

Terraform used the selected providers to generate the following execution plan.
Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # google_storage_bucket.demo-bucket will be created
  + resource "google_storage_bucket" "demo-bucket" {
      + effective_labels            = {
          + "goog-terraform-provisioned" = "true"
        }
      + force_destroy               = true
      + id                          = (known after apply)
      + location                    = "EU"
      + name                        = "fine-pride-447109-q8-terra-bucket"
      + project                     = (known after apply)
      + project_number              = (known after apply)
      + public_access_prevention    = (known after apply)
      + rpo                         = (known after apply)
      + self_link                   = (known after apply)
      + storage_class               = "STANDARD"
      + terraform_labels            = {
          + "goog-terraform-provisioned" = "true"
        }
      + time_created                = (known after apply)
      + uniform_bucket_level_access = (known after apply)
      + updated                     = (known after apply)
      + url                         = (known after apply)

      + lifecycle_rule {
          + action {
              + type          = "AbortIncompleteMultipartUpload"
                # (1 unchanged attribute hidden)
            }
          + condition {
              + age                    = 1
              + matches_prefix         = []
              + matches_storage_class  = []
              + matches_suffix         = []
              + with_state             = (known after apply)
                # (3 unchanged attributes hidden)
            }
        }

      + soft_delete_policy (known after apply)

      + versioning (known after apply)

      + website (known after apply)
    }

Plan: 1 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

google_storage_bucket.demo-bucket: Creating...
google_storage_bucket.demo-bucket: Creation complete after 3s [id=terraform-demo-bucket-484515]

Apply complete! Resources: 1 added, 0 changed, 0 destroyed.

### Destroy (Check in BQ and bucket will be gone)
(base) biancaniemann@Biancas-Air terrademo % terraform destroy
google_storage_bucket.demo-bucket: Refreshing state... [id=terraform-demo-bucket-484515]

Terraform used the selected providers to generate the following execution plan.
Resource actions are indicated with the following symbols:
  - destroy

Terraform will perform the following actions:

  # google_storage_bucket.demo-bucket will be destroyed
  - resource "google_storage_bucket" "demo-bucket" {
      - default_event_based_hold    = false -> null
      - effective_labels            = {
          - "goog-terraform-provisioned" = "true"
        } -> null
      - enable_object_retention     = false -> null
      - force_destroy               = true -> null
      - id                          = "terraform-demo-bucket-484515" -> null
      - labels                      = {} -> null
      - location                    = "EU" -> null
      - name                        = "terraform-demo-bucket-484515" -> null
      - project                     = "terraform-demo-484515" -> null
      - project_number              = 19398471153 -> null
      - public_access_prevention    = "inherited" -> null
      - requester_pays              = false -> null
      - rpo                         = "DEFAULT" -> null
      - self_link                   = "https://www.googleapis.com/storage/v1/b/terraform-demo-bucket-484515" -> null
      - storage_class               = "STANDARD" -> null
      - terraform_labels            = {
          - "goog-terraform-provisioned" = "true"
        } -> null
      - time_created                = "2026-01-16T15:18:54.180Z" -> null
      - uniform_bucket_level_access = false -> null
      - updated                     = "2026-01-16T15:18:54.180Z" -> null
      - url                         = "gs://terraform-demo-bucket-484515" -> null

      - hierarchical_namespace {
          - enabled = false -> null
        }

      - lifecycle_rule {
          - action {
              - type          = "AbortIncompleteMultipartUpload" -> null
                # (1 unchanged attribute hidden)
            }
          - condition {
              - age                                     = 1 -> null
              - days_since_custom_time                  = 0 -> null
              - days_since_noncurrent_time              = 0 -> null
              - matches_prefix                          = [] -> null
              - matches_storage_class                   = [] -> null
              - matches_suffix                          = [] -> null
              - num_newer_versions                      = 0 -> null
              - send_age_if_zero                        = false -> null
              - send_days_since_custom_time_if_zero     = false -> null
              - send_days_since_noncurrent_time_if_zero = false -> null
              - send_num_newer_versions_if_zero         = false -> null
              - with_state                              = "ANY" -> null
                # (3 unchanged attributes hidden)
            }
        }

      - soft_delete_policy {
          - effective_time             = "2026-01-16T15:18:54.180Z" -> null
          - retention_duration_seconds = 604800 -> null
        }
    }

Plan: 0 to add, 0 to change, 1 to destroy.

Do you really want to destroy all resources?
  Terraform will destroy all your managed infrastructure, as shown above.
  There is no undo. Only 'yes' will be accepted to confirm.

  Enter a value: yes

google_storage_bucket.demo-bucket: Destroying... [id=terraform-demo-bucket-484515]
google_storage_bucket.demo-bucket: Destruction complete after 2s

Destroy complete! Resources: 1 destroyed.
(base) biancaniemann@Biancas-Air terrademo % 

### To use variables and create a dataset in BQ
create a variables.tf file and in there create variables for all the points you want to use in the main.tf 

To remove the credentials
(base) biancaniemann@Biancas-Air terrademo % unset GOOGLE_CREDENTIALS 
(base) biancaniemann@Biancas-Air terrademo % echo $GOOGLE_CREDENTIALS 

---
### Setting up Terrform in codespaces (not permanent)
sudo apt update
sudo apt install -y gnupg software-properties-common

wget -O- https://apt.releases.hashicorp.com/gpg | \
  gpg --dearmor | \
  sudo tee /usr/share/keyrings/hashicorp-archive-keyring.gpg

echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] \
https://apt.releases.hashicorp.com $(lsb_release -cs) main" | \
sudo tee /etc/apt/sources.list.d/hashicorp.list

sudo apt update
sudo apt install -y terraform

terraform version

⚠️ Note: This won’t persist if the Codespace is deleted — devcontainer will.