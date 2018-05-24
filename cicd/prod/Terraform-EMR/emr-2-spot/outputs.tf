output "id" {
  value = "${aws_emr_cluster.emr-test-cluster.id}"
}

output "name" {
  value = "${aws_emr_cluster.emr-test-cluster.name}"
}

output "master_public_dns" {
  value = "${aws_emr_cluster.emr-test-cluster.master_public_dns}"
}
