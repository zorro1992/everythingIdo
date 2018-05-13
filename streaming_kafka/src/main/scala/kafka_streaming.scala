import org.apache.spark.SparkConf
import org.apache.spark.streaming.{Seconds, StreamingContext}
import org.apache.spark.streaming.kafka.KafkaUtils

/**
  * Created by raghunandanask on 5/13/18.
  */


object kafka_streaming {

    def main(args: Array[String]) {
      val sparkConf = new SparkConf().setAppName("KafkaWordCount").setMaster("local[*]")
      val ssc = new StreamingContext(sparkConf, Seconds(2))

      val lines = KafkaUtils.createStream(ssc, "localhost:2181", "test",Map("test" -> 5))
      ssc.start()
      ssc.awaitTermination()
    }
  }
