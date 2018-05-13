name := "streaming_kafka"

version := "1.0"


scalaVersion := "2.11.11"
val sparkVersion = "1.5.2"

libraryDependencies ++= Seq(
  "org.apache.spark" %% "spark-core" % sparkVersion,
  "org.apache.spark" %% "spark-sql" % sparkVersion,
  "org.apache.spark" %% "spark-streaming" % sparkVersion
)
libraryDependencies += "org.apache.spark" % "spark-streaming-kafka_2.11" % "1.6.3"
libraryDependencies += "org.apache.spark" % "spark-streaming-kafka-0-10_2.11" % "2.0.0"

