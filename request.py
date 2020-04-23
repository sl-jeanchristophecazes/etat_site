# Paramètres : datedebut / datefin / typepublication / sourcecouplage 
# / table_transaction et ses colonnes / colonne de jointure date / colonne de jointure annonce
# / table_bien et ses colonnes / colonne de jointure date / colonne de jointure annonce
# 

from template_between_dates import query
from mappings import property_type_config, transaction_type_config


from template_instant import query
from mappings import property_type_config, transaction_type_config

def format_query_between_dates(date_debut, 
                               date_fin, 
                               typepublication,
                               sourcecouplage,
                               dim_annonce_col_list,
                               annonce_col_list,
                               typetransaction,
                               typetransaction_col_list,
                               typebien,
                               typebien_col_list, 
                               query, 
                               property_type_config, 
                               transaction_type_config
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
    
    # Join cols
    idannonce_join_for_annonce = annonce_col_list[0]
    idannonce_join_for_typetransaction = typetransaction_col_list[0]
    idannonce_join_for_typebien = typebien_col_list[0]
    
    # Getting transaction table name and idtypetransaction
    typetransaction_table = transaction_type_config[typetransaction]['table']
    idtypetransaction = transaction_type_config[typetransaction]['id']
    
    # Getting type bien table name and idtypebien
    typebien_table = property_type_config[typebien]['table']
    idtypebien = property_type_config[typebien]['id']
    
    # Config_dict
    config_dict = {'full_cols': full_cols,
                   'date_debut': date_debut,
                   'date_fin': date_fin, 
                   
                   # Publication et couplage
                   'typepublication': typepublication, 
                   'sourcecouplage': sourcecouplage,
                   
                   # Annonce
                   'dim_annonce_cols': dim_annonce_cols,
                   'annonce_cols': annonce_cols,
                   
                   # Transaction
                   'typetransaction_table': typetransaction_table,
                   'idtypetransaction': idtypetransaction,
                   'transaction_cols': transaction_cols,
                   
                   # Bien
                   'typebien_table': typebien_table,
                   'idtypebien': idtypebien,
                   'bien_cols': bien_cols,
                   
                   # PKEY joins
                   'idannonce_join_for_annonce': idannonce_join_for_annonce,
                   'idannonce_join_for_typetransaction': idannonce_join_for_typetransaction,
                   'idannonce_join_for_typebien': idannonce_join_for_typebien
                  }
    
    query = query.format(**config_dict)
    
    return(query)



def format_query_instant(date_debut,
                         typepublication,
                         sourcecouplage,
                         dim_annonce_col_list,
                         annonce_col_list,
                         typetransaction,
                         typetransaction_col_list,
                         typebien,
                         typebien_col_list, 
                         query, 
                         property_type_config, 
                         transaction_type_config
                        ):

    # Adding table alias for each col in list (list)
    dim_annonce_col_list_with_alias = ['full_dwh.' + col for col in dim_annonce_col_list]
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
    
    # Join cols
    idannonce_join_for_annonce = annonce_col_list[0]
    idannonce_join_for_typetransaction = typetransaction_col_list[0]
    idannonce_join_for_typebien = typebien_col_list[0]
    
    # Getting transaction table name and idtypetransaction
    typetransaction_table = transaction_type_config[typetransaction]['table']
    idtypetransaction = transaction_type_config[typetransaction]['id']
    
    # Getting type bien table name and idtypebien
    typebien_table = property_type_config[typebien]['table']
    idtypebien = property_type_config[typebien]['id']
    
    # Config_dict
    config_dict = {'full_cols': full_cols,
                   'date_debut': date_debut,
                   
                   # Publication et couplage
                   'typepublication': typepublication, 
                   'sourcecouplage': sourcecouplage,
                   
                   # Annonce
                   'dim_annonce_cols': dim_annonce_cols,
                   'annonce_cols': annonce_cols,
                   
                   # Transaction
                   'typetransaction_table': typetransaction_table,
                   'idtypetransaction': idtypetransaction,
                   'transaction_cols': transaction_cols,
                   
                   # Bien
                   'typebien_table': typebien_table,
                   'idtypebien': idtypebien,
                   'bien_cols': bien_cols,
                   
                   # PKEY joins
                   'idannonce_join_for_annonce': idannonce_join_for_annonce,
                   'idannonce_join_for_typetransaction': idannonce_join_for_typetransaction,
                   'idannonce_join_for_typebien': idannonce_join_for_typebien
                  }
    
    query = query.format(**config_dict)
    
    return(query)

