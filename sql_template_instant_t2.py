query = """
SELECT {full_cols} FROM


      (
            SELECT DISTINCT(table_max."iddwh_annonce") AS iddwh_annonce, DATE("datedebut") AS datedebut_ref

                    FROM "dwhdweb"."dimannoncepublicationhisto"

            INNER JOIN

            (
            SELECT "iddwh_annonce", MAX(datedebut) datemaj

                   FROM "dwhdweb"."dimannoncepublicationhisto" WHERE datedebut > timestamp '2020-03-01'

            GROUP BY "iddwh_annonce"
            )
            AS table_max

            ON table_max."iddwh_annonce" = "dwhdweb"."dimannoncepublicationhisto"."iddwh_annonce" AND "dwhdweb"."dimannoncepublicationhisto".datedebut = table_max.datemaj
      )
      AS t1

INNER JOIN


     (
           SELECT *
                      FROM
                         (
                          SELECT
                               {dim_annonce_cols} ,
                               DATE("datedebut") AS datedebut_ref

                               FROM "dwhdweb"."dimannoncepublicationhisto"
                         )
                      WHERE datedebut_ref >= TIMESTAMP '{datedebut}' AND (iddwh_typepublication = {} AND iddwh_typepublicationcouplage = {})

    )
    AS full_dwh

ON t1.iddwh_annonce = full_dwh.iddwh_annonce AND full_dwh."datedebut_ref" = t1.datedebut_ref

INNER JOIN


     (
           SELECT *
                      FROM
                         (
                          SELECT
                               {annonce_cols} ,
                               CAST(from_iso8601_timestamp(CONCAT(CAST(year AS VARCHAR),'-',LPAD(CAST(month AS VARCHAR),2,'0'),'-',LPAD(CAST(day AS VARCHAR),2,'0'))) AS TIMESTAMP) AS datemaj

                               FROM "immobc"."annonce_history"
                         )
                      WHERE datemaj >= TIMESTAMP '{date_t}'

    )
    AS t2

ON t1.iddwh_annonce = t2.{idannonce_join_for_annonce} AND t2."datemaj" = t1.datedebut_ref

INNER JOIN


    (
           SELECT *
                      FROM
                          (
                          SELECT  idannonce, si_meuble,
                                  CAST(from_iso8601_timestamp(CONCAT(CAST(year AS VARCHAR),'-',LPAD(CAST(month AS VARCHAR),2,'0'),'-',LPAD(CAST(day AS VARCHAR),2,'0'))) AS TIMESTAMP) datemaj

                                  FROM immobc.abmaison_history
                          )
                      WHERE datemaj >= TIMESTAMP '2020-03-01'
    )
     AS t3

ON t1.iddwh_annonce = t3.idannonce AND t3.datemaj = t2.datemaj

INNER JOIN

    (
           SELECT *
                      FROM
                          (
                          SELECT idannonce, px, prixmaxi,
                                  CAST(from_iso8601_timestamp(CONCAT(CAST(year AS VARCHAR),'-',LPAD(CAST(month AS VARCHAR),2,'0'),'-',LPAD(CAST(day AS VARCHAR),2,'0'))) AS TIMESTAMP) datemaj

                                  FROM immobc.atvente_history
                          )
                      WHERE datemaj >= TIMESTAMP '2020-03-01'
    )

AS t4

ON t1.iddwh_annonce = t4.idannonce AND t4.datemaj = t2.datemaj
"""