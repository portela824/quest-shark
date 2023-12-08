#José G Portela & Edwardo S. Rivera
# Check if this works
def set_pd_options(rows=1000,cols=30):
    import pandas as pd
    try:
        pd.set_option('display.max_rows', rows)
        pd.set_option('display.max_columns', cols)
        return True
    except:
        print("Error on input, must be an integer")
        return False
# read excel given filename
def read_excel_to_df(file='GSAF5.xls'):
    import pandas as pd
    try:
        df = pd.read_excel(file)
        return df
    except:
        print("Cannot read file, please make sure you added the correct extension or file path")
        return None
# rename columns removing spaces and putting to lower   
def rename_columns(df):
    # rename columns
    df.columns = df.columns.str.strip().str.replace(" ", "_").str.lower()
    return df
# helper function for clear_country. Given a string, if it eds with '?' remove it at the end (apply)    
def clean_char(el,char='?'):
    if el.endswith(char):
        return el[:-1]
    else:
        return el    
# clean country varible
def clean_country(df):
    df['country'] = df['country'].fillna('').str.lower().str.strip() # fill na with '', put lowercase and remove spaces
    df['country'] = df['country'].apply(clean_char)  # to lower, remove ? at the end
    df['country'] = df['country'].str.replace(' (uae)','').str.replace('&','and').str.replace(' (sri lanka)','').str.replace('columbia','colombia').str.replace('coast of africa','africa').str.replace('st. martin','st martin').str.replace('st. maartin','')
    return df
# cleaner for activity
def clean_helper(row,mydict):
    for key,value in mydict.items():
        if key in row.lower():
            return value
    return row

def clean_activity(df):
    mydict = {'diving':'diving',
          'accident':'accident',
          'waves':'surfing',
          'adrift':'adrift',
          'attempting':'attempt',
          'attempted':'attempt',
          'bathing':'bathing',
          'boat':'boat',
          'body':'boogie',
          'boogie':'boogie',
           'canoe':'canoe',
          'collecting':'collect',
          'dived':'diving',
          'diving': 'diving',
          'fishing':'fishing',
          'swimming':'swimming',
          'disaster':'sea disaster',
          'boat':'sea disaster',
          'air':'sea disaster',
          'ship':'sea disaster',
          'typhoon':'sea disaster',
          'cyclone':'sea disaster',
          'beach':'beach',
          'feeding':'feeding',
          'fell':'fell',
          'floating':'floating',
          'jumped':'jumped',
          'jumping':'jumped',
          'kayak':'kayak',
          'kite':'kite',
          'paddle':'paddling',
          'paddling':'paddling',
          'surf':'surfing',
          'sailing':'sea disaster',
          'sea disaster':'sea disaster',
          'sinking':'sinking',
          'snorkeling':'snorkeling',
          'spearfishing':'fishing',
          'standing':'standing',
          'treading': 'swimming',
          'photo': 'photography',
          'wading': 'swimming',
          'wade':'swimming',
          'washing':'washing',
          'wreck':'sea disaster',
          'yacht':'sea disaster'
          }
    df['activity'] = df['activity'].fillna('not_confirmed').str.lower().str.strip()
    df['activity'] = df['activity'].apply(clean_helper,mydict=mydict)
    return df

def clean_type(df):
    df["type"] = df["type"].fillna('Unconfirmed')
    df["type"] = df["type"].replace({"?": "Unconfirmed", "Unconfirmed": "Unconfirmed", "Unverified": "Unconfirmed", "Under investigation":"Unconfirmed","Questionable":"Unconfirmed"})
    df["type"] = df["type"].str.lower()
    return df