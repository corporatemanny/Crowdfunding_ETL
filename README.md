# Crowdfunding ETL

## Overview
In our ETL mini project, we used Python, Pandas, and dictionary methods to extract and transform data from an excel file into a pandas dataframe.

## Purpose
For this project, we read the excel file into a pandas dataframe. We separated the category and subcategory values into separate columns. From there, we assigned each category amd subcategory an ID. We used the IDs to create new dataframes, one each for Category and Subcategory.

With our data extracted, we updated some of the column names, changed the data types to more appropriate types, merged the category and subcategroy dataframes into the main dataframe, and then dropped the columns we didn't need. We saved the result to a CSV file.

The second file required us iterate through the data and convert the rows to a dictionary. After checking the resultant info for the dataframe, we split the name field into two columns, the reorganized the columns to put the names before the email addresses. After double-checking the database, we exported it to a CSV file.

Once both files were saved, we loaded them to a database.

## Summary
By bringing this data, which was housed in separate, discrete locations, and bringing them together within pandas dataframes, and then a database, we make it easier to pull and manipulate the data for future analysis and quicker data retrieval. 
