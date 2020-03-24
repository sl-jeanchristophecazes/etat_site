# Paramètres : datedebut / datefin / typepublication / sourcecouplage 
# / table_transaction et ses colonnes / colonne de jointure date / colonne de jointure annonce
# / table_bien et ses colonnes / colonne de jointure date / colonne de jointure annonce
# 

def format_query(date_debut, 
                datefin, 
                typepublication,
                sourcecouplage,
                dim_annonce_col_list,
                annonce_col_list,
                typetransaction_table,
                typetransaction_col_list,
                typebien_table,
                typebien_col_list
                ):

    # Full columns for all the tables (str)
    full_cols = ''

    # Full columns for annonce_history (str)
    annonce_cols = ''

    # Full columns for typetransaction_table (str)
    transaction_cols = ''

    # Full columns for typebien_table (str)
    bien_cols = ''

    idannonce_join_for_annonce = ''
    idannonce_join_for_typetransaction = ''
    idannonce_join_for_typebien = ''
