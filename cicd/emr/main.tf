provider "aws" {
  version = "~> 1.19"
  region  = "${var.aws_region}"
  profile = "${var.aws_profile}"
}


resource "aws_emr_cluster" "emr-test-cluster" {
  name          = "emr-test-arn"
  release_label = "emr-4.6.0"
  applications  = ["Spark"]

  termination_protection = false
  keep_job_flow_alive_when_no_steps = true

  ec2_attributes {
    subnet_id                         = "subnet8"
    emr_managed_master_security_group = "sgce230"
    emr_managed_slave_security_group  = "sg-5a712"
    instance_profile                  = "EMR_EC2_DefaultRole"
  }

    master_instance_type = "m4.large"
    core_instance_type   = "m4.large"
    core_instance_count  = 2

  service_role = "EMR_DefaultRole"
}
