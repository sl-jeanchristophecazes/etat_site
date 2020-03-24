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

    return(full_cols)


if __name__ == '__main__':

    res = format_query(date_debut = '2020-03-01', 
                datefin = '2020-03-15', 
                typepublication = 1,
                sourcecouplage = 0,
                dim_annonce_col_list = ['iddwh_annonce'],
                annonce_col_list = ['idannonce','libelle_fr'],
                typetransaction_table = 'immobc.abappartement_history',
                typetransaction_col_list = ['idannonce', 'px', 'prixmaxi'],
                typebien_table = 'immobc.atvente_history',
                typebien_col_list = ['idannonce', 'si_meuble']
                )

    print(res)