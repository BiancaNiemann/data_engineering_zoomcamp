variable "credentials" {
  description = "My Credentials"
  default     = "/workspaces/data_engineering_zoomcamp/keys/my-creds.json"
}

variable "project" {
  description = "Project"
  default     = "kestra-sandbox-485712"
}

variable "location" {
  description = "My GCP Location"
  default     = "EU"
}

variable "bq_dataset_name" {
  description = "My Big Query Dataset Name"
  default     = "gcp_dataset"
}

variable "gsc_storage_class" {
  description = "My GSC Storage Class"
  default     = "STANDARD"
}

variable "gsc_bucket_name" {
  description = "My GSC Bucket Name"
  default     = "kestra-bucket-484712"
}

variable "region" {
  description = "My GCP Region"
  default     = "europe-west3"
}