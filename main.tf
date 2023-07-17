resource "google_storage_bucket" "GCS1"{
  name = "bucket_from_terraform_pranav_reddy"
  location = "us-central1"
  storage_class = "STANDARD"
  labels = {
    "key1" = "value1"
    "key2" = "value2"
    "key3" = "value3"
  }
  uniform_bucket_level_access = true
}

resource "google_storage_bucket_object" "photo" {
  name = "random_name"
  bucket = google_storage_bucket.GCS1.name
  source = "photo.png"
}