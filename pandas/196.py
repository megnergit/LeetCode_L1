import pandas as pd

dict_person=dict(id=[1,2,3], email=["john@example.com", 
                                    "bob@example.com",
                                    "john@example.com"])

person=pd.DataFrame.from_dict(dict_person)

print(person)


def delete_duplicate_emails(person: pd.DataFrame) -> None:
  person.sort_values(by=['id'])
  person.drop_duplicates(subset=["email"],
                         inplace=True, ignore_index=True, keep="first")
#  person.set_index('id', inplace=True)
  return person

#  return person.loc[:,["id", "email"]]

print(delete_duplicate_emails(person))






