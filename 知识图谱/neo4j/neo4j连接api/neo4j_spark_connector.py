import org.apache.spark.{SparkConf, SparkContext}
import org.neo4j.spark.Neo4j
import org.neo4j.spark.Neo4jDataFrame
import org.apache.spark.sql.{DataFrame, Row, SQLContext, SparkSession}
import org.apache.spark.sql.types.{DataTypes, StructField, StructType}
import org.apache.spark.graphx._
import org.apache.spark.rdd.RDD
import org.apache.spark.sql.SparkSession
object ScalaWordCount {
  def main(args: Array[String]): Unit = {
    val conf = new SparkConf()
      .setMaster("yarn").setAppName("Spark Connect to Neo4j")
      .set("spark.neo4j.bolt.url","bolt://localhost:7687")
      .set("spark.neo4j.bolt.user","neo4j")
      .set("spark.neo4j.bolt.password","neo4j")
    val spark = SparkSession
      .builder()
      .config(conf)
      .enableHiveSupport()
      .getOrCreate()
    val sc = spark.sparkContext
    val neo = Neo4j(sc)
    // 简单的查询并且返回df
    val df = neo.cypher("MATCH (n:Shop) RETURN n.cshop_cd, n.credit_score").loadDataFrame
    df.show()
    // 创建节点及边
    val school_transfer_to_school = sc.makeRDD(Seq(
      Row("Stanford", "MIT", "100","1987"),
      Row("Stanford", "UC LA", "1100","2001"),
      Row("MIT", "UTD","110","1988"),
      Row("UTD", "Stanford","500","1999"),
      Row("UTD", "MIT","1500","2011"),
      Row("UTD", "MIT","2800","2017")
    ))
    val school_transfer_to_school_schema = StructType(Seq(
      StructField("name_send",DataTypes.StringType),
      StructField("name_rec",DataTypes.StringType),
      StructField("amount",DataTypes.StringType),
      StructField("date",DataTypes.StringType)
    ))
    val transfer_df = spark.createDataFrame(school_transfer_to_school,school_transfer_to_school_schema)
    Neo4jDataFrame.mergeEdgeList(sc, transfer_df,
      ("TopUniversity_2", Seq("name_send")),
      ("TRANSFER_TO_REL_2",Seq("amount","date")),
      ("TopUniversity_2", Seq("name_rec"))
    )
  }
}
