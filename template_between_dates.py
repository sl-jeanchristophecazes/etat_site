query = """
SELECT {full_cols} FROM


      (
           SELECT {dim_annonce_cols}
                  from dwhdweb.dimannoncepublicationhisto
                  WHERE (datedebut BETWEEN TIMESTAMP '{date_debut}' AND TIMESTAMP '{date_fin}' AND
                        (iddwh_typepublication = {typepublication} AND iddwh_typepublicationcouplage = {sourcecouplage}))
      )
      AS t1


INNER JOIN


     (
           SELECT *
                      FROM
                         (
                          SELECT
                               {annonce_cols},
                               CAST(from_iso8601_timestamp(CONCAT(CAST(year AS VARCHAR),'-',LPAD(CAST(month AS VARCHAR),2,'0'),'-',LPAD(CAST(day AS VARCHAR),2,'0'))) AS TIMESTAMP) AS datemaj

                               FROM "immobc"."annonce_history"
                         )

                      WHERE datemaj >= TIMESTAMP '{date_debut}' AND idtypetransaction = {idtypetransaction} AND idtypebien = {idtypebien}
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

                                  FROM "immobc".{typebien_table}
                          )
                      WHERE datemaj >= TIMESTAMP '{date_debut}'
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

                                  FROM "immobc".{typetransaction_table}
                          )
                      WHERE datemaj >= TIMESTAMP '{date_debut}' 
    )

AS t4

ON t1.iddwh_annonce = t4.{idannonce_join_for_typetransaction} AND t4.datemaj = t2.datemaj
"""