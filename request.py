# Paramètres : datedebut / datefin / typepublication / sourcecouplage 
# / table_transaction et ses colonnes / colonne de jointure date / colonne de jointure annonce
# / table_bien et ses colonnes / colonne de jointure date / colonne de jointure annonce
# 

def format_query(date_debut, 
                datefin, 
                typepublication,
                sourcecouplage,
                typetransaction_table,
                typetransaction_cols,
                typetransaction_join_idannonce,
                typetransaction_join_datemaj,
                typepublication_table,
                typepublication_cols,
                typepublication_join_idannonce,
                typepublication_join_datemaj
                ):

    # Full column list for all the tables
    
    full_cols = []

    

