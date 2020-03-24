query = 
"""
SELECT t2.idannonce, t2.libelle_fr, si_meuble, "px", "prixmaxi" FROM


      (
           SELECT "iddwh_annonce"
                  from dwhdweb.dimannoncepublicationhisto
                  WHERE (datedebut >   timestamp '2020-03-01' AND datefin < timestamp '2020-03-15' AND
                        (iddwh_typepublication = 1 AND iddwh_typepublicationcouplage = 0))
      )
      AS t1


LEFT JOIN


     (
           SELECT *
                      FROM
                         (
                          SELECT
                               idannonce, libelle_fr,
                               CAST(from_iso8601_timestamp(CONCAT(CAST(year AS VARCHAR),'-',LPAD(CAST(month AS VARCHAR),2,'0'),'-',LPAD(CAST(day AS VARCHAR),2,'0'))) AS TIMESTAMP) AS datemaj

                               FROM "immobc"."annonce_history"
                         )

                      WHERE datemaj BETWEEN TIMESTAMP '2020-03-01' AND TIMESTAMP '2020-03-15'
    )
    AS t2

ON t1.iddwh_annonce = t2.idannonce

INNER JOIN


    (
           SELECT *
                      FROM
                          (
                          SELECT "idannonce", "si_meuble",
                                  CAST(from_iso8601_timestamp(CONCAT(CAST(year AS VARCHAR),'-',LPAD(CAST(month AS VARCHAR),2,'0'),'-',LPAD(CAST(day AS VARCHAR),2,'0'))) AS TIMESTAMP) datemaj

                                  FROM "immobc".abappartement_history
                          )
                      WHERE datemaj BETWEEN TIMESTAMP '2020-03-01' AND TIMESTAMP '2020-03-15'
    )
     AS t3

ON t1."iddwh_annonce" = t3."idannonce" AND t3.datemaj = t2."datemaj"

INNER JOIN

    (
           SELECT *
                      FROM
                          (
                          SELECT "idannonce", "px", "prixmaxi",
                                  CAST(from_iso8601_timestamp(CONCAT(CAST(year AS VARCHAR),'-',LPAD(CAST(month AS VARCHAR),2,'0'),'-',LPAD(CAST(day AS VARCHAR),2,'0'))) AS TIMESTAMP) datemaj

                                  FROM "immobc"."atvente_history"
                          )
                      WHERE datemaj BETWEEN TIMESTAMP '2020-03-01' AND TIMESTAMP '2020-03-15'
    )

AS t4

ON t1."iddwh_annonce" = t4."idannonce" AND t4.datemaj = t2."datemaj"




"""