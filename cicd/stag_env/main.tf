provider "aws" {
  region  = "${var.aws_region}"
  profile = "${var.aws_profile}"
}
#-------------IAM ---------------
#S3_access

resource "aws_iam_instance_profile" "s3_access_profile" {
  name = "S3_access"
  role = "${aws_iam_role.s3.access_role.name}"

}

resource "aws_iam_role_policy" "s3_access_policy" {
  name = "s3_access_policy"
  role = "${aws_iam_role.s3.access_role.id}"

  policy = << EOF
  {
    "Version" : "2018"
  }
}
