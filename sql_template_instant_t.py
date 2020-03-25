query = """
SELECT {full_cols} FROM


      (
           SELECT {dim_annonce_cols}
                  from dwhdweb.dimannoncepublicationhisto
                  WHERE (datedebut >=   TIMESTAMP '{date_t}' AND
                        (iddwh_typepublication = {typepublication} AND iddwh_typepublicationcouplage = {sourcecouplage}))
      )
      AS t1


LEFT JOIN


     (
           SELECT *
                      FROM
                         (
                          SELECT
                               {annonce_cols},
                               CAST(from_iso8601_timestamp(CONCAT(CAST(year AS VARCHAR),'-',LPAD(CAST(month AS VARCHAR),2,'0'),'-',LPAD(CAST(day AS VARCHAR),2,'0'))) AS TIMESTAMP) AS datemaj

                               FROM "immobc"."annonce_history"
                         )

                      WHERE datemaj = TIMESTAMP '{date_t}'
    )
    AS t2

ON t1.iddwh_annonce = t2.{idannonce_join_for_annonce}

INNER JOIN


    (
           SELECT *
                      FROM
                          (
                          SELECT  {bien_cols},
                                  CAST(from_iso8601_timestamp(CONCAT(CAST(year AS VARCHAR),'-',LPAD(CAST(month AS VARCHAR),2,'0'),'-',LPAD(CAST(day AS VARCHAR),2,'0'))) AS TIMESTAMP) datemaj

                                  FROM {typebien_table}
                          )
                      WHERE datemaj = TIMESTAMP '{date_t}'
    )
     AS t3

ON t1.iddwh_annonce = t3.{idannonce_join_for_typebien} AND t3.datemaj = t2.datemaj

INNER JOIN

    (
           SELECT *
                      FROM
                          (
                          SELECT {transaction_cols},
                                  CAST(from_iso8601_timestamp(CONCAT(CAST(year AS VARCHAR),'-',LPAD(CAST(month AS VARCHAR),2,'0'),'-',LPAD(CAST(day AS VARCHAR),2,'0'))) AS TIMESTAMP) datemaj

                                  FROM {typetransaction_table}
                          )
                      WHERE datemaj = TIMESTAMP '{date_t}'
    )

AS t4

ON t1.iddwh_annonce = t4.{idannonce_join_for_typetransaction} AND t4.datemaj = t2.datemaj
"""