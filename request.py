# Paramètres : datedebut / datefin / typepublication / sourcecouplage 
# / table_transaction et ses colonnes / colonne de jointure date / colonne de jointure annonce
# / table_bien et ses colonnes / colonne de jointure date / colonne de jointure annonce
# 

from sql_template import query

def format_query(date_debut, 
                date_fin, 
                typepublication,
                sourcecouplage,
                dim_annonce_col_list,
                annonce_col_list,
                typetransaction_table,
                typetransaction_col_list,
                typebien_table,
                typebien_col_list, 
                query
                ):

    # Adding table alias for each col in list (list)
    dim_annonce_col_list_with_alias = ['t1.' + col for col in dim_annonce_col_list]
    annonce_col_list_with_alias = ['t2.' + col for col in annonce_col_list]
    typebien_col_list_with_alias = ['t3.' + col for col in typebien_col_list]
    typetransaction_col_list_with_alias = ['t4.' + col for col in typetransaction_col_list]

    # joining them together (str)
    dim_annonce_col_string = ', '.join(dim_annonce_col_list_with_alias)
    annonce_col_string = ', '.join(annonce_col_list_with_alias)
    typebien_col_string = ', '.join(typebien_col_list_with_alias)
    typetransaction_col_string = ', '.join(typetransaction_col_list_with_alias)

    # Full columns for all the tables (str)
    full_cols = dim_annonce_col_string + ', ' + annonce_col_string + ', ' + typebien_col_string \
                + ', ' + typetransaction_col_string

    # Full columns for dim_annonce (str)
    dim_annonce_cols = ', '.join(dim_annonce_col_list)

    # Full columns for annonce_history (str)
    annonce_cols = ', '.join(annonce_col_list)

    # Full columns for typetransaction_table (str)
    transaction_cols = ', '.join(typetransaction_col_list)

    # Full columns for typebien_table (str)
    bien_cols = ', '.join(typebien_col_list)

    idannonce_join_for_annonce = annonce_col_list[0]
    idannonce_join_for_typetransaction = typetransaction_col_list[0]
    idannonce_join_for_typebien = typebien_col_list[0]
    
    # config_dict
    config_dict = {'full_cols': full_cols,
                   'date_debut': date_debut,
                   'date_fin': date_fin, 
                   'typepublication': typepublication, 
                   'sourcecouplage': sourcecouplage,
                   'dim_annonce_cols': dim_annonce_cols,
                   'annonce_cols': annonce_cols,
                   'transaction_cols': transaction_cols,
                   'typebien_table': typebien_table,
                   'typetransaction_table': typetransaction_table,
                   'bien_cols': bien_cols,
                   'idannonce_join_for_annonce': idannonce_join_for_annonce,
                   'idannonce_join_for_typetransaction': idannonce_join_for_typetransaction,
                   'idannonce_join_for_typebien': idannonce_join_for_typebien
                  }
    
    query = query.format(**config_dict)
    
    return(query)



if __name__ == '__main__':

    full_cols, dim_annonce_cols, annonce_cols, transaction_cols, bien_cols = format_query(date_debut = '2020-03-01', 
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

    print(transaction_cols)