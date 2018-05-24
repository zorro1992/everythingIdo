provider "aws" {
  version = ">= 1.2.0"
}

resource "aws_emr_cluster" "emr-test-cluster" {
  name          = "Big-Data-Cluster-IAC-Terraform"
  release_label = "emr-5.5.0"
  applications  = ["Spark","Hive","Hadoop","Spark","Zeppelin","Hue","Tez","ZooKeeper","Sqoop"]
  termination_protection = false
  keep_job_flow_alive_when_no_steps = true


  ec2_attributes {
    subnet_id                         = "subnet-7b51f233"
    emr_managed_master_security_group = "sg-25455741"
    emr_managed_slave_security_group  = "sg-26455742"
    service_access_security_group     = "sg-27455743"
    instance_profile                  = "EMR_EC2_DefaultRole"
    key_name                          = "BigMama"
  }

  instance_group {
    instance_count = 1
    instance_role  = "MASTER"
    instance_type  = "r3.xlarge"
  }

  instance_group {
    instance_count = 1
    instance_role  = "CORE"
    instance_type  = "r3.xlarge"
    bid_price      = "0.371"
  }


    tags {
      environment = "prod"
      criticality = "low"
      managedbyterraform = "yes"
    }
  service_role = "EMR_DefaultRole"
  configurations = "https://s3-eu-west-1.amazonaws.com/careem-analytics/ETLs/hivemetadata/emr_configurations.json"
}
