# Pythong-Challenge

Resources

https://docs.python.org/3/tutorial/inputoutput.html

https://note.nkmk.me/en/python-key-sort-sorted-max-min/

https://www.w3schools.com/python/ref_dictionary_items.asp

https://www.w3schools.com/python/ref_dictionary_get.asp

https://www.w3schools.com/python/ref_dictionary_keys.asp

https://www.tutorialspoint.com/python/os_chdir.htm

https://docs.python.org/3/library/os.path.html


ReadMe Notes

# Campaign DataFrame

## Create a Campaign DataFrame that has the following columns:

The "cf_id" column.

The "contact_id" column.

The “company_name” column.

The "blurb" column is renamed as "description."

The "goal" column.

The "goal" column is converted to a float datatype.

The "pledged" column is converted to a float datatype.

The "backers_count" column.

The "country" column.

The "currency" column.

The "launched_at" column is renamed as "launch_date" and converted to a datetime format.

The "deadline" column is renamed as "end_date" and converted to a datetime format.

The "category_id" with the unique number matching the “category_id” from the category DataFrame.

The "subcategory_id" with the unique number matching the “subcategory_id” from the subcategory DataFrame.

And, create a column that contains the unique four-digit contact ID number from the contact.xlsx file.

Then export the DataFrame as a campaign.csv CSV file.

## Description

I started by creating a copy of the crowdfunding info data frame named campaign_df as instructed. I renamed the columns based on the names provided using .rename. I
I assigned the goal and pledged columns to float data types. I convereted the launch_date and end_date columns to datetime format using the .strftime() function to convert
the date and time objects to their string representation. I then merged the campaign dataframe with the category and subcategory dataframes respectively. I finished by dropping the category & sub-category, category, and subcategory columns and exporting the dataframe to a csv file with the code provided.  

## Contacts Dataframe

Create a Contacts DataFrame that has the following columns:

A column named "contact_id" that contains the unique number of the contact person.

A column named "first_name" that contains the first name of the contact person.

A column named "last_name" that contains the first name of the contact person.

A column named "email" that contains the email address of the contact person

Then export the DataFrame as a contacts.csv CSV file.

# Option 2: Use regex to create the contacts DataFrame

## Description

I started by creating a copy of the contacts dataframe. I noticed that the header row was with the rest of the values in the dataframe so I converted the first row to the header of the column. I extracted the contact ID number by using a regular experssion and .str.extract() to find specifially a number that is four digits. I checked the datatypes as instructed. I changed the contact_ID cvalues to int64 data type by using .astype() and specifying int64 as a string. To find the names in dataframe and add them to a new column I used the same idea as I did when trying to find the contact ID. I noticed that both the first and last name were capitalized and was able to create a regular expression specifically looking for capital letters. To find the email addresses, I started by using a regular expression that finds based on "email": specifically. It looked something like this ('("email":\s\W[a-z]\w*\.*\W[a-z]\w*\@*\W[a-z]\w*\.*\w{2,})'). I noticed that because I was using .str.extraact it was pulling the "email": part as well in the output. I refined my regular expression this time focusing on the @ symbol spefically and was able to get the output. By printing all the rows in the dataframe I noticed some values returned as NaN and that was due to not including special characters and numbers as some people's emails included hyphens. I then created the new dataframe including the information we retrived up until this point. I then split the name column into first and last name using .str.split passing over the name column. I dropped the name column, reorganized the dataframe in the instructed format, checked that datatypes one last time and exported the dataframe to a csv file with the code provided.

# References

https://stackoverflow.com/questions/14745022/how-to-split-a-dataframe-string-column-into-two-columns

https://stackoverflow.com/questions/69788264/appending-a-string-during-list-comprehension-with-np-arange

https://stackoverflow.com/questions/43956335/convert-float64-column-to-int64-in-pandas

https://stackoverflow.com/questions/67394800/regex-to-extract-numbers-length-4-from-a-dataframe-column

https://sparkbyexamples.com/pandas/pandas-convert-row-to-column-header-in-dataframe/

https://stackoverflow.com/questions/67237455/how-to-find-all-words-with-first-letter-as-upper-case-using-python-regex

https://dev.to/chanduthedev/how-to-display-all-rows-from-data-frame-using-pandas-dha

https://stackoverflow.com/questions/42407785/regex-extract-email-from-strings

   
