variable "credentials" {
  description = "My Credentials"
  default     = "./keys/my-creds.json"
}

variable "project" {
  description = "Project"
  default     = "terraform-demo-484515"
}

variable "location" {
  description = "My GCP Location"
  default     = "EU"
}

variable "bq_dataset_name" {
  description = "My Big Query Dataset Name"
  default     = "demo_dataset"
}

variable "gsc_storage_class" {
  description = "My GSC Storage Class"
  default     = "STANDARD"
}

variable "gsc_bucket_name" {
  description = "My GSC Bucket Name"
  default     = "terraform-demo-bucket-484515"
}

variable "region" {
  description = "My GCP Region"
  default     = "europe-west3"
}