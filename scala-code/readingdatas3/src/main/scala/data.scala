import scala.io.Source

/**
  * Created by raghunandanask on 5/15/18.
  */
object data {
  def main(args: Array[String]): Unit = {

    val v1 = args(0) /* The path of the file is in Run config */
    val v2: Seq[String] = Source.
      fromFile(v1).
      getLines.
      toList
    v2.foreach(println)
  }

}