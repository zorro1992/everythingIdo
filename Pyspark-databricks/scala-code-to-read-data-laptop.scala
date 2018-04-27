/* The scala code will read any input file in the laptop */

import scala.io.Source
object read_file {
    def main(args: Array[String]) {
      val filename = "/Users/raghunandanask/Downloads/mockdata/MOCK_DATA.csv"
      for (line <- Source.fromFile(filename).getLines) {
          println(line)
      }
      /* val src = io.Source.fromFile("/Users/raghunandanask/Downloads/mockdata/MOCK_DATA.csv") */
  }
}
